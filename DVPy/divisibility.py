for i in range(1,101):
    print(i," : ",end="")
    for j in range(2 , i):
        if(i%j==0):
            print(j,end=", ")
    print()