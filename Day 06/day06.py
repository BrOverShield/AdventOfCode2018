def calculateManhattanDistance(x1, x2, y1, y2):
    x = [x1, x2]
    y = [y1, y2]
    x1 = max(x)
    x2 = min(x)
    y1 = max(y)
    y2 = min(y)
    #print(x1)
    #print(x2)
    #print(y1)
    #print(y2)
    return (x1 - x2) + (y1-y2)

filename = "day06 example.txt"
input = open(filename)

lines = input.read().split("\n")
lines = list(lines)

xs = []
ys = []

grid = {}

for line in lines:
    coordinates = line.split(",")
    x = int(coordinates[0])
    y = int(coordinates[1])
    xs.append(x)
    ys.append(y)

maxX = max(xs)
maxY = max(ys)

minX = min(xs)
minY = min(ys)

maxX += 1
maxY += 1

minX -= 1
minY -= 1

for i, val in enumerate(xs):
    grid[str(xs[i]) + "," + str(ys[i])] = 0

print(grid)

end = False
iteration = 1
xDirection = 0
yDirection = 0
x = 0
y = 0
while end == False:
    change = False
    for i, val in enumerate(xs): #pour chaque point central
        print("xs[i] : " + str(xs[i]))
        print("ys[i] : " + str(ys[i]))
        for stage in range(0, 3):
            if stage == 0:
                x = iteration
                y = (-1 * iteration)
                xDirection = 0
                yDirection = 1
            if stage == 1:
                x = iteration
                y = iteration
                xDirection = -1
                yDirection = 0
            if stage == 2:
                x = (-1 * iteration)
                y = iteration
                xDirection = 0
                yDirection = -1
            if stage == 3:
                x = (-1 * iteration)
                y = (-1 * iteration)
                xDirection = 1
                yDirection = 0
            for step in range(0, iteration * 2):
                #print("x : " + str(xs[i] + xDirection * step + x))
                #print("y : " + str(ys[i] + yDirection * step + y))
                if (xs[i] + xDirection * step + x) <= maxX and (xs[i] + xDirection * step + x) >= minX and (ys[i] + yDirection * step + y) <= maxY and (ys[i] + yDirection * step + y) >= minY:
                    if str(xs[i] + xDirection * step + x) + "," + str(ys[i] + yDirection * step + y) in grid:
                        grid[str(xs[i] + xDirection + x) + "," + str(ys[i] + yDirection * step + y)] = calculateManhattanDistance((xs[i] + xDirection * step + x), xs[i], (ys[i] + yDirection * step + y), ys[i])
                    else:
                        grid[str(xs[i] + xDirection * step + x) + "," + str(ys[i] + yDirection * step + y)] = calculateManhattanDistance((xs[i] + xDirection * step + x), xs[i], (ys[i] + yDirection * step + y), ys[i])
                    change = True
                print(grid)
    if change == False:
        end = True
    iteration += 1