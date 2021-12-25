import sys
import itertools
from itertools import product

my_file = open("input", "r")
content = my_file.read()
lines = content.split(",")

parsing_x = lines[0].replace("target area: x=", "")
x_range = parsing_x.split("..")
x1 = int(x_range[0])
x2 = int(x_range[1])
parsing_y = lines[1].replace(" y=", "")
y_range = parsing_y.split("..")
y1 = int(y_range[0])
y2 = int(y_range[1])

start_x = 0
start_y = 0

hit = False
initial_x = 1
current_x = initial_x
initial_y = 1
current_y = initial_y

probe_x = 0
probe_y = 0
max_y = -sys.maxsize-1

hits = list()
max_ys = list()

while current_x < 150:
    while current_y < 150:
        while not hit:
            probe_x += current_x
            probe_y += current_y 

            if probe_y > max_y:
                max_y = probe_y

            if probe_x >= x1 and probe_x <= x2 and probe_y >= y1 and probe_y <= y2:
                hit = True
                hits.append((initial_x, initial_y))
                max_ys.append(max_y)
                break

            if probe_y < y2:
                hit = False
                break

            if current_x > 0:
                current_x -= 1
            elif current_x < 0:
                current_x += 1

            current_y -= 1
        
        initial_y += 1
        current_y = initial_y
        current_x = initial_x
        probe_x = 0
        probe_y = 0
        hit = False
        max_y = -sys.maxsize-1
    
    initial_x += 1
    initial_y = 1
    current_x = initial_x
    current_y = initial_y
    probe_x = 0
    probe_y = 0
    hit = False
    max_y = -sys.maxsize-1

print(max(max_ys))
#print(hits)