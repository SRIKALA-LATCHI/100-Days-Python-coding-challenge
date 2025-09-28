# moving zero elements to the end of the array.
n=int(input())
j=0
l=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        l[j]=a
        j+=1
for i in l:
    print(i,end=" ")
    
"""Input:
6
10
20
30
0
0
8
output :
10 20 30 8 0 0"""
