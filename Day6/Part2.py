import collections

my_file = open("input", "r")
timers = my_file.read()
timerList = [int(x) for x in timers.split(",")]
lifespan = 256 #days

timersCount = [0] * 9

for idx in range(8):
    timersCount[idx] = timerList.count(idx)

for i in range(lifespan): 
    tmp = timersCount[0] 
    timersCount[0] = timersCount[1]
    timersCount[1] = timersCount[2]
    timersCount[2] = timersCount[3]
    timersCount[3] = timersCount[4]
    timersCount[4] = timersCount[5]
    timersCount[5] = timersCount[6]
    timersCount[6] = timersCount[7] + tmp
    timersCount[7] = timersCount[8]
    timersCount[8] = tmp

print(sum(timersCount))