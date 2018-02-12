import json
from matplotlib import pyplot as plot


# data = {
#   "data": [
#     [1, 1],
#     [2, 2],
#     [3, 3],
#     [4, 4]
#   ]
# }

# with open('data.json', 'w') as file_handle:
#     json.dump(data, file_handle)

def plotJSONdata(fileName, fileExtension):
    fileToRead = fileName + fileExtension
    with open(fileToRead, 'r') as file_handle:
        data = json.load(file_handle)
        print(data)

    xcoords = []
    ycoords = []
    print(data)
    for i in data['data']:
        xcoords.append(i[0])
        ycoords.append(i[1])

    plot.plot(xcoords, ycoords, marker="o", markersize=5, color="red")
    plot.show()


plotJSONdata('data', '.json')