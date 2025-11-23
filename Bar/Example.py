from Main import Bar
from time import sleep, time
bar = Bar()


max = 100000
bar.get_time()
for i in range(max):
    z = 12357 * 1357 / 1373
    bar.get_process_processed(max, i, text=f"for loop range {max}")
    

print("\n\n")
 
max = 1000
bar.get_time()
for j in range(max):
    sleep(0.001)
    z = 12357 * 1357 / 1373
    bar.get_process_processed(max, j, text=f"for loop {max}, with function sleep")
    
print("\n\n")

for x in range(1,5):
    max = 100000 * x
    bar.get_time()
    for y in range(max):
        bar.get_process_processed(max, y, f"nestes loop[{x}]", False)
    print("\n")
