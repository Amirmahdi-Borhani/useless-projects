Sum = 2
y=0

for y in range(3,(2000000+1),2):
    q=0
    x = 1
    while (x-1)<(y**0.5) :
        if y%x == 0 :
            q=q+1
        x=x+1
    if q<=1 :
        Sum=Sum+y
        

print(Sum)

import time
time.sleep(5)
