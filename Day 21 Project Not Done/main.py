from matplotlib import pyplot
import data_storage as ds
import graph


flower_data = ds.get_data()


x = [1, 2, 3]

x_ticks = ds.get_x(flower_data)

y_data = ds.get_y(flower_data, "sepal_length")


graph.create_scatter_graph(x, y_data, x_ticks)

