import networkx as nx
import matplotlib.pyplot as plt

def print_matrix(matrix):
    for i,line in enumerate(matrix):
        for j, val in enumerate(line):
            print(str(matrix[i][j]), end ="")
        print("")

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

cost_matrix = list()
for line in lines:
    line_list = list()
    for risk in line:
        line_list.append(int(risk))
    cost_matrix.append(line_list)

gr = nx.DiGraph()

width = len(cost_matrix)
height = len(cost_matrix[0])

for i,line in enumerate(cost_matrix):
    for j, val in enumerate(line):
        gr.add_node((i,j))

        if i + 1 < width:
            gr.add_node((i+1,j))
            gr.add_edge((i+1,j), (i,j), weight=cost_matrix[i][j])
            gr.add_edge((i,j), (i+1,j), weight=cost_matrix[i+1][j])

        if j + 1 < height:
            gr.add_node((i,j+1))
            gr.add_edge((i,j+1), (i,j), weight=cost_matrix[i][j])
            gr.add_edge((i,j), (i,j+1), weight=cost_matrix[i][j+1])

min_path = nx.dijkstra_path(gr, source=(0,0), target=(width-1,height-1))

source_weight = cost_matrix[0][0]
path_risk = 0
for el in min_path:
    x = el[0]
    y = el[1]
    weight = cost_matrix[x][y] 
    path_risk += weight
    cost_matrix[x][y] = "\x1b[6;30;42m" + "" + str(cost_matrix[x][y]) + "" + "\x1b[0m"

path_risk -= source_weight #subtract source node
print(path_risk)

#print_matrix(cost_matrix)