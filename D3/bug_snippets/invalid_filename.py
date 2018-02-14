import numpy as np
import matplotlib.pyplot as plt

# a simple figure with one graph
fig = plt.figure()
ax = fig.add_subplot(111)

# plot a random function
x = np.arange(0.0, 15.0, 0.01)
y = np.sin(0.3*np.pi*x)
ax.plot(x, y, lw=2, label="sin(x)")

# change the window title to hold invalid characters for a file name in windows
fig.canvas.set_window_title("Invalid Window File Name Characters *./\[]:;|=,")

plt.grid()
plt.show()