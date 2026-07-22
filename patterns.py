
"""for i in range(n):
    for j in range(n):
        print("*",end=" " )
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
#fist how many rows
#how many spaces
#how many stars
n=153
temp=n
d=len(str(n))

sum=0
c=0
while n>0:
    digit=n%10
    sum=sum+digit**d
    n=n//10
if temp==sum:
    print("armstong")
else:
    print("not")
#hollow square pattern
n=5
for i in range(n):
    
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            
            print(" ",end=" ")
    print()"""
#pascals patten
n=int(input())
for i in range(n):
    num=1
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(num,end=" ")
        
        