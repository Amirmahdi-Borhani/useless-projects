
sum1=0
sum2=0
for i in range(1,100+1):
    sum1 = sum1+i**2
for i in range(1,100+1):
    sum2 = sum2+i
sum2=sum2**2
print(sum2-sum1)

import time
time.sleep(5)

