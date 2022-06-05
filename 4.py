nums = []
nc=[]
slic=[]
final = []
d=0
palin=0

for a in range(999,101,-1):
    for b in range(999,101,-1):
        nc.append(a*b)
        
for c in range(len(nums)):
    nc.append(max(nums))
    nums.remove(max(nums))

for e in range(len(nc)):
    test=nc[e]
    while test > 0 :
        slic.append(test%10)
        test=test//10
    for f in range((len(slic))):
        if slic[0+f]==slic[len(slic)-(f+1)]:
            palin+=1
            if palin >= 6:
                final.append(nc[e])
    palin=0
    slic=[]
print(max(final))

import time
time.sleep(5)

            
        
    
