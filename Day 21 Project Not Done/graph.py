from matplotlib import pyplot


def create_scatter_graph(x, y, x_ticks):
    
    pyplot.xticks(x, x_ticks, rotation = 45)
    pyplot.scatter(x, y)
    pyplot.savefig("newgraph.png")