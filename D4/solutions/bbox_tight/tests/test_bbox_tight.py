import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.testing.decorators import image_comparison


@image_comparison(baseline_images=['simple_topLeft'],
                  extensions=['png'])
def test_simple_topLeft():
    
    # gather all the points and plot it
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    
    # create figure legend using bbox
    legend =  fig.legend(handles, labels,frameon=True, bbox_to_anchor=(0, 1))
    plt.show()


@image_comparison(baseline_images=['simple_topRight'],
                  extensions=['png'])
def test_simple_topRight():
    
    # gather all the points and plot it
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()

    # create figure legend using bbox
    legend =  fig.legend(handles, labels,frameon=True, bbox_to_anchor=(1, 1))
    plt.show()


@image_comparison(baseline_images=['simple_bottomRight'],
                  extensions=['png'])
def test_simple_bottomRight():
    # gather all the points and plot it
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()

    # create figure legend using bbox
    legend =  fig.legend(handles, labels,frameon=True, bbox_to_anchor=(1, 0))
    plt.show()

    

@image_comparison(baseline_images=['simple_bottomLeft'],
                  extensions=['png'])
def test_simple_bottomLeft():
    # gather all the points and plot it
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()

    # create figure legend using bbox
    legend =  fig.legend(handles, labels,frameon=True, bbox_to_anchor=(0, 0))
    plt.show()


@image_comparison(baseline_images=['simple_multipleColumns'],
                  extensions=['png'])    
def test_simple_multipleColumns():
    # gather all the points and plot it
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()

    # create figure legend using bbox
    legend =  fig.legend(handles, labels,ncol=2,frameon=True, bbox_to_anchor=(1, 1))
    plt.show()
    

@image_comparison(baseline_images=['simple_randomLocation'],
                  extensions=['png'])   
def test_simple_randomLocation():
    # gather all the points and plot it
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()

    # create figure legend using bbox
    legend =  fig.legend(handles, labels,ncol=2,frameon=True, bbox_to_anchor=(0.78, 0.52))
    plt.show()
    