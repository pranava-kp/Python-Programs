import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,1000)
y=np.exp(x)
plt.plot(x,y,'r.')
plt.title("Graph of exponent")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()