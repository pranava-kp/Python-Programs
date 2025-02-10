import os.path,string,sys
n=input("Enter file path")
n=r"C:\Users\prana\OneDrive\Desktop\py.txt.txt"
if not os.path.isfile(n):
    print("Invalid")
    sys.exit(0)
else:
    print("Yes")
infile=open(n,"r")
filecontents=""
for i in infile:
    for ch in i:
        if ch not in string.punctuation:
            filecontents+=ch
        else:
            filecontents+= " "
wordlist=filecontents.split()
wordfreq={}
for i in wordlist:
    wordfreq.setdefault(i,0)
    wordfreq[i]+=1
sortedwordfreq=sorted(wordfreq.items(),key=lambda x:x[1],reverse=True)
for i in range(10):
    print(sortedwordfreq[i][0],"occurs",sortedwordfreq[i][1],"times")