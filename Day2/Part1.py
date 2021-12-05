my_file = open("input", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

currPositionHorizontal = 0
currPositionVertical = 0

for coordLine in content_list:
    coordSplit = coordLine.split(" ")
    coordDirection = coordSplit[0]
    coordNum = int(coordSplit[1])
    
    if coordDirection == "forward":
        currPositionHorizontal += coordNum
    elif coordDirection == "up": 
        currPositionVertical -= coordNum
    else:
        # down
        currPositionVertical += coordNum


print(currPositionHorizontal * currPositionVertical)