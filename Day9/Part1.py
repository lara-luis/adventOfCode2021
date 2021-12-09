import sys

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

matrix = list()
for line in lines:
    lineArray = [int(x) for x in line]
    matrix.append(lineArray)

riskScore = 0
for idxline, line in enumerate(matrix):
    for idx, value in enumerate(line):
        left = sys.maxsize 
        if idx-1 > -1:
            left = line[idx-1]
        
        right = sys.maxsize 
        if idx+1 < len(line):
            right = line[idx+1]

        up = sys.maxsize 
        if idxline-1 > -1:
            up = matrix[idxline-1][idx]
        
        down = sys.maxsize 
        if idxline+1 < len(matrix):
            down = matrix[idxline+1][idx]

        if (value < left and 
            value < right and 
            value < up and 
            value < down):
            riskScore += (1+value)

print(riskScore)