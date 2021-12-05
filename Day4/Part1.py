import collections

def isBingo(matrix):
    # has row complete?
    for line in matrix:
        if all(flag for (_, flag) in line):
            return True
            
    # has column complete?
    i = 0
    while i < 5:
        column = list()
        j = 0
        while j < 5:
            columnNumber = matrix[j][i]
            column.append(columnNumber)
            j += 1
        
        if len(column) > 0 and all(flag for (_, flag) in column):
            return True 
        else:    
            i += 1
    
    return False
 
def CalculateSumOfUnmarkedNumbers(matrix):
    sumTotal = 0
    for line in matrix:
        sumOfLine = sum(int(number) for (number, flag) in line if flag == False)
        sumTotal = sumTotal + sumOfLine
    return sumTotal
    
my_file = open("input", "r")
bingoNumbersLine = my_file.readline().strip('\n')
bingoNumbersList = bingoNumbersLine.split(",")

content = my_file.read()
matrixList = content.split("\n\n")
#matrixList.pop(0)
my_file.close()

matrixArrays = list()
finalMatrix = list()
matrixLine = list()
i = 1
    
for matrix in matrixList:
    matrixLines = matrix.split("\n")
    matrixNumberArray = list()
    for matrixLine in matrixLines:
        if matrixLine != "":
            matrixNumberLine = [[number,False] for number in matrixLine.split(" ") if number != "''" and number != ""]
    
            finalMatrix.append(matrixNumberLine)
            if i == 5:
                #end of one matrix
                matrixArrays.append(finalMatrix)
                finalMatrix = list()
                i = 1
            else:
                i += 1

winningMatrix = list()
winningNumber = -1

for bingoNumber in bingoNumbersList:
    #print(bingoNumbersList)
    for matrix in matrixArrays:
        for matrixLine in matrix:
            for matrixNumber in matrixLine:
                if matrixNumber[0] == bingoNumber:
                    matrixNumber[1] = True
        
        bingo = isBingo(matrix)
        if bingo:
            winningMatrix = matrix
            winningNumber = bingoNumber
            break
    
    if len(winningMatrix) > 0:
        break


sumOfUnmarkedNumbers = CalculateSumOfUnmarkedNumbers(winningMatrix)
print(sumOfUnmarkedNumbers*int(winningNumber))