n=input("Enter a number : ")
uniqdig=set(n)
for i in uniqdig:
    print(i,"occurs",n.count(i),"times")

