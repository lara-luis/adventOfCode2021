import collections
import statistics

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

for i,line in enumerate(lines):
    if(i % 2 == 1):
        digitList = content.split("|")

        digitListOutput = digitList[1].strip().split(" ")
        count = 0

        for digit in digitListOutput:
            wordSize = len(digit)
            if wordSize == 2 or wordSize == 3 or wordSize == 4 or wordSize == 7:
                count += 1

print(count)




