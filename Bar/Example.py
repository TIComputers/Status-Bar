from Main import Bar
from time import sleep, time
bar1 = Bar()





max = 10000
x = 1

bar1.get_time()
while x < max:
    bar1.status(process=max, processd=x)
    x += 1
    


bar2 = Bar()

max = 5
x = 1

bar2.get_time()
while x < max:
    bar2.status(process=max, processd=x, text="outerloop")
    max1 = 10000
    y = 0
    bar2.get_time()
    while y < max1:
        bar2.status(process=max1, processd=y, text=f"inerloop[{x}]")
        y += 1
    x += 1
   