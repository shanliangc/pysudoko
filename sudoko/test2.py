import sudoko.test1
class student_table:
    student_information = []
    def __init__(self):
        for i in range(0,20):
            tmp_information = sudoko.test1.information("chen",i)
            self.student_information.append(tmp_information)
    def print_table(self):
        for ele in self.student_information:
            ele.print_information()

s = student_table()
s.print_table()
