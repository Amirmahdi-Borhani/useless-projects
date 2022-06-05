primelist = [2]
i=3
h=1

def makeprime (y):
    global primelist
    global h
    q=0
    x = 1
    while (x-1)<(y**0.5) :
        if y%x == 0 :
            q=q+1
        x=x+1
    if q<=1 :
        primelist.append(y)
        h+=1
        
while h!=10001:
    makeprime(i)
    i+=2
print(primelist[10000])

import time
time.sleep(5)
    
    
