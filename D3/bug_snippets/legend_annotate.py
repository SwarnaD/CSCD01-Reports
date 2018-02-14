import numpy as np
import matplotlib.pyplot as plt

# create a range of numbers as the x axis and the function for the y axis
x = np.arange(0.0, 15.0, 0.01)
y = np.sin(0.3*np.pi*x)

# create a new figure with only one graph
fig = plt.figure()
ax = fig.add_subplot(111)

# plot the function
ax.plot(x, y, lw=2, label="sin(x)")

# create annotations to indicate a wave's length and amplitude
# notice the label param to indicate name in legend
ax.annotate("",
            xy=(1.6, 1.03), 
            xytext=(8.4, 1.03), 
            arrowprops={'arrowstyle':'<->'}, 
            label="wavelength")
ax.annotate("",
            xy=(8.4, 0), 
            xytext=(8.35, 1.0), 
            arrowprops={'arrowstyle':'<->', 'ls':'dashed'}, 
            label="amplitude")

# set the bounds and show the legend
ax.set_ylim(-1.5, 1.5)
ax.legend()

plt.grid()
plt.show()
