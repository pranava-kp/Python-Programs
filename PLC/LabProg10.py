class Student:
    def __init__(self,name="",USn="",score=[0,0,0,0]):
        self.name=name
        self.USN=USn
        self.score=score
    def getmarks(self):
        self.name=input("Enter name\n")
        self.USN=input("Enter USN\n")
        self.score[0]=int(input("Enter marks 1 "))
        self.score[1]=int(input("Enter marks 2 "))
        self.score[2]=int(input("Enter marks 3 "))
        self.score[3]=self.score[0]+self.score[1]+self.score[2]
    def display(self):
        percentage=self.score[3]/3
        spstr="*"*80
        print(spstr)
        print("Score Card Details".center(80))
        print(spstr)
        print(self.name)
        print(self.USN)
        print(self.score[3])
        print(percentage)
        print(spstr)
def main():
    s1=Student()
    s1.getmarks()
    s1.display()
main()
