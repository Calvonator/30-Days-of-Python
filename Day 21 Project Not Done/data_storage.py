
data_file = "iris.csv"


def get_data():

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
                "species": row[4].strip()
                }   
            )
    return flowers


def get_x(data):

    x_list = set()

    for row in data:
        x_list.add(row["species"])

    return x_list

def get_y(data, column):
    
    y_list = []

    for row in data:
        y_list.append(row[column])

    return y_list
