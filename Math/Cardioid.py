import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection="polar")
a=5
rad=np.arange(0,(2*np.pi),0.01)
for i in rad:
    r=a-(a*np.cos(i))
    plt.polar(i,r,'r.')
    s=a+(a*np.cos(i))
    plt.polar(i,s,'b.')
plt.title("Graph of Cardioid")
plt.show()    