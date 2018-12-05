
filename = "day03 input.txt"
input = open(filename)

lines = input.read().split("\n")
lines = list(lines)

dictionary = {}

for line in lines:
    info = line.split(" ")
    commandNumber = info[0][1:]
    coordonnees = info[2].split(",")
    x = coordonnees[0]
    y = coordonnees[1][:-1]
    dimensions = info[3].split("x")
    width = dimensions[0]
    height = dimensions[1]

    height_iter = 0
    while height_iter < int(height):
        new_y = int(y) + height_iter
        width_iter = 0
        while width_iter < int(width):
            new_x = int(x) + width_iter
            if str(new_x) + "-" + str(new_y) in dictionary:
                dictionary[str(new_x) + "-" + str(new_y)] = "X"
            else:
                dictionary[str(new_x) + "-" + str(new_y)] = commandNumber
            width_iter += 1

        height_iter += 1

count = 0

for key, value in dictionary.items():
    if value == "X":
        count += 1

print(count)