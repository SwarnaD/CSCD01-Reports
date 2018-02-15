import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

x = np.arange(-10, 10, 0.5)
y1 = np.tan(x)
y2 = np.sin(x)

fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))

ax1.plot(x, y1, label='tan')
ax1.plot(x, y2, label='sin')

handles, labels = ax1.get_legend_handles_labels()
# following code does not work
legend = fig.legend(handles, labels, bbox_to_anchor=(1, 1))
plt.savefig('test.png', bbox_extra_artists=[legend], bbox_inches='tight')
#plt.show()




