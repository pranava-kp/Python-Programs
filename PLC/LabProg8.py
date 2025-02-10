def DivExp(a,b):
    assert a>0, "A cannot be less than 1"
    try:
        c=a/b
    except ZeroDivisionError:
        print("Value of b cannot be 0")
    else:
        return c
val1=int(input())
val2=int(input())
val3=DivExp(val1,val2)
print(val3)