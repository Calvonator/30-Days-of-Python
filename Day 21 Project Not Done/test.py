from matplotlib import pyplot

def get_y(data, column):
    
    y_list = []

    for row in data:
        y_list.append(row[column])

    return y_list

with open("iris.csv", "r") as f:
    flowers = []                            #List to contain dictionaries of flowers
    data = f.readlines()                    #Read data into a list, where each row/line is an entry in the list
    for i in range(1, len(data)):   
        row = data[i].split(',')            #Convert the single string line into a list of seperated values
        flowers.append({
            "sepal_length": row[0], 
            "sepal_width": row[1], 
            "petal_length": row[2], 
            "petal_width": row[3], 
            "species": row[4]
            }   
        )

x = [x for x in range(len(flowers))]

y =  get_y(flowers, 'sepal_length')


x_ticks = []

#for i in range(len(flowers)):
    #x_ticks.append(flowers[i]["species"].strip())

#pyplot.xticks(x, x_ticks, rotation = 45)
pyplot.scatter(y = [1, 2, 3], x = ["one", "two", "three"])
#pyplot.savefig("exgraph.png")
