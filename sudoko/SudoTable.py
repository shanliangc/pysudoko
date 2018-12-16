import sudoko.SudoBlock
import random
import codecs


def ele_compare(ele):
    return ele[1]

class SudoTable:
    # data:
    ele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    block_num = [1, 2, 5, 3, 6, 7]
    path = []
    ans = []
    left_puzzle = 0

    def __init__(self, left_puzzle):
        # res是一个终局还代填的数字
        self.res = 81
        # path出发的位置
        self.start = 0
        # 坐标对应的数值是否存在可能
        self.coordinate_ele_jud = {}
        # 终局结果
        self.table = []
        # 初始化最终答案
        for i in range(0, 9):
            self.table.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        # 初始化坐标对应的可能的元素值
        for row in range(0, 9):
            for col in range(0, 9):
                self.coordinate_ele_jud[(row, col)] = {}
                for tmp_ele in self.ele:
                    self.coordinate_ele_jud[(row, col)][tmp_ele] = True
        # 初始化路径
        for tmp_ele in self.ele:
            for tmp_block_num in self.block_num:
                self.path.append((tmp_ele, tmp_block_num))
        # 初始化还剩下的终局数量
        self.left_puzzle = left_puzzle

    def print_table(self):
        pass

    # 自动生成一个终局
    def generate_sudoko_puzzle(self):
        self.generate_0_4_8_block(0)
        self.generate_0_4_8_block(4)
        self.generate_0_4_8_block(8)
        self.search_a_puzzle(0)
        # for i in range(0, 9):
        #     print(self.table[i])
        #     if i % 3 == 2:
        #         print()
        # print()

    # 自动生成0、4、8方块的算法
    def generate_0_4_8_block(self, block_num):
        random_ele_sequence = random.sample(range(1, 10), 9)
        if block_num == 0:
            subs = 0
            for i in range(0, 9):
                if random_ele_sequence[i] == 2:
                    subs = i
                    break
            random_ele_sequence[subs] = random_ele_sequence[0]
            random_ele_sequence[0] = 2
        subs = 0
        a = int(block_num / 3)
        b = int(block_num % 3)
        for i in range(0, 3):
            row = a * 3 + i
            for j in range(0, 3):
                col = b * 3 + j
                tmp_ele = random_ele_sequence[subs]
                self.table[row][col] = random_ele_sequence[subs]
                # 更改其他行列剩余的可能的值
                # python的不灵活性体现在一下的句子中，如果这里不用tmp_ele而用random_ele_sequence[subs]
                # 是会报错的
                # 可能传入一个list特定下标的值对我们来说事已知的，但是python在传入的时候，必须传入一次访问就存在的切实的数
                self.coordinate_ele_jud[(row, col)][tmp_ele] = False
                for tmp_row in range(0, 9):
                    self.coordinate_ele_jud[(tmp_row, col)][tmp_ele] = False
                for tmp_col in range(0, 9):
                    self.coordinate_ele_jud[(row, tmp_col)][tmp_ele] = False
                # 很明显对于0、4、8block而言，这些block里面
                for tmp_ele in self.ele:
                    self.coordinate_ele_jud[(row, col)][tmp_ele] = False

                # 剩余代填的空格数量-1
                self.res -= 1
                subs += 1

    def search_possible_coordinate_for_ele(self, ele, block_num):
        a = int(block_num / 3)
        b = int(block_num % 3)
        possible_coordinate = []
        for i in range(0, 3):
            row = a * 3 + i
            for j in range(0, 3):
                col = b * 3 + j
                if self.coordinate_ele_jud[(row, col)][ele]:
                    possible_coordinate.append((row, col))
        return possible_coordinate

    # 寻找一个终局
    # 把上一个传进来
    #
    def search_a_puzzle(self, start):
        if start >= len(self.path):
            # print("end")
            # print("end")
            self.left_puzzle -= 1
            self.ans.append(self.table)
            # for row in self.table:
            #     print(row)
            # print()

            # print("end2222")
            return True
        # 当前要填的是哪一个元素，哪一个格子
        (ele, block_num) = self.path[start]
        # print("start = ", start, " ", (ele, block_num))
        # 寻找当前block，可以填上ele的坐标有哪些
        possible_coordinate = self.search_possible_coordinate_for_ele(ele, block_num)
        # print(possible_coordinate)
        is_find = False
        if len(possible_coordinate) == 0:
            # print('sssssssssssssssssssssss')
            return False
        for (row, col) in possible_coordinate:
            # 对于每一个当前block可以填下数字ele的坐标而言
            # 记录因在这个coordinate填写当前ele而改变的状态，保存下来
            self.table[row][col] = ele
            changed_coordinate = []
            # 更改自身的值
            changed_this_coordinate_ele = []
            for tmp_ele in self.ele:
                if self.coordinate_ele_jud[(row, col)][tmp_ele]:
                    self.coordinate_ele_jud[(row, col)][tmp_ele] = False
                    changed_this_coordinate_ele.append(tmp_ele)
            # 更改同一个block的
            a = int(block_num / 3)
            b = int(block_num % 3)
            for i in range(0, 3):
                tmp_row = a * 3 + i
                for j in range(0, 3):
                    tmp_col = b * 3 + j
                    if self.coordinate_ele_jud[(tmp_row, tmp_col)][ele]:
                        changed_coordinate.append((tmp_row, tmp_col))
                        self.coordinate_ele_jud[(tmp_row, tmp_col)][ele] = False
            # 更改同行的
            for tmp_row in range(0, 9):
                if self.coordinate_ele_jud[(tmp_row, col)][ele]:
                    changed_coordinate.append((tmp_row, col))
                    self.coordinate_ele_jud[(tmp_row, col)][ele] = False
            # 更改同列的
            for tmp_col in range(0, 9):
                if self.coordinate_ele_jud[(row, tmp_col)][ele]:
                    changed_coordinate.append((row, tmp_col))
                    self.coordinate_ele_jud[(row, tmp_col)][ele] = False
            # 根据路径寻找下一个
            # 如果下一个返回的是False，则代表不能找到
            # 如果下一个返回的值是True，代表已经找到了结果
            # print("coordinate = ", (row,col),"changed_coordinate = ", changed_coordinate)
            is_find = self.search_a_puzzle(start + 1)
            if is_find:
                # self.table[row][col] = ele
                break
            else:
                # 如果没有找到答案，则把已经更改的状态退回来
                # 更改已经改过的
                self.table[row][col] = 0
                for (tmp_row, tmp_col) in changed_coordinate:
                    self.coordinate_ele_jud[(tmp_row, tmp_col)][ele] = True
                for tmp_ele in changed_this_coordinate_ele:
                    self.coordinate_ele_jud[(row, col)][tmp_ele] = True
        # 填不了了为什么没有回退上一个呢？
        # 为什么会出现同行的现象？ 改得不够彻底吗？
        if is_find:
            return True
        else:
            return False

    # 重新开始我们的故事：
    def clean_data(self):
        for row in range(0, 9):
            for col in range(0, 9):
                self.table[row][col] = 0
                for tmp_ele in self.ele:
                    self.coordinate_ele_jud[(row, col)][tmp_ele] = True
        self.res = 81
        self.start = 0

    def write_answer_to_file(self, file_path):
        file = codecs.open()
        for tmp_table in self.ans:
            for row in range(0, 9):
                for col in range(0, 9):
                    tmp_ele = tmp_table[row][col]
                    if col == 8:
                        file.write(tmp_ele, "\n")
                    else:
                        file.write(tmp_ele, " ")
            file.write("\n")



    def solve_a_puzzle(self, table):
        self.clean_data()
        # 构建一个数据结构
        # 这个数据结构里标着False的，代表这个单元格里面这个元素还没有被填入
        block_num_ele = []
        for i in range(0, 9):
            # 填1~9，全为True,0为False（0不填）
            block_num_ele.append([False, True, True, True, True, True, True, True, True, True])

        for row in range(0, 9):
            for col in range(0, 9):
                ele = table[row][col]
                # 如果是未填写的数，则继续
                if ele == 0:
                    continue
                # 如果是已经填写的数，先计算这个数所在的block
                a = int(row / 3)
                b = int(col / 3)
                tmp_block_num = a * 3 + b
                block_num_ele[tmp_block_num][ele] = False

                # 更改自身
                for tmp_ele in self.ele:
                    self.coordinate_ele_jud[(row, col)][tmp_ele] = False
                # 更改本block里面的其他坐标
                for i in range(0, 3):
                    tmp_row = a * 3 + i
                    for j in range(0, 3):
                        tmp_col = b * 3 + j
                        self.coordinate_ele_jud[(tmp_row, tmp_col)][ele] = False
                # 更改同行的
                for tmp_row in range(0, 9):
                    self.coordinate_ele_jud[(tmp_row, col)][ele] = False
                # 更改同列的
                for tmp_col in range(0, 9):
                    self.coordinate_ele_jud[(row, tmp_col)][ele] = False

        # 初始化状态后，统计每个元素剩余的代填格数是什么
        ls = []
        for tmp_block_num in range(0,9):
            n = 0
            for tmp_ele in range(1,10):
                if block_num_ele[tmp_block_num][tmp_ele]:
                    n += 1
            ls.append((tmp_block_num, n))
        ls.sort(key=ele_compare)
        for (tmp_block_num, left) in ls:
            for tmp_ele in range(1,10):
                if block_num_ele[tmp_block_num][tmp_ele]:
                    self.path.append((tmp_block_num, tmp_ele))
        self.search_a_puzzle(0)