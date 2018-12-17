import sys
from sudoko import SudoTable
from sudoko import FastSudoko
import os
sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__))))
l = len(sys.argv)

if l != 3:
    print("check your input!")
if sys.argv[1] == '-c':
    try:
        res = int(sys.argv[2])
    except ValueError:
        print("check your num")
    else:
        if res < 1 or res > 1000000:
            print("res is out of our range")
            print("it must between 1 to 1000000")
        else:
            sudoko_generator = FastSudoko.FastSudokoGenerator(res)
            sudoko_generator.create_puzzle()
            file_path = "sudoko.txt"
            sudoko_generator.write_to_file()
elif sys.argv[1] == '-s':
    file_path = sys.argv[2]
    sudoko_puzzle = SudoTable.SudoTable(1)
    sudoko_puzzle.solve_a_puzzle()
    sudoko_puzzle.write_to_file(file_path)
    pass
else:
    print("check your input")

