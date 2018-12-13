class SudoBlock:
    #data
    #possible_element每个possible_element[i]代表
    #建立一个私有的
    def __init__(self,num):
        self.num = num
        self.stored_coordinate_num = {}
        self.possible_element = {}
        #0或4或8是处理过的单元格不必再次处理
        if num == 0 or num == 4 or num == 8:
            return
        a = int(num/3)
        b = int(num%3)
        for i in range(0,3):
            row = a*3+i
            for j in range(0,3):
                col = b*3+j
                self.stored_coordinate_num[(row,col)] = 0
        for i in range(0,10):
            #只需要1~9
            self.possible_element[i] = {}
            if i == 0:
                continue
            #now是为了以后搜索时回溯，搜索从now以后到结尾可能的坐标
            self.possible_element[i]['now'] = 0
            for coordinate in self.stored_coordinate_num.keys():
                self.possible_element[i][coordinate] = 'true'

    #清理数据
    def clear_data(self):
        for coordinate in self.stored_coordinate_num.keys():
            self.stored_coordinate_num[coordinate] = 0
        for i in range(1,10):
            for coordinate in self.stored_coordinate_num.keys():
                self.possible_element['now'] = 0
                self.possible_element[i][coordinate] = 'true'


    def print_block(self):
        print(self.possible_element)
        print(self.stored_coordinate_num)

    def find_a_block(self,start,ele):
        ls = ['false',0,0]
        #感觉好麻烦，这里也是一个需要保存的堆栈：
        #必须将现在搜索到的元素的下标记录起来
        #更新




