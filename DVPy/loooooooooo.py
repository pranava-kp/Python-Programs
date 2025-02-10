import matplotlib.pyplot as plt
import random
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [40, 75, 22, 33]
hex=['0',"1","2","3","4","5","6","7","8","9",'A','B','C','D','E','F']
clr=[]
for i in range(len(values)):
    s=""
    for i in range(6):
        s=s+random.choice(hex)
    s="#"+s
    clr.append(s)
plt.pie(values, labels=categories,colors=clr,autopct="%0.2f%%")