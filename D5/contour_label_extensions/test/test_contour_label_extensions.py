import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from matplotlib.testing.decorators import image_comparison

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 2.1, 1.2, 0.3, 0.4)
Z2 = mlab.bivariate_normal(X, Y, 1.8, 0.6, 1.1, 1.1)
# difference of Gaussians
Z = 12 * (Z2 - Z1)


@image_comparison(baseline_images=['test_clabel_transform_data'],
                  extensions=['png'])
def test_clabel_transform_data():
    # test that contour labels are placed using the data coordinate system
    plt.figure()
    ax = plt.gca()
    CS = plt.contour(X, Y, Z)
    manual_locations = [(-1, -1.4), (-0.62, -0.7), (1, 1)]
    plt.clabel(CS, inline=1, fontsize=10, manual=manual_locations, 
               transform=ax.transData)
    plt.title('data coordinate system')
    plt.show()
  

@image_comparison(baseline_images=['test_clabel_transform_axes'],
                  extensions=['png'])
def test_clabel_transform_axes():
    # test that the contour labels are placed using the axes coordinate system
    plt.figure()
    ax = plt.gca()
    CS = plt.contour(X, Y, Z)
    manual_locations = [(0.5, 0.5), (0.8, 0.8), (0.1, 0.1)]
    plt.clabel(CS, inline=1, fontsize=10, manual=manual_locations, 
               transform=ax.transAxes)
    plt.title('axes coordinate system')
    plt.show()
    

@image_comparison(baseline_images=['test_clabel_transform_figure'],
                  extensions=['png'])
def test_clabel_transform_figure():
    # test that the contour labels are placed using the figure coordinate system
    fig = plt.figure()
    CS = plt.contour(X, Y, Z)
    manual_locations = [(0, 0), (1, 1), (0.5, 0.5)]
    plt.clabel(CS, inline=1, fontsize=10, manual=manual_locations, 
               transform=fig.transFigure)
    plt.title('figure coordinate system')
    plt.show()


@image_comparison(baseline_images=['test_clabel_positional_coordinate'],
                  extensions=['png'])
def test_clabel_positional_coordinate():
    # test that the contour labels are placed using positional coordinates
    plt.figure()
    CS = plt.contour(X, Y, Z)
    manual_locations = [(0, [0]), (-2, [-2]), (2, [4])]
    plt.clabel(CS, inline=1, fontsize=10, manual=manual_locations)
    plt.title('positional coordinates')
    plt.show()   
