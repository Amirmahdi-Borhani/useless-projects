
def makeprime (y):
    global primelist
    q=0
    x = 1
    while (x-1)<(y**0.5) :
        if y%x == 0 :
            q=q+1
        x=x+1
    if q<=1 :
        primelist.append(y)
        
primelist = [2]

for i in range(3,100001,2):
    makeprime(i)

primelist2 = []

inp = 600851475143

for i in primelist[ : :-1] :
    if inp%i ==0:
        #primelist2.append(i)
        print(i)
        break

import time
time.sleep(5)







        
