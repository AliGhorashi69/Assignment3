
n=int(input("Please insert the size of the list: "))
l=[]

for i in range(n):
     e=int(input("enter the element:"))
     l.append(e)
     print(l)




if l==l.sort():
    print("the list is sorted")
else:
    print("the list was not sorted and the sorted list is: ", l)

