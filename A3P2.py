import random

A=[]

n=int(input("enter n: "))
B=random.randint(0,100)

while True:
    if B in A :
        B=random.randint(0,5) 
    else:
        A.append(B)
    if len(A)>n:
        break

print(A)