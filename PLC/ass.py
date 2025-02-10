n=int(input("Enter the number of elements"))
A=[]
for i in range (n):
    print("Enter element ",i+1)
    val=int(input())
    A.append(val)
print("The list is ")
print(A)
Acopy=A
print("The list without ODD numbers is ")
for i in A:
    if(i%2!=0):
        Acopy.remove(i)
    else:
        continue

print(Acopy)