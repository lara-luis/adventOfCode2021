import sys

sys.setrecursionlimit(5000)

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

def findBasin(i,j,matrix, positionsVerified):
    if i < 0 or j < 0: 
        return 0

    if i >= len(matrix) or j >= len(matrix[0]):
        return 0

    if positionsVerified[i][j]:
        return 0

    if matrix[i][j] == 9:
        positionsVerified[i][j] = True
        return 0
    else:
        positionsVerified[i][j] = True
        return 1 + findBasin(i+1,j,matrix, positionsVerified) + findBasin(i,j+1,matrix, positionsVerified) + findBasin(i-1,j,matrix, positionsVerified) + findBasin(i,j-1,matrix, positionsVerified)

matrix = list()
for line in lines:
    lineArray = [int(x) for x in line]
    matrix.append(lineArray)

basinSizes = list()
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

            #to avoid to have the rows referring to always the same row 
            # and when updating one, updating the same position in all rows...
            positionsVerified = list()
            for i in range(0,len(matrix)):
                field = []
                for j in range(0,len(matrix[0])):
                    field.append(False)
                positionsVerified.append(field)

            size = findBasin(idxline, idx,matrix, positionsVerified)
            basinSizes.append(int(size))

basinSizes.sort(reverse = True)
print(basinSizes[0] * basinSizes[1] * basinSizes[2])