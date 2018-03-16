import pytest
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, SymLogNorm

@image_comparison(baseline_images=['simple_log_cbar'],
                  extensions=['png'])
def test_log_minor_ticks_visible():
    # test the undesired minor ticks do not appear if minor
    # ticks visibility is set to True
    data = [[0.1, 0.3],
            [0.6, 1]]
    plt.rcParams['xtick.minor.visible'] = True    
    plt.rcParams['ytick.minor.visible'] = True
    plt.pcolormesh(data, norm=LogNorm())
    plt.colorbar()

@image_comparison(baseline_images=['simple_log_cbar_horizontal'],
                  extensions=['png'])
def test_log_horizontal_colorbar():
    # test the undesired minor ticks do not appear if minor
    # ticks visibility is set to True and the Colorbar is set
    # to horizontal
    data = [[0.1, 0.3],
            [0.6, 1]]
    plt.rcParams['xtick.minor.visible'] = True    
    plt.rcParams['ytick.minor.visible'] = True
    plt.pcolormesh(data, norm=LogNorm())
    plt.colorbar(orientation="horizontal")

@image_comparison(baseline_images=['dense_log_cbar'],
                  extensions=['png'])
def test_log_dense_pcolormesh():
    # test the undesired minor ticks do not appear if minor
    # ticks visibility is set to True for a Colorbar with a
    # lot of linear ticks
    data = [[0.0001, 0.005],
            [0.01, 1]]
    plt.rcParams['xtick.minor.visible'] = True    
    plt.rcParams['ytick.minor.visible'] = True
    plt.pcolormesh(data, norm=LogNorm())
    plt.colorbar()

@image_comparison(baseline_images=['dense_log_cbar_symlognorm'],
                  extensions=['png'])
def test_log_symlognorm_cbar():
    # test the undesired minor ticks do not appear if minor
    # ticks visibility is set to True for a pcolormesh with
    # a SymLogNorm
    data = [[0.0001, 0.005],
            [0.01, 1]]
    plt.rcParams['xtick.minor.visible'] = True    
    plt.rcParams['ytick.minor.visible'] = True
    plt.pcolormesh(data, norm=SymLogNorm(0.01))
    plt.colorbar()    
