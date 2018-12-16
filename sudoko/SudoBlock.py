class SudoBlock:
    # data
    # python中的字典无下标,直接导致设计的算法出现问题
    def __init__(self, block_num):
        self.block_num = block_num
        # 0_4_8为填好的内容

        # 存储了True,False的链表
        self.block_ele_possible_coordinate_subs_jud = []
        self.find_ele_subs = []
        self.coordinate = []
        self.now_ele = []
        self.ele = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.coordinate_ele = {}
        # last_modified里面存储了上一次更改时改动过的相对block内坐标
        # 相对block内坐标如下定义：
        # 0 1 2
        # 3 4 5
        # 6 7 8
        self.modified_by_this_block_coordinate_subs_stack = []
        self.modified_by_other_coordinate_subs_stack = []

        if block_num == 0 or block_num == 4 or block_num == 8:
            return
        a = int(block_num / 3)
        b = int(block_num % 3)
        for i in range(0, 3):
            row = a * 3 + i
            for j in range(0, 3):
                col = b * 3 + j
                self.coordinate.append((row, col))
        for tmp_ele in self.ele:
            self.now_ele.append(0)
        # 初始化block_ele_possible_coordinate_subs_jud
        # 其中第一个下标表示ele:
        # 第二个下标表示的是在self.coordinate中下标对应的坐标
        for tmp_ele in self.ele:
            self.block_ele_possible_coordinate_subs_jud.append([])
            self.block_ele_possible_coordinate_subs_jud[tmp_ele].append(True)
            for tmp_coordinate in self.coordinate:
                self.block_ele_possible_coordinate_subs_jud[tmp_ele].append(True)
        for i in range(0, 10):
            self.find_ele_subs.append(0)

        # 初始化表格
        for tmp_coordinate in self.coordinate:
            self.coordinate_ele[tmp_coordinate] = 0

    # 测试block初始化是否正确
    def print_block(self):
        print(self.block_num)
        print(self.block_ele_possible_coordinate_subs_jud)
        for i in range(0,len(self.block_ele_possible_coordinate_subs_jud)):
            print("ele = ",i,self.block_ele_possible_coordinate_subs_jud[i])
        print()
        print(self.find_ele_subs)

    # 查找函数
    def find_by_ele(self, ele):
        return_jud = False
        return_coordinate = (0, 0)
        tmp_subs = 0
        # 从上一次找到True的地方后一个开始寻找，如果找到下一个True
        for i in range(self.find_ele_subs[ele] + 1, 10):
            if self.block_ele_possible_coordinate_subs_jud[ele][i] == True:
                return_jud = True
                return_coordinate = self.coordinate[i]
                tmp_subs = i
                break
        if not return_jud:
            tmp_subs = 0
        self.find_ele_subs[ele] = tmp_subs
        return [return_jud, return_coordinate]

    # 将ele填入coordinate中。
    def modify_by_coordinate_in_this_block(self, coordinate, ele):
        tmp_modified_list = []
        for tmp_coordinate_subs in range(0, len(self.block_ele_possible_coordinate_subs_jud[ele])):
            if self.block_ele_possible_coordinate_subs_jud[ele][tmp_coordinate_subs]:
                tmp_modified_list.append(tmp_coordinate_subs)
                self.block_ele_possible_coordinate_subs_jud[ele][tmp_coordinate_subs] = False
        self.coordinate_ele[coordinate] = ele
        self.modified_by_this_block_coordinate_subs_stack.append(tmp_modified_list)
        pass

    # 撤销对此块中的更改
    def retract_modify_by_coordinate_in_this_block(self, coordinate, ele):
        tmp_modified_list = []
        tmp_modified_list = self.modified_by_this_block_coordinate_subs_stack[-1]
        for tmp_coordinate_subs in tmp_modified_list:
            self.block_ele_possible_coordinate_subs_jud[ele][tmp_coordinate_subs] = True
        self.coordinate_ele[coordinate] = 0
        self.modified_by_this_block_coordinate_subs_stack.pop()
        pass

    #在coordinate中填入ele，此操作会影响其他block
    #根据行列不同进行更改
    def modify_by_coordinate_in_other_block(self, coordinate, ele, type='row'):

        pass

    #
    def retract_modify_by_coordinate_in_other_block(self, coordinate, ele, type='row'):
        tmp_modified_by_coordinate_subs = []
        tmp_modified_by_coordinate_subs = self.modified_by_other_coordinate_subs_stack[-1]
        for tmp_coordinate_subs in tmp_modified_by_coordinate_subs:
            self.block_ele_possible_coordinate_subs_jud[ele][tmp_coordinate_subs] = True