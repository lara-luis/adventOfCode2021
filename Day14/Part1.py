from collections import Counter

my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

initial_template = lines[0]
dictionary = dict()

for line in lines[2:]:
    if line.strip() != "":
        el = line.split(" -> ")
        dictionary[el[0]] = el[1]

steps = 10
current_string_list = [x for x in initial_template]
changed = True

current_step = 0
while changed and current_step < steps:
    changed = False
    current_step += 1
    current_string = current_string_list[:]
    num_added_elements = 0
    for idx, el in enumerate(current_string):
        if idx == (len(current_string)-1):
            break

        pair = el +  current_string[idx+1]
        decode = dictionary.get(pair)
        if decode != "":
            current_string_list.insert(num_added_elements + idx + 1, decode)
            num_added_elements += 1
            changed = True

occurence_count = Counter(current_string_list)
most_common_list = occurence_count.most_common()

most_common_quantity = most_common_list[0][1]

least_common_pair = most_common_list[len(most_common_list)-1]
least_common_quantity = least_common_pair[1]

print(most_common_quantity-least_common_quantity)
