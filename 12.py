fac = 1
i=2
while fac<500+1:
    y=((i+1)*i)/2
    q=0
    x = 1
    while (x-1)<int(y**0.5) :
        if y%x == 0 :
            q=q+2
        x=x+1
    fac = q
    i+=1
print(int(y))

import time
time.sleep(5)

