"""
Illustrate simple contour plotting with different coordinate systems and
automatically placing the contour given one coordinate and an nth-intersection.
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.01
x = np.arange(-4.0, 4.0, delta)
y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = 10.0 * (Z2 - Z1)

# contour labels are set manually based off the data coordinate system
# this is the default behaviour
plt.figure()
CS = plt.contour(X, Y, Z)
manual_locations = [(-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), 
                    (2.0, 1.4), (2.4, 1.7)]
plt.clabel(CS, inline=1, fontsize=8, manual=manual_locations)
plt.title("Labels at Selected Locations (Data Coordinate System)")

# contour labels are set manually based off the axes coordinate system
# transform param used to change coordinate systems
plt.figure()
CS = plt.contour(X, Y, Z)
ax = plt.gca()
manual_locations = [(0.4, 0.3), (0.47, 0.45), (0.2, 0.55), (0.7, 0.7), 
                    (0.72, 0.72), (0.8, 0.8)]
plt.clabel(CS, inline=1, fontsize=8, manual=manual_locations, 
           transform=ax.transAxes)
plt.title('Labels at Selected Locations (Axes Coordinate System)')


# contour labels are placed automatically given a x/y coordinate
# the other coordinate is the nth-intersection where the label will be placed
# 0 based index
plt.figure()
CS = plt.contour(X, Y, Z)
manual_locations = [(-1, [0]), ([2], 0), (0, [2]), (2, [0]), ([0], 1)]
plt.clabel(CS, inline=1, fontsize=8, manual=manual_locations)
plt.title("Labels With Positional Arguments")


plt.show()
