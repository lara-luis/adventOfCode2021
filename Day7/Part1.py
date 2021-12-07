import collections
import statistics

my_file = open("input", "r")
positions = my_file.read()
positionsList = [int(x) for x in positions.split(",")]

medianPosition = statistics.median(positionsList)

fuelSpent = 0
for crabPos in positionsList:
    fuelSpent += abs(crabPos - int(medianPosition))

print(fuelSpent)

