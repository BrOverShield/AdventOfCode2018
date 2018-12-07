
filename = "day03 input.txt"
input = open(filename)

lines = input.read().split("\n")
lines = list(lines)

dictionary = {}
numbers = {}

for line in lines:
    info = line.split(" ")
    commandNumber = info[0][1:]
    numbers[commandNumber] = "GOOD"
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
                numbers[dictionary.get(str(new_x) + "-" + str(new_y))] = "DEAD"
                dictionary[str(new_x) + "-" + str(new_y)] = "X"
                numbers[commandNumber] = "DEAD"
            else:
                dictionary[str(new_x) + "-" + str(new_y)] = commandNumber
            width_iter += 1

        height_iter += 1

count = 0

for key, value in numbers.items():
    if value == "GOOD":
        print("GOOD: " + key)