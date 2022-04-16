#figure as object

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,10)
y = x**2+1

fig_1 = plt.figure(figsize=(5,4), dpi=100)

axes_1 = fig_1.add_axes([.1,.1,.9,.9])

axes_1.plot(x,y,label='simple display')
axes_1.set_xlabel('arg [ ]')
axes_1.set_ylabel('val')

fig_1.show()
fig_1.savefig('example.png')
