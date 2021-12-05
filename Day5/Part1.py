import collections

my_file = open("input", "r")
bingoNumbersLine = my_file.read()
content = bingoNumbersLine.split("\n")

my_file.close()
countsMap = {} #map

for line in content:
    numberPair = line.split(" -> ")
    [x1,y1] = numberPair[0].split(",")
    [x2,y2] = numberPair[1].split(",")
    
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    
    if x1 == x2:
        # vertical
        if y1 > y2:
            tmp = y2
            y2 = y1
            y1 = tmp
        
        intermediateYs = range(y1,y2+1,1)
        
        for y in intermediateYs:
            currentCount = countsMap.get((x1,y))
            if currentCount:
                # already exists in dictionary
                countsMap[(x1,y)] = currentCount+1
            else:
                countsMap[(x1,y)] = 1

    if y1 == y2:
        # horizontal
        if x1 > x2:
            tmp = x2
            x2 = x1
            x1 = tmp
            
        intermediateXs = range(x1,x2+1,1)
        
        for x in intermediateXs:
            currentCount = countsMap.get((x,y1))
            if currentCount:
                # already exists in dictionary
                countsMap[(x,y1)] = currentCount+1
            else:
                countsMap[(x,y1)] = 1

result = sum(1 for count in list(countsMap.values()) if count > 1)
print(result)
