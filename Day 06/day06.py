import os

filename = "day06 input.txt"
input = open(filename)

lines = input.read().split("\n")
lines = list(lines)

xs = []
ys = []

grid = {}

owners = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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

maxX += 2
maxY += 2

minX -= 1
minY -= 1

for i, val in enumerate(xs):
    grid[str(xs[i]) + "," + str(ys[i])] = {"distance" : 0, "owner" : i}

end = False
iteration = 1
xDirection = 0
yDirection = 0
x = 0
y = 0
while end == False:
    change = False
    for i, val in enumerate(xs): #pour chaque point central
        for stage in range(0, 4):
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
            #print("x : " + str(x))
            #print("y : " + str(y))
            #print("xDirection : " + str(xDirection))
            #print("yDirection : " + str(yDirection))
            #os.system("pause")
            for step in range(0, iteration * 2 +1):
                name = str(xs[i] + xDirection * step + x) + "," + str(ys[i] + yDirection * step + y)
                #print(name)
                #os.system("pause")
                if (xs[i] + xDirection * step + x) <= maxX and (xs[i] + xDirection * step + x) >= minX and (ys[i] + yDirection * step + y) <= maxY and (ys[i] + yDirection * step + y) >= minY:
                    Ax = xs[i]
                    Bx = xs[i] + xDirection * step + x
                    Ay = ys[i]
                    By = ys[i] + yDirection * step + y
                    distance = abs(Ax - Bx) + abs(Ay - By)
                    if name in grid:
                        if grid[name]["distance"] == distance:
                            if grid[name]["owner"] != i:
                                grid[name]["owner"] = "."
                        elif grid[name]["distance"] > distance:
                            grid[name]["distance"] = distance
                            grid[name]["owner"] = i
                    else:
                        grid[name] = {"distance" : distance, "owner" : i}
                    change = True
    #for yi in range(minY, maxY):
     #   string = ""
      #  for xi in range(minX, maxX):
       #     name = str(xi) + "," + str(yi)
        #    if name in grid:
         #       string += str(grid[name]["owner"])
          #  else:
           #     string += " "
        #print(string)
    #os.system("pause")
    if change == False:
        end = True
    iteration += 1

#for y in range(minY, maxY):
 #   string = ""
  #  for x in range(minX, maxX):
   #     name = str(x) + "," + str(y)
    #    if grid[name]["distance"] != 0:
     #       if grid[name]["owner"] == ".":
      #          string += grid[name]["owner"]
       #     else:
        #        string += owners[int(grid[name]["owner"])].lower()
        #else:
        #    string += owners[int(grid[name]["owner"])].upper()
    #print(string)

results = {}

for location in grid:

for result in results:
    print(result)