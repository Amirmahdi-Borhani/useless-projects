
n1 = 1
n2 = 2
n3 = n1+n2
count = 2

while n3 < 4000000 :
    count+=n3
    n1=n2+n3
    n2=n3+n1
    n3=n1+n2
print(4*count)
