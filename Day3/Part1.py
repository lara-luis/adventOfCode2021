import collections

my_file = open("input", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

index0 = list()
index1 = list()
index2 = list()
index3 = list()
index4 = list()
index5 = list()
index6 = list()
index7 = list()
index8 = list()
index9 = list()
index10 = list()
index11 = list()

def split(word):
        return [char for char in word]

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

for reportLine in content_list:
    charList = split(reportLine)
    index0.append(charList[0])
    index1.append(charList[1])
    index2.append(charList[2])
    index3.append(charList[3])
    index4.append(charList[4])
    index5.append(charList[5])
    index6.append(charList[6])
    index7.append(charList[7])
    index8.append(charList[8])
    index9.append(charList[9])
    index10.append(charList[10])
    index11.append(charList[11])
    
    
gammaRateString = most_frequent(index0) + most_frequent(index1) + most_frequent(index2) + most_frequent(index3) + most_frequent(index4) + most_frequent(index5) + most_frequent(index6) + most_frequent(index7) + most_frequent(index8) + most_frequent(index9) + most_frequent(index10) + most_frequent(index11)
gammaRateDecimal = int(gammaRateString, 2)

epsilonRateString = str(1 - int(most_frequent(index0))) + str(1 - int(most_frequent(index1))) + str(1-int(most_frequent(index2))) + str(1-int(most_frequent(index3))) + str(1-int(most_frequent(index4))) + str(1 - int(most_frequent(index5))) + str(1-int(most_frequent(index6))) + str(1-int(most_frequent(index7))) + str(1-int(most_frequent(index8))) + str(1-int(most_frequent(index9))) + str(1-int(most_frequent(index10))) + str(1-int(most_frequent(index11)))
epsilonRateDecimal = int(epsilonRateString, 2)

print(gammaRateDecimal*epsilonRateDecimal)