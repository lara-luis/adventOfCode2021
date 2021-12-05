my_file = open("input", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

countIncrease = 0

previousSum = -1
currentSum = -1

currentIndex = 0
listLength = len(content_list)

while currentIndex < listLength-2:
    i = 0
    while i < 3:
        currentSum = int(currentSum) + int(content_list[currentIndex+i])
        i = i + 1

    if previousSum != -1 and currentSum > previousSum:
     countIncrease = countIncrease + 1
     
    previousSum = currentSum
    currentSum = 0
    currentIndex = currentIndex + 1

print(countIncrease)