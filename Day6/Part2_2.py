import collections

my_file = open("input", "r")
timers = my_file.read()
timerList = [int(x) for x in timers.split(",")]
lifespan = 256 #days

def RecursiveFunction(num, iteration):

    if iteration == lifespan:
        return 0
      
    if num == 0:
        return 1 + RecursiveFunction(6, iteration+1) + RecursiveFunction(8, iteration+1)

    return RecursiveFunction(num-1, iteration+1)


result = 0
size = len(timerList)
for n in timerList:
    result += 1+ RecursiveFunction(n-1, 1)
    
print(result)