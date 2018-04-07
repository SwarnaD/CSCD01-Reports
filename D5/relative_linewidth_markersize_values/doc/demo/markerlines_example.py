import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.array([1,1])
y = np.array([0,9])

ax.plot(x, y, marker='o', markersize='xx-large', linewidth='thin')
ax.set_title('Large marker with a thin line')


plt.show()