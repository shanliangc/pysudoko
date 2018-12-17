import sudoko.FastSudoko
import time
import codecs
import sudoko.SudoTable

start = time.time()
sudoko_generator = sudoko.FastSudoko.FastSudokoGenerator(1)
sudoko_generator.create_puzzle()
end = time.time()
file_path = "sudoko.txt"
sudoko_generator.write_to_file(file_path)
print(end-start,"s")




