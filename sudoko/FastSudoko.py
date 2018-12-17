import random
import codecs
class FastSudokoGenerator():

    # 初始化剩余的数字
    def __init__(self,res):
        self.res = res
        self.ans = []

    def create_puzzle(self):
        # 初始化
        sequence = [3, 6, 1, 4, 7, 2, 5, 8]
        while self.res > 0:
            random_ele_sequence = random.sample(range(1, 10), 9)
            # 调整成2在左上角
            random_ele_sequence.remove(2)
            random_ele_sequence.insert(0, 2)
            ls = []
            for ele in random_ele_sequence:
                ls.append(str(ele))
            random_ele_sequence = ls.copy()
            table = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            table[0] = random_ele_sequence.copy()
            for i in sequence:
                tmp = random_ele_sequence[-1]
                random_ele_sequence.pop()
                random_ele_sequence.insert(0, tmp)
                table[i] = random_ele_sequence.copy()
            # 通过交换的方式生成新的矩阵
            for i in range(1, 3):
                for tmp_i in range(1, 3):
                    if tmp_i == i:
                        continue
                    if self.res == 0:
                        break
                    table[i], table[tmp_i] = table[tmp_i], table[i]
                    for j in range(3, 6):
                        for tmp_j in range(3, 6):
                            if tmp_j == j:
                                continue
                            if self.res == 0:
                                break
                            table[j], table[tmp_j] = table[tmp_j], table[j]
                            for k in range(6, 9):
                                for tmp_k in range(6, 9):
                                    if tmp_k == k:
                                        continue
                                    if self.res == 0:
                                        break
                                    table[k], table[tmp_k] = table[tmp_k], table[k]
                                    self.res -= 1
                                    s = ''
                                    for row in table:
                                        for i in range(0,8):
                                            s += row[i]
                                            s += ' '
                                        s += row[8]
                                        s += '\n'
                                    s += '\n'
                                    self.ans.append(s)
                                    table[k], table[tmp_k] = table[tmp_k], table[k]
                            #调整回原来状态
                            table[j], table[tmp_j] = table[tmp_j], table[j]
                    # 调整回原来状态
                    table[i], table[tmp_i] = table[tmp_i], table[i]

    def write_to_file(self,file_path):
        file = codecs.open(file_path,'a','utf-8')
        for row in self.ans:
            file.write(row)
        file.close()
            #结尾添一行