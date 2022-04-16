import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_1 = np.linspace(0,5,10)
y_1 = x_1**2

plt.subplot(1,2,1)

plt.plot(x_1, y_1)

plt.title('some title')
plt.xlabel('argument')
plt.ylabel('value')


plt.subplot(1,2,2)
plt.plot(x_1,y_1,'ro')

plt.show()
