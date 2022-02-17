#!/usr/bin/env python

#on x=10..12,y=10..12,z=10..12
#on x=11..13,y=11..13,z=11..13
#off x=9..11,y=9..11,z=9..11
#on x=10..10,y=10..10,z=10..10

x = [[10,12],[11,13],[9,11],[10,10]]
y = [[10,12],[11,13],[9,11],[10,10]]
z = [[10,12],[11,13],[9,11],[10,10]]
turn = [1,1,-1,1]

count = 0
a = []

for c in range(0,len(x)):
    for i in range(x[c][0],x[c][1]+1):
            for j in range(y[c][0], y[c][1]+1):
                    for k in range(z[c][0], z[c][1]+1):
                          temp = [i,j,k]
                          if temp not in a and turn[c] == 1:
                                  a.append(temp)
                                  count = count+ turn[c]
                          if turn[c] == -1 and temp in a:
                                  count = count+turn[c]
                                  a.remove(temp)
print(a)
print(count)
