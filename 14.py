a=[]
chain = 1
Max=chain

for test in range(1,1000001):

    test2=test
    
    while test2 != 1 :
        if test2%2 ==0:
            test2=test2/2
            chain+=1
        elif test2%2 != 0:
            test2 = (test2*3)+1
            chain+=1

    if chain>=Max:
        Max=chain
        a.append(test)
        
    chain = 1
print(a[-1])

import time
time.sleep(5)

        


    
            
        
        
