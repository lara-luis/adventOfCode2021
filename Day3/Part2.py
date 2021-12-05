import collections

my_file = open("input", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

index0 = list()

def split(word):
        return [char for char in word]

def most_frequent(List):
    # 0 frequency
    zeroFrequency = List.count("0")
    # 1 frequency
    oneFrequency = List.count("1")
    
    if zeroFrequency > oneFrequency:
        return "0"
    
    if oneFrequency > zeroFrequency:
        return "1"
        
    if oneFrequency == zeroFrequency:
        return "1"
        
def least_frequent(List):
    # 0 frequency
    zeroFrequency = List.count("0")
    # 1 frequency
    oneFrequency = List.count("1")
    
    if zeroFrequency < oneFrequency:
        return "0"
    
    if oneFrequency < zeroFrequency:
        return "1"
        
    if oneFrequency == zeroFrequency:
        return "0"
    
for reportLine in content_list:
    charList = split(reportLine)
    index0.append(charList[0])

mostCommonIndex0 = most_frequent(index0)
leastCommonIndex0 = str(1 - int(most_frequent(index0)))

# Oxygen

filterList = list()

for reportLine in content_list:
    charList = split(reportLine)
    
    if int(charList[0]) == int(mostCommonIndex0):
        filterList.append(reportLine)
 
tmpList = list()
indexI = list()
i = 1
while i < 12:
    for reportLine in filterList:
        charList = split(reportLine)
        indexI.append(charList[i])
        
    mostCommonIndexI = most_frequent(indexI)
    tmpList = list()

    for reportLine in filterList:
        charList = split(reportLine)
        indexBeingVerified = charList[i]
    
        if int(indexBeingVerified) == int(mostCommonIndexI):
            tmpList.append(reportLine)
            
    i += 1
    indexI = list()
    filterList = tmpList
    
    if(len(tmpList) == 1):
        break; 
    
str1 = "" 
oxygenRate = int(str1.join(filterList), 2)

# CO2

filterList = list()

for reportLine in content_list:
    charList = split(reportLine)
    
    if int(charList[0]) == int(leastCommonIndex0):
        filterList.append(reportLine)

tmpList = list()
indexI = list()
i = 1
while i < 12:
    for reportLine in filterList:
        charList = split(reportLine)
        indexI.append(charList[i])
    leastCommonIndexI = least_frequent(indexI)

    tmpList = list()
    
    for reportLine in filterList:
        charList = split(reportLine)
        indexBeingVerified = charList[i]
        
        if int(indexBeingVerified) == int(leastCommonIndexI):
            tmpList.append(reportLine)
    
    i += 1
    indexI = list()
    filterList = tmpList
    
    if(len(tmpList) == 1):
        break;

str1 = "" 
co2Rate = int(str1.join(filterList), 2)

print(oxygenRate*co2Rate)
