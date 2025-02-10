import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,1000)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,'r.')
plt.plot(x,z,'b.')
plt.title("Graph of Sine and Cosine")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()