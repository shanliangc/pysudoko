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