count=0
day=0
for a in range(1901,2001):
    daycount=0
    yearday=365
    days=['sat','sun','mon','tue','wen','thu','fri']
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    today2=0
    month=0
    if (a%100==0 and a%400==0)or(a%100!=0 and a%4==0) :
         months[1]=29
         yearday=366
    for _ in range(1,yearday+1) :
        day+=1
        daycount+=1
        if daycount>months[month]:
            daycount-=months[month]
            month+=1
            today2=0
        today2+=1
        today1=days[day%7]
        if today2==1 and today1=='sun' :
            print(a,'/',month+1,'/',today2,' : ',today1)
            count+=1
print()
print()
print(count)
