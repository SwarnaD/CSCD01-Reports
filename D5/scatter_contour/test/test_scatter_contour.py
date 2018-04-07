import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import matplotlib.mlab as mlab



def test_all_defaults():

    x = [0.5,1, 1.8, 0.3, -1, -1]
    y = [1,1.3, -1.2, 0.3, -1, -3]
    z = [0.4, -0.3, 1.2, 0.7, 2, 1]
    
    plt.scatter_contour([x,y,z], [-3, 2], [-3,2])
    
    #plt.tricontour(x, y, z, 100, linewidths=0, colors='k')
    #plt.tricontourf(x, y, z, 100, norm=plt.Normalize(vmax=abs(zi).max(), vmin=-abs(zi).max()))
    plt.colorbar(ticks=[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    plt.plot(x, y, 'ko', ms=3)
    plt.xlim(-3, 2)
    plt.ylim(-3, 2)
    plt.title('Tricontour from data points')
    
    
    plt.savefig('test_all_deafults')
    

def test_colour_density():

    x = [0.5,1, 1.8, 0.3, -1, -1]
    y = [1,1.3, -1.2, 0.3, -1, -3]
    z = [0.4, -0.3, 1.2, 0.7, 2, 1]
    
    plt.scatter_contour([x,y,z], [-3, 2], [-3,2], 10)
    
    #plt.colorbar(ticks=[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    plt.plot(x, y, 'ko', ms=3)
    plt.xlim(-3, 2)
    plt.ylim(-3, 2)
    plt.title('Tricontour from data points')
    
    
    plt.savefig('test_colour_density')
    

def test_edge_max():

    x = [0.5,1, 1.8, 0.3, -1, -1]
    y = [1,1.3, -1.2, 0.3, -1, -3]
    z = [0.4, -0.3, 1.2, 0.7, 2, 1]
    
    plt.scatter_contour([x,y,z], [-3, 2], [-3,2], 10, "MAX")
    
    #plt.colorbar(ticks=[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    plt.plot(x, y, 'ko', ms=3)
    plt.xlim(-3, 2)
    plt.ylim(-3, 2)
    plt.title('Tricontour from data points')
    
    
    plt.savefig('test_edge_max')

def test_inputted_edge():

    x = [0.5,1, 1.8, 0.3, -1, -1]
    y = [1,1.3, -1.2, 0.3, -1, -3]
    z = [0.4, -0.3, 1.2, 0.7, 2, 1]
    
    plt.scatter_contour([x,y,z], [-3, 2], [-3,2], 10, 1000)
    
    #plt.colorbar(ticks=[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    plt.plot(x, y, 'ko', ms=3)
    plt.xlim(-3, 2)
    plt.ylim(-3, 2)
    plt.title('Tricontour from data points')
    
    
    plt.savefig('test_inputted_edge')
    

def test_circular():

    x = [0.5,1, 1.8, 0.3, -1, -1]
    y = [1,1.3, -1.2, 0.3, -1, -3]
    z = [0.4, -0.3, 1.2, 0.7, 2, 1]
    
    plt.scatter_contour([x,y,z], [-3, 2], [-3,2], 150, "MIN", False)
    
    #plt.colorbar(ticks=[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    plt.plot(x, y, 'ko', ms=3)
    plt.xlim(-3, 2)
    plt.ylim(-3, 2)
    plt.title('Tricontour from data points')
    
    
    plt.savefig('test_circular')
    
def test_triangular():

    x = [0.5,1, 1.8, 0.3, -1, -1]
    y = [1,1.3, -1.2, 0.3, -1, -3]
    z = [0.4, -0.3, 1.2, 0.7, 2, 1]
    
    plt.scatter_contour([x,y,z], [-3, 2], [-3,2], 150, "MIN", True)
    
    #plt.colorbar(ticks=[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    plt.plot(x, y, 'ko', ms=3)
    plt.xlim(-3, 2)
    plt.ylim(-3, 2)
    plt.title('Tricontour from data points')
    
    
    plt.savefig('test_triangular')

if __name__== "__main__":
    test_all_defaults()
    test_colour_density()
    test_edge_max()
    test_inputted_edge()
    test_circular()
    test_triangular()