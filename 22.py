file=open('p022_names.txt','r')
text=file.read()
names=[]

str=''
for i in text:
    if i=='"':
        if len(str)>1 :
            names.append(str)
        str=''
    else:
        str+=i

names.sort()

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sum=0

for i in names :
    worth=0
    for j in i:
        worth=worth+alpha.index(j)+1
    sum+=worth*(names.index(i)+1)
print(sum)
    
