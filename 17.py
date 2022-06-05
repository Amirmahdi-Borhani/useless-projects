
def letters(inp):
    nums1 = ["",'one','two','three','four','five','six','seven','eight','nine','ten','eleven','telve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    nums2=["","",'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    nums3=["",'one','two','three','four','five','six','seven','eight','nine']
    letter=""
    inp2 = inp
    if (inp2//10)%10 <=1 and inp2//100 == 0 :
        letter = str(nums1[(inp2)])
    elif (inp2//10)%10 <=1 and inp2//100 != 0 :
        letter = str(nums3[(inp2//100)])+"hundred"+"and"+nums1[inp2%100]
    elif (inp2//10)%10 >1 and inp2//100 == 0 :
        letter = str(nums2[(inp2//10)%10])+str(nums1[inp%10])
    else:
        letter = str(nums3[inp2//100])+"hundred"+"and"+str(nums2[(inp2//10)%10])+str(nums1[inp%10])

    return(letter)

Sum=0
for i in range (1,1000):
    Sum+=len(letters(i))
Sum+=len("ziro")
print(Sum)


    
    
    
    
    
