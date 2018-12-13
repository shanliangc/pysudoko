import sudoko.test1
class student_table:
    name = 0
    student_information = []
    def __init__(self,i):
        self.mytable = []
        for i in range(20):
            self.student_information.append([])
            self.mytable.append([])
        self.name = str(i)
    def print_table(self):
        print("name "+ str(self.name) + " " + str(len(self.student_information)))
        print("name "+ str(self.name) + " " + str(len(self.mytable)))


for i in range(20):
    #难道没创建新的东西吗？
    a = student_table(i)
    print(a)
    a.print_table()

#在python的学习中发现了一新的，曾经没有注意过的内容：
#python中的类没有java中的前缀static等，只要写在class里面的，都为static
#而在函数中使用的self.变量名 才是真正的每个python类的实例化拥有的私有变量