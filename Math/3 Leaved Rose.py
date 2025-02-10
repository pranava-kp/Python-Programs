import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection="polar")
a=5
rad=np.arange(0,(2*np.pi),0.01)
for i in rad:
    r=a*np.sin(3*i)
    plt.polar(i,r,'r.')
plt.title("Graph of 3 Leaved Rose")
plt.show()    

    