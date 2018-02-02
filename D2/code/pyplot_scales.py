# This script emulates the pyplot_scales.py script
# included in the folder matplotlib/lib/mpl_examples
# from the Artist layer

from matplotlib.ticker import NullFormatter
import numpy as np

# Choose a FigureCanvas from any backend, attach figure to it
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# initialize FigureCanvas and attach it to the selected Figure()
fig = Figure()
canvas = FigureCanvas(fig)

#linear

# Call Figure() method to add subplot, creates Axes artist
ax1 = fig.add_subplot(221)
# Use Axes() artist method plot() to plot
ax1.plot(x, y)
ax1.set_yscale('linear')
ax1.set_title('linear')
ax1.grid(True)

#log
# same as above
ax2 = fig.add_subplot(222)
ax2.plot(x, y)
ax2.set_yscale('log')
ax2.set_title('log')
ax2.grid(True)


#symmetric log
ax3 = fig.add_subplot(223)
ax3.plot(x, y - y.mean())
ax3.set_yscale('symlog', linthreshy=0.01)
ax3.set_title('symlog')
ax3.grid(True)

#logit
ax4 = fig.add_subplot(224)
ax4.plot(x, y)
ax4.set_yscale('logit')
ax4.set_title('logit')
ax4.grid(True)
ax4.yaxis.set_minor_formatter(NullFormatter())

fig.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

# Set titles and save
fig.savefig('pyplot_scales.png')
