def divsum(n):
    sum=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sum+=i
            sum+=n/i
    if (n**0.5)%1==0:
        sum-=n**0.5
    return int(sum)

Sum=0
for a in range(2,10001):
    b=divsum(a)
    if divsum(b)==a :
        if a!=b:
            Sum+=a
            print('(',a,',',b,')')
print()
print(Sum)
