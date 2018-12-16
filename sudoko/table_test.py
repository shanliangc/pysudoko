import sudoko.SudoTable
import time
tmp_table = sudoko.SudoTable.SudoTable(100)
n = 10
tmp_table.generate_sudoko_puzzle()
start = time.time()
for i in range(0,1000):
    print(i)
    tmp_table.generate_sudoko_puzzle()
    tmp_table.clean_data()
end = time.time()
print(end-start,"s")