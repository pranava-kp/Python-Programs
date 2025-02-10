import os.path,sys,string
fname=input("Enter file path")
if not os.path.isfile(fname):
    print("Invalid")
    sys.exit(0)
infile=open(fname,"r")
filecontent=""
for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            filecontent+=ch
        else:
            filecontent+=" "
wordfreq={}
wordlist=filecontent.split()
for i in wordlist:
    if i not in wordfreq:
        wordfreq[i]=1
    else:
        wordfreq[i]+=1
sortedwordfreq=sorted(wordfreq.items(),key=lambda x:x[1],reverse=True)
leng=len(sortedwordfreq)
if(leng>10):
    leng=10
for i in range(leng):
    print(sortedwordfreq[i][0],"occurs",sortedwordfreq[i][1],"times")