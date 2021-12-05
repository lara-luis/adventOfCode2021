my_file = open("input", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

countIncrease = 0
previousNum = content_list[0]

for integer in content_list[1:]:
    if int(integer) > int(previousNum):
     countIncrease = countIncrease + 1
     
    previousNum = integer


print(countIncrease)