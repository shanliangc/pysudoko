import sudoko.SudoTable
import time
import codecs
start = time.time()
sudotable = sudoko.SudoTable.SudoTable(1)


file_path = "sudokopuzzle.txt"
table = []
file = codecs.open(file_path,'r','utf-8')
num = 0
print("sssssssss")
for line in file.readlines():
    if num == 9:
        break
    num += 1
    row = line.strip().split()
    ls = []
    for i in range(0,9):
        ls.append(int(row[i]))
    table.append(ls.copy())

sudotable.solve_a_puzzle(table)
end = time.time()
print(end-start,'s')