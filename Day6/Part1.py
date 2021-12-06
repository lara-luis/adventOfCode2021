import collections

my_file = open("input", "r")
timers = my_file.read()
timerList = [int(x) for x in timers.split(",")]
lifespan = 80 #days

def updateTimer(internalTimer):
    if internalTimer == 0:
        internalTimer = 6
    else:
        internalTimer = internalTimer-1
    return internalTimer

my_file.close()

for i in range(lifespan):
    newElements = timerList.count(0)
    timerList = list(map(updateTimer, timerList))
    
    newElementsList = [8] * newElements;
    timerList.extend(newElementsList)
    
print(len(timerList))