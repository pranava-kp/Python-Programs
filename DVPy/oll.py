
l=[]
N = int(input())
for i in range(N):
    ele=input("enter elements")
    l.append(ele)
print(l)
l.sort()
print("sorted list:",l)
i=int(input("index"))
e=input()
l.insert(i,e)
l.remove(e)
print("updated",l)
deli=int(input("ietm to del"))
l.pop(deli)
print("updated",l)
l.reverse()
print("updated",l)