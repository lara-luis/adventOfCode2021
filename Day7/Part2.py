import collections
import statistics

my_file = open("input", "r")
positions = my_file.read()
positionsList = [int(x) for x in positions.split(",")]

def calculateFuel(num):
    res = 0

    if num == 0:
        return 0    
    else:
        for i in range(1,num + 1):
            res = res + i

    return res

positionsList.sort()
maxPos = max(positionsList)
minPos = min(positionsList) 
allPotentialPositions = [int(x) for x in range(minPos,maxPos+1)]

movesMatrix = list()

for i in allPotentialPositions:
    line = list()
    for pos in positionsList:
        line.append(calculateFuel(abs(pos - i)))

    movesMatrix.append(line)

finalSum = list()

for positionLine in movesMatrix:
    finalSum.append(sum(positionLine))

print(min(finalSum))