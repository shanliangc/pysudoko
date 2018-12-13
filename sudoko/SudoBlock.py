class SudoBlock:
    #data
    num = 0
    #possible_element每个possible_element[i]代表
    possible_element = []

    def __init__(self,num):
        self.num = num
        print("SudoBlock __init__ num = ",self.num)
        a = int(num/3)
        b = int(num%3)
        #为什么会出现这种情况？？？？？
        #在初始化的时候已经有了前面的数据了？？？
        #了解清楚？
        print("pre len =",len(self.possible_element))
        for n in range(0,10):
            self.possible_element.append([])
        print("mid len = ",len(self.possible_element))

        for i in range(0,3):
            row = a*3 + i
            for j in range(0,3):
                col = b*3 + j
                for n in range(1,10):
                    self.possible_element[n].append((row,col))
        print("aft len =",len(self.possible_element))

    #对可能的数字进行更新
    def upgrade_possible_element(self,element,row,col):
        self.possible_element[element].append((row,col))

    def print_block(self):
        print("num = ",self.num)
        print(len(self.possible_element))
        for ele in self.possible_element:
            print(ele,end = " ")
        print()

