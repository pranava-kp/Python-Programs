def Bin2dec(bin):
    bin=bin[::-1]
    dec=0
    pow=0
    for i in bin:
        dec+=int(i)*2**pow
        pow=pow+1
    return dec

bin=input("Enter the Binary Number")
print("Binary to Decimal is ",Bin2dec(bin))


def oct2hex(oct):
    dec=0
    pow=0
    oct=oct[::-1]
    for i in oct:
        dec+=int(i)*8**pow
        pow+=1
    hex=['0',"1","2","3","4","5","6","7","8","9",'A','B','C','D','E','F']
    h=""
    while(dec>0):
        h=hex[dec%16]+h
        dec=dec//16
    return (h)
bin=input("Enter the Octal Number")
print("Octal to HexaDecimal is ",oct2hex(bin))