import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x= np.linspace(-10,10,100)

#graph of row 1, column 1: sin(x)
plt.subplot(2,2,1)
plt.plot(x, np.sin(x),'c')
plt.title('sis(x)')
plt.xlabel("sin(x)")
plt.ylabel("X")
plt.tick_params(labelsize=9)

#graph of row 1, column 2: cos(x)
plt.subplot(2,2,2)
plt.plot(x, np.cos(x),'m')
plt.title('cos(x)')
plt.xlabel("cos(x)")
plt.ylabel("X")
plt.tick_params(labelsize=9)

#graph of row 2, column 1: tan(x)
plt.subplot(2,2,3)
plt.plot(x, np.tan(x),'c')
plt.title('tan(x)')
plt.xlabel("tan(x)")
plt.ylabel("X")
plt.tick_params(labelsize=9)

plt.tight_layout()#from pandas, so that all the plots do not overlap
plt.show()
