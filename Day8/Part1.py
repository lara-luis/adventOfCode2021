import collections

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

count = 0
for line in lines:
    digitString = line.strip().split("|")
    digitListOutput = digitString[1].split(" ")

    for digit in digitListOutput:
        wordSize = len(digit)
        if wordSize == 2 or wordSize == 3 or wordSize == 4 or wordSize == 7:
            count += 1

print(count)