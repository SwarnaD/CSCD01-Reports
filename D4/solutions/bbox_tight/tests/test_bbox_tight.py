import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

def test_simple_topLeft():
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    # following code does not work
    legend = fig.legend(handles, labels, frameon=True, bbox_to_anchor=(0, 1))
    plt.savefig('test_topLeft.png', bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show()
    
def test_simple_topRight():
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    # following code does not work
    legend = fig.legend(handles, labels, frameon=True, bbox_to_anchor=(1, 1))
    plt.savefig('test_topRight.png', bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show()

def test_simple_bottomRight():
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    # following code does not work
    legend = fig.legend(handles, labels, frameon=True, bbox_to_anchor=(1, 0))
    plt.savefig('test_bottomRight.png', bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show()

def test_simple_bottomLeft():
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    # following code does not work
    legend = fig.legend(handles, labels, frameon=True, bbox_to_anchor=(0, 0))
    plt.savefig('test_bottomLeft.png', bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show()
    
def test_simple_multipleColumns():
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    # following code does not work
    legend = fig.legend(handles, labels,ncol=2, frameon=True, bbox_to_anchor=(1, 1))
    plt.savefig('test_topLeft.png', bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show()
    
    
def test_simple_randomLocation():
    x = np.arange(-10, 10, 0.5)
    y1 = np.tan(x)
    y2 = np.sin(x)
    
    fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
    
    ax1.plot(x, y1, label='tan')
    ax1.plot(x, y2, label='sin')
    
    handles, labels = ax1.get_legend_handles_labels()
    rand1 = random.uniform(0,1)
    rand2 = random.uniform(0,1)    
    # following code does not work
    legend = fig.legend(handles, labels,ncol=2, frameon=True, bbox_to_anchor=(rand1, rand2))
    plt.savefig('test_randomLocation.png', bbox_extra_artists=(legend,), bbox_inches='tight')
    #plt.show()     
    
    
    

if __name__== "__main__":
    test_simple_topLeft()
    test_simple_topRight()
    test_simple_bottomRight()
    test_simple_bottomLeft()
    test_simple_multipleColumns()
    test_simple_randomLocation()
    