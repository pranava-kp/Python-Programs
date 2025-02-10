import os.path,sys
fname=input("Enter file name")
if not os.path.isfile(fname):
    print("Invalid")
    sys.exit(0)
infile=open(fname,"r")
mylist=infile.readlines()
print(mylist)
linelist=[]
for line in mylist:
    linelist.append(line.strip("\n"))
linelist.sort()
outfile=open("sorted.txt","w")
for line in linelist:
    outfile.write(line+"\n")
infile.close()
outfile.close()
if os.path.isfile("sorted.txt"):
    print("File exists")
    print("Contents are ")
    rdfile=open("sorted.txt","r")
    for line in rdfile:
        print(line)