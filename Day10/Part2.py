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
total_scores = list()

for line in lines:
    invalid = False

    chars = [x for x in line]
    stack = []
    completion_chars = []
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
    
    if not invalid:
        if len(stack) > 0:
            for c in reversed(stack):
                if c == valid_char:
                    completion_chars.append(other_valid_char)  
                if c == valid_char1:
                    completion_chars.append(other_valid_char1) 
                if c == valid_char2:
                    completion_chars.append(other_valid_char2) 
                if c == valid_char3:
                    completion_chars.append(other_valid_char3) 
        
        line_score = 0
        for c in completion_chars:
            line_score = line_score*5
            if c == other_valid_char:
                line_score += 1
            if c == other_valid_char1:
                line_score += 2
            if c == other_valid_char2:
                line_score += 3
            if c == other_valid_char3:
                line_score += 4
        
        total_scores.append(line_score)

#): 1 point.
#]: 2 points.
#}: 3 points.
#>: 4 points.

total_scores.sort()
final_value = 0

middle = float(len(total_scores))/2.
if middle % 2 != 0:
    final_value = total_scores[int(middle - .5)]
else:
    final_value = (total_scores[int(middle)], total_scores[int(middle-1)])

print(final_value)