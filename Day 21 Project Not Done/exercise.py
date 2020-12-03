from matplotlib import pyplot  


x_data = [1, 2, 3, 4, 5]
y_data = [5.5, 4.4, 3.3, 2.2, 1.1]


pyplot.scatter(x_data, y_data)
pyplot.savefig("graph.png")