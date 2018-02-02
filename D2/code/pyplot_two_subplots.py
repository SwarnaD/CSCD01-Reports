# This script emulates the pyplot_two_subplots.py script
# included in the folder matplotlib/lib/mpl_examples
# from the Artist layer

import numpy as np

# Choose a FigureCanvas from any backend, attach figure to it
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas
from matplotlib.figure import Figure

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


# initialize FigureCanvas and attach it to the selected Figure()
fig = Figure()
canvas = FigureCanvas(fig)


# Call Figure method to add subplot, creates Axes
ax1 = fig.add_subplot(121)

# Use Axes method plot() to plot
ax1.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# repeat for second subplot
ax2 = fig.add_subplot(122)
ax2.plot(t2, np.cos(2*np.pi*t2), 'r--')

# save
fig.savefig('pyplot_two_subplots.pdf')
