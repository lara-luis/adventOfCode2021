my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")
my_file.close()

valid_char = "("
other_valid_char = ")"
valid_char1 = "["
other_valid_char1 = "]"
valid_char2 = "{"
other_valid_char2 = "}"
valid_char3 = "<"
other_valid_char3 = ">"

illegal_chars = list()

for line in lines:
    invalid = False

    chars = [x for x in line]
    stack = []
    for c in chars:
        if not invalid:
            if c == valid_char or c == valid_char1 or c == valid_char2 or c == valid_char3:
                stack.append(c)
            elif c == other_valid_char:
                valid = stack[-1] == valid_char

                if not valid:
                    invalid = True
                    illegal_chars.append(c)

                stack.pop()     
            elif c == other_valid_char1:
                valid = stack[-1] == valid_char1

                if not valid:
                    invalid = True
                    illegal_chars.append(c)

                stack.pop() 
            elif c == other_valid_char2:
                valid = stack[-1] == valid_char2

                if not valid:
                    invalid = True
                    illegal_chars.append(c)

                stack.pop()
            elif c == other_valid_char3:
                valid = stack[-1] == valid_char3

                if not valid:
                    invalid = True
                    illegal_chars.append(c)

                stack.pop()
            else:
                invalid = True

                if not valid:
                    invalid = True
                    illegal_chars.append(c)

    #if len(stack) > 0:
    #    print("incomplete")


#): 3 points.
#]: 57 points.
#}: 1197 points.
#>: 25137 points.

first_char_count = illegal_chars.count(")")
second_char_count = illegal_chars.count("]")
third_char_count = illegal_chars.count("}")
forth_char_count = illegal_chars.count(">")

print(first_char_count*3 + second_char_count*57 + third_char_count*1197 + forth_char_count*25137)