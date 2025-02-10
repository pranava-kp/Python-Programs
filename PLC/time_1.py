class Time:
    def __init__(self,h=0,m=0,s=0):
        self.hour=h
        self.minute=m
        self.second=s
    def __add__(self,t1):
        r=Time()
        r.hour=t1.hour+self.hour
        r.minute=t1.minute+self.minute
        r.second=t1.second+self.second
        r.fix()
        return r
    def __str__(self):
        v=str(self.hour)+":"+str(self.minute)+":"+str(self.second)
        return v
    def fix(self):
        while(self.second>=60):
            self.second-=60
            self.minute+=1
        while(self.minute>=60):
            self.minute-=60
            self.hour+=1

def add2times(t1,t2):
    final=t1+t2
    return final
t=[]
ans=Time()
n=int(input("Enter number of elements"))
for i in range(n):
    print("Enter h",i+1)
    v1=int(input())
    print("Enter m",i+1)
    v2=int(input())
    print("Enter m",i+1)
    v3=int(input())
    tm=Time(v1,v2,v3)
    t.append(tm)
for i in t:
    ans=add2times(ans,i)
print(ans)