class Complex:
    def __init__(self,realp=0,imagp=0):
        self.realp=realp
        self.imagp=imagp
    def readComplex(self):
        self.realp=int(input("Enter real part\n"))
        self.imagp=int(input("Enter imaginary part\n"))
    def showComplex(self):
        print("(",self.realp,")+i(",self.imagp,")",sep="")
    def addComplex(self,c2):
        c3=Complex()
        c3.realp=self.realp+c2.realp
        c3.imagp=self.imagp+c2.imagp
        return c3
    def __str__(self):
        return "("+str(self.realp)+")+i("+str(self.imagp)+")"
def add2Complex(a,b):
    c=a.addComplex(b)
    return c
def main():
    c1=Complex(3,5)
    c2=Complex(6,4)
    print("complex number 1")
    c1.showComplex()
    print("complex number 2")
    c2.showComplex()
    c3=add2Complex(c1,c2)   
    print("Sum of two complexes is ")
    c3.showComplex()
compList=[]
num=int(input("\nEnter the value for N\n"))
for i in range (num):
    print("Object",i+1)
    obj=Complex()
    obj.readComplex()
    compList.append(obj)
print("Entered complex numbers are ")
for obj in compList:
    print(obj)
sumObj=Complex()
for obj in compList:
    sumObj=add2Complex(sumObj,obj)
print("\nSum of n complex numbers is ",end="")
sumObj.showComplex()
main()