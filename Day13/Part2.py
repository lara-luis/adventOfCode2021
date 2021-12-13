my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

matrix = list()

coordinates = list()
max_x = -1
max_y = -1

folds = list()

def Fold_Y(fold_y, matrix):
    row_check_index = 1
    fold_row_index = fold_y + 1
    for line in matrix[fold_row_index:]:
        matching_row = matrix[fold_y-row_check_index]
        for idx, x in enumerate(matching_row):
            matching_row[idx] = matrix[fold_row_index][idx] or matching_row[idx]
            matrix[fold_row_index][idx] = False
        fold_row_index += 1 
        row_check_index += 1

def Fold_X(fold_x, matrix):
    row_check_index = 1
    fold_row_index = fold_x + 1
    for idx_y, line in enumerate(matrix):
        second_half_of_the_row = line[fold_row_index:]
        for idx_x, el in enumerate(second_half_of_the_row):
            matching_el = line[fold_x-row_check_index]
            line[fold_x-row_check_index] = el or matching_el
            matrix[idx_y][fold_row_index + idx_x] = False
            #fold_row_index += 1 
            row_check_index += 1
        row_check_index = 1

for line in lines:
    if line != "":
        if line.find("fold") > -1:
            fold = line.replace("fold along ", "")
            folds.append(fold)
        else:
            coord = line.split(",")
            x = int(coord[0])
            y = int(coord[1])
            coordinates.append((x,y))

            if x > max_x:
                max_x = x
            
            if y > max_y:
                max_y = y

for i in range(0,max_y+1):
    field = []
    for j in range(0,max_x+1):
        field.append(False)
    matrix.append(field)

for coord in coordinates:
    x = coord[0]
    y = coord[1]
    matrix[y][x] = True

for fold in folds:
    if fold.find("y") > -1:
        fold_y = fold.replace("y=","")
        Fold_Y(int(fold_y), matrix)
    else:
        fold_x = fold.replace("x=","")
        Fold_X(int(fold_x), matrix)

f = open("output.txt", "a")
for idx_y, line in enumerate(matrix):
    for idx_x, el in enumerate(line):
        if el == True:
            f.write("#")
        else:
            f.write(".")
    f.write("\n")

f.close()