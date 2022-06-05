def kemimmim ( mylist ):
    guess = 1
    q=1
    z=False

    while z==False :
        guess+=1
        for i in range(len(mylist)):
            if guess%mylist[i]!= 0 :
                z=False
                break
            else:
                z=True
    return guess

nums = range(1,17)
print(kemimmim(nums)*(17*19))


import time
time.sleep(5)



