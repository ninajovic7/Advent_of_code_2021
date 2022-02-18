i = 1
counter = 0
pl = [4,8]
s =[0,0]
n = True
j = 0
turn = 3

while n:
    for k in range(len(pl)):
        count1 = 0
        for j in range(j+1,turn+j+1):
                count1 += j
                counter = counter+1
        
        temp1 = (pl[k]+count1)%10 
        if (pl[k]+count1)%10 == 0:
                temp1 = 10
        s[k] = s[k] + temp1 
        if s[k] >=1000:
                print(counter,s.pop(k),counter*s[0])
                n = False
                break      
        pl[k] = temp1

