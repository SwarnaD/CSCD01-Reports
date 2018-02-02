import numpy as np
import matplotlib.pyplot as plt
import sys

def contour():
	X = np.arange(6)
	Y = np.arange(6)
	Z = [[2,3,6,1,3,5],[3,5,1,3,4,6], [1,7,0,4,7,2], [1,5,3,2,7,8], [9,6,3,7,2,3], [1,2,3,6,7,3]]
	levels = np.linspace(-1, 10, 100)

	cs = plt.contourf(X, Y, Z, levels=levels)
	plt.colorbar(cs, format="%.2f")
	plt.title('Contour Plot')
	plt.show()

def scatter():
	x = [1,2,3,4,5]
	y = [3,1,4,9,3]

	plt.scatter(x, y, alpha=0.5)
	plt.show()

def bar():
	x = np.arange(4)
	y = np.random.rand(4)

	fig, ax = plt.subplots()
	plt.bar(x, y)
	plt.xticks(x, ('\t\t\tPos1', '\t\t\tPos2', '\t\t\tPos3', '\t\t\tPos4'))
	plt.show()

if __name__== "__main__":
	print (sys.argv[1])
	arg = sys.argv[1]
	if(arg == "0"):
		contour()
	elif(arg == "1"):
		scatter()
	elif(arg == "2"):
		bar()