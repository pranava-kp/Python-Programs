n=int(input())
dec=[]
for i in range(n):
    l=int(input())
    dec.append(l)
sorted(dec)
a=[]
asc=dec[::-1]
i=0
j=0
while(i<n):
    while(j<n):
        if(asc[i]+dec[j]==200):
            a.append((i,j))
            asc.pop(i)
            dec.pop(j)
            asc.pop(n-j)
            
            
print(len(a))