my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

steps = 1000
num_of_flashes = 0
matrix = list()
first_flash_step = -1

for line in lines:
    line_array = [int(x) for x in line]
    matrix.append(line_array)

number_of_matrix_elements = len(matrix) * len(matrix[0])
    
def calculateFlashes(i,j, flashed) -> int:
    if i < 0 or j < 0: 
        return 0

    if i >= len(matrix) or j >= len(matrix[0]):
        return 0

    if matrix[i][j] == 10 and flashed[i][j]:
        return 0
   
    matrix[i][j] += 1

    if matrix[i][j] == 10:
        #flashes
        if not flashed[i][j]:
            flashed[i][j] = True
            return (1 + calculateFlashes(i+1,j, flashed) + 
            calculateFlashes(i,j+1, flashed) + 
            calculateFlashes(i-1,j, flashed) + 
            calculateFlashes(i,j-1, flashed) +
            calculateFlashes(i-1,j-1, flashed) + 
            calculateFlashes(i+1,j+1, flashed) + 
            calculateFlashes(i+1,j-1, flashed) + 
            calculateFlashes(i-1,j+1, flashed))
    return 0
    
for step in range(1, steps):
    flashed = list()
    for i in range(0,len(matrix)):
        field = []
        for j in range(0,len(matrix[0])):
            field.append(False)
        flashed.append(field)
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            num_of_flashes = num_of_flashes + calculateFlashes(i,j, flashed)

    # all of them flashing
    occurrences_of_flashes = 0
    for line in matrix:
        occurrences_of_flashes += line.count(10)
        
    if first_flash_step == -1 and occurrences_of_flashes == number_of_matrix_elements:
        first_flash_step = step
        break

    for k in range(0,len(matrix)):
        for m in range(0,len(matrix[0])): 
            if matrix[k][m] == 10:
                matrix[k][m] = 0

print(first_flash_step)
