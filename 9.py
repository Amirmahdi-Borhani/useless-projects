q=0
for a in range(1,1000):
    for b in range(1,1000):
        c2=(a**2)+(b**2)
        if a+b+(c2**0.5) == 1000 and q==0:
            print(int((a)*(b)*(c2**0.5)))
            q=q+1
            
import time
time.sleep(5)

            
            


