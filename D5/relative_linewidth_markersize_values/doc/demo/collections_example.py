import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

N = 7
x= np.arange(N)
ys = [x + i for i in x]

fig,ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection([np.column_stack([x,y]) for y in ys], linewidths=('xx-thin', 'x-thin',
	'medium', 'thick', 'x-thick', 'xx-thick'))

line_segments.set_array(x)
ax.add_collection(line_segments)
plt.title('Collection of lines created with strings given as linewidth')

plt.show()