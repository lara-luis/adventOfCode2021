my_file = open("input", "r")
content = my_file.read()
lines = content.split("\n")

start = list()
paths = dict()

built_paths = list()

def build_path(currentPlace, currentPath, built_paths):
    if currentPlace.islower():
        # avoiding to repeat small caves
        if currentPath.count(currentPlace) > 0:
            return
    
    if currentPlace == "end":
        currentPath.append(currentPlace)
        built_paths.append(currentPath)
        return
    
    this_place_paths = paths.get(currentPlace)
    if this_place_paths != None:
        currentPath.append(currentPlace)
        for place in this_place_paths:
            build_path(place, currentPath[:], built_paths)


for line in lines:
    line_components = line.split("-")
    if line_components[0] == "start":
        start.append(line_components[1])

    if line_components[1] == "start":
        start.append(line_components[0])

    else:
        if line_components[0] == "end":
            tmp = line_components[0]
            line_components[0] = line_components[1]
            line_components[0] = tmp

        dests = paths.get(line_components[0])
        if dests:
            dests.append(line_components[1])
        else:
            new_list = list()
            new_list.append(line_components[1])
            paths[line_components[0]] = new_list

        dests = paths.get(line_components[1])
        if dests:
            dests.append(line_components[0])
        else:
            new_list = list()
            new_list.append(line_components[0])
            paths[line_components[1]] = new_list

for path in start:
    new_path = list()
    new_path.append("start")
    build_path(path, new_path[:], built_paths)

print(len(built_paths))

