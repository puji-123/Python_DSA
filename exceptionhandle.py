"""x=int(input())
y=int(input())
#print(x/y)
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("done")
for i in range(5):
    
    if i==4:
        
        print(i)
else:
    print("done")
try:
    a=int(input())
    print(a)
except ValueError as e:
    print(e)
else:
    print("done")
a=int(input())
if a<0:
    raise ValueError(":number is negative")
else:
    print(a)  
l=[1,2,4,5]


try:
    print(l[5])
except IndexError as e:
    print(e)
finally:
    print("done") 
while True:
    try:
        a=int(input())
        print(a)
        break
    except ValueError as e:
        print(e) """         

   
