import difflib
import collections

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

def contains(string, chars):
    substringArray = [char for char in chars]
    
    contains = True
    for substr in substringArray:
        contains = contains and string.find(substr) > -1

    return contains

digitsSum = 0
for line in lines:
    digitString = line.strip().split("|")
    signalPatterns = digitString[0].strip().split(" ")
    digitListOutput = digitString[1].strip().split(" ")

    # understanding patterns
    digitsMap = {}

    oneCode = [x for x in signalPatterns if len(x) == 2]
    arrayOneCode = [char for char in oneCode[0]]
    signalPatterns.remove(oneCode[0])

    sevenCode = [x for x in signalPatterns if len(x) == 3]
    arraySevenCode = [char for char in sevenCode[0]]
    signalPatterns.remove(sevenCode[0])

    fourCode = [x for x in signalPatterns if len(x) == 4]
    arrayFourCode =  [char for char in fourCode[0]]
    signalPatterns.remove(fourCode[0])

    eightCode = [x for x in signalPatterns if len(x) == 7]
    signalPatterns.remove(eightCode[0])

    # 3 has 5 chars and always contains the same chars as the number 7
    threeCode = [x for x in signalPatterns if len(x) == 5 and contains(x, sevenCode[0])]
    signalPatterns.remove(threeCode[0])

    # 9 has 6 chars and always contains the same chars as the number 3
    nineCode = [x for x in signalPatterns if len(x) == 6 and contains(x, threeCode[0])]
    signalPatterns.remove(nineCode[0])

    # 0 has 6 chars and always contains the same chars as the number 1
    zeroCode = [x for x in signalPatterns if len(x) == 6 and contains(x, oneCode[0])]
    signalPatterns.remove(zeroCode[0])

    # after excluding other numbers that contain 6 chars, only number 6 is left
    sixCode = [x for x in signalPatterns if len(x) == 6]
    #signalPatterns.remove(sixCode[0])

    # 5 has 5 chars and it is contained in number 6
    fiveCode = [x for x in signalPatterns if len(x) == 5 and contains(sixCode[0], x)]
    signalPatterns.remove(fiveCode[0])

    # 2 is the other number with 5 chars that's left
    twoCode = [x for x in signalPatterns if len(x) == 5]

    digitsMap = {
        "".join(sorted(zeroCode[0])): 0,
        "".join(sorted(oneCode[0])): 1,
        "".join(sorted(twoCode[0])): 2,
        "".join(sorted(threeCode[0])): 3,
        "".join(sorted(fourCode[0])): 4,
        "".join(sorted(fiveCode[0])): 5,
        "".join(sorted(sixCode[0])): 6,
        "".join(sorted(sevenCode[0])): 7,
        "".join(sorted(eightCode[0])): 8,
        "".join(sorted(nineCode[0])): 9
    }

    # decoding
    lineDigit = ""
    for digitCode in digitListOutput:
        wordSize = len(digitCode)
        digit = 0
        if wordSize == 2:
            digit = 1
        elif wordSize == 3:
            digit = 7
        elif wordSize == 4:
            digit = 4
        elif wordSize == 7:
            digit = 8
        else:
            orderedDigitCode = "".join(sorted(digitCode))
            digit = digitsMap.get(orderedDigitCode)
        
        lineDigit += str(digit)
    
    digitsSum += int(lineDigit)

print(digitsSum)
