import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection="polar")
a=5
rad=np.arange(0,(2*np.pi),0.001)
for i in rad:
    r=np.sqrt((a*a)*np.cos(2*i))
    plt.polar(i,r,'r.')
    
plt.title("Graph of Lemmiscate")
plt.show()