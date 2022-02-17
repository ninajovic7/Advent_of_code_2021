###Dirac dice

i = 1
counter = 0
p1 = 4
p2 = 8
s1 = 0
s2 = 0
n = True

j = 0
turn = 3
while n:
    count1 = i + (i +1) + (i +2)
    i = i+3
    count2 = i + (i +1) + (i +2)
    i = i+3
    #count1 = 0
    #for j in range(j+1,turn+j+1):
    #    count1 += j
    
    temp1 = (p1+count1)%10 
    temp2 = (p2+count2)%10 
    
    if (p1+count1)%10 == 0:
        temp1 = 10
    if (p2+count2)%10 ==0:
        temp2 = 10

    s1 = s1 + temp1 
    counter = counter+1
    if s1 >=1000:
        print(3*counter*s2)
        n = False
        break      

    s2 = s2 + temp2
    counter = counter+1
    if s2 >=1000:
        print(3*counter*s1)
        n = False
        break

    p1 = temp1 
    p2 = temp2 
#    print(count1, p1,s1)
#    print(count2, p2,s2)
print(3*counter,s1,s2, 3*counter*s2)
