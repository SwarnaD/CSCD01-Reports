import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

data = np.array([[0.1, 0.3],
               [0.6, 1]])

plt.rcParams['ytick.minor.visible'] = True

plt.pcolormesh(data, norm=LogNorm())
plt.colorbar()
