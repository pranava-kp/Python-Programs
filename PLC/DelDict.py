n=int(input("Enter the number of elements\n"))
A={}
for i in range (n):
    key=input("Enter key\n")
    value=input("Enter value\n")
    A[key]=value

print("The dictionary is ",A)
dele=input("Enter key of the value to be deleted\n")
if dele in A:
    print("The key ",dele," has been deleted")
    del A[dele]
    
else:
    print("The key does not exist")
print("Updated dictionary is \n",A)