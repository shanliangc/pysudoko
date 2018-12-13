import sudoko.SudoBlock
import random
class SudoTable:
    #data:
    res = 81
    table = []
    row_possible_element = []
    col_possible_element = []
    sudo_block = []
    order = [2,8,7,4,7,3]

    #function:
    #简要讲解一下生成算法：
    #生成算法先随机生成0、4、8block的值，因为0、4、8模块的值是互不冲突的，所以可以直接填上
    #再使用回溯法，分别填1，2，3，4，5，6，7，8，9的值，这里的填法是先将某一个数字填满9个不同的block
    #填数字的格的序号是：[2,8,7,4,6,3]，其中这串数字已经被记录在order中，直接使用就可以
    #初始化函数
    def __init__(self):
        self.res = 81
        for i in range(0,9):
            #初始化表格,全部初始化成0
            self.table.append([0,0,0,0,0,0,0,0,0])
            #初始化每一行。
            self.row_possible_element.append([])
            self.col_possible_element.append([])
            #初始化每一行、每一列的可能值
            for j in range(1,10):
                self.row_possible_element[i].append(j)
                self.col_possible_element[i].append(j)
            #初始化数独块
            tmp_block = sudoko.SudoBlock.SudoBlock(i)
            print(tmp_block)
            self.sudo_block.append(tmp_block)
        print("block len = ",len(self.sudo_block))

            #测试构建的结果，发现存在问题
            # tmp_block.print_block()

    #生成数独库文件，同时返回table的值，以便将table写入最终的文件中
    def generate_sudoku(self):
        #先填满0_4_8模块的内容
        self.initialize_0_4_8_block()
        #再一次不足2、8、7、4、1、3模块中的可能值
        self.upgrade_2_8_7_4_1_3()

        #最后返回table值。将table保存在一个更大的链表中，可以逐一将table的值写入结果方程中
        return self.table

    #打印函数
    def print_SudoTable(self):
        print("res = ",self.res)
        for raw in self.table:
            for element in raw:
                print(element,end=' ')
            print()
        print()

    #对一个block里面的数字进行随机化处理
    def initialize_element_group_in_1_9(self,num):
        rs = random.sample(range(1,10),9)
        #应作业的要求，我的学号后两位是1，0，所以左上角的数字应该为(1+0)%9+1 = 2
        if num == 0:
            tmp = 0
            for i in range(0,9):
                if rs[i] == 2:
                    tmp = i
                    break
            rs[tmp] = rs[0]
            rs[0] = 2
        return rs

    #对一次性填满的词块进行处理
    def process_element_group_in_0_4_8(self,rs,num):
        a = int(num/3)
        b = int(num%3)
        tmp = 0
        # print("rs",num," = ",rs,"process_element_group_in_0_4_8")
        # print((a,b))
        for i in range(0,3):
            row = a * 3 + i
            for j in range(0,3):
                col = b*3 + j
                #对整个词块进行处理
                self.table[row][col] = rs[tmp]

                #删除行中可能的值
                self.row_possible_element[row].remove(rs[tmp])
                #删除列中可能的值
                self.col_possible_element[col].remove(rs[tmp])
                tmp += 1
                # 剩余的填词数--
                self.res -= 1
        # self.print_SudoTable()

    #查看还剩下的行和列的值：
    def print_possible_element(self):
        print("row_possible_element:")
        for ele in self.row_possible_element:
            print(ele)
        print("col_possible_element:")
        for ele in self.col_possible_element:
            print(ele)

    #初始化0_4_8中的数字
    def initialize_0_4_8_block(self):
        #生成第0个block里面的数字：
        rs1 = self.initialize_element_group_in_1_9(0)
        # print("rs0 = ",rs1)
        self.process_element_group_in_0_4_8(rs1,0)
        # print("**************")
        #生成第4个block里面的数字：
        rs2 = self.initialize_element_group_in_1_9(4)
        # print("rs4 = ",rs2)
        self.process_element_group_in_0_4_8(rs2,4)
        # print("**************")
        #生成第8个block里面的数字：
        rs3 = self.initialize_element_group_in_1_9(8)
        # print("rs8 = ",rs3)
        self.process_element_group_in_0_4_8(rs3,8)

        del rs1,rs2,rs3
        # print("**************")
    
    #对block中的情况进行更新，此函数发生在初始完0、4、8模块以后
    def upgrade_2_8_7_4_1_3(self):
        for num in self.order:
            a = int(num/3)
            b = int(num%3)
            for i in range(0,3):
                row = a * 3 + i
                for j in range(0,3):
                    col = b*3 + j
                    ls = [tmp for tmp in self.row_possible_element[row] if tmp in self.col_possible_element]
                    print((row,col))
                    print(ls)
                    for ele in ls:
                        #更新可能的值
                        self.sudo_block[num].upgrade_possible_element(ele,row,col)

    #检查sudoko_block的情况
    def check_sudo_block(self):
        for num in self.order:
            self.sudo_block[num].print_block()








