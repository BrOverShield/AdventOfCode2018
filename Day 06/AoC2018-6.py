INPUT_FILE_PATH = "day06 test.txt"
X_INDEX = 0
Y_INDEX = 1

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

sides = [UP, RIGHT, DOWN, LEFT]

inputDictionary = []
coordinatesDictionary = {}

lowestX = 1
lowestY = 1
highestX = 0
highestY = 0

def saveCoordinates(input, coordinatesDictionary):
    if input["X"] not in coordinatesDictionary:
        coordinatesDictionary[input["X"]] = {}
    if input["Y"] not in coordinatesDictionary[input["X"]]:
        coordinatesDictionary[input["X"]][input["Y"]] = {"letter" : None, "distance" : 0}
    if coordinatesDictionary[input["X"]][input["Y"]]["letter"] != "":
        if coordinatesDictionary[input["X"]][input["Y"]]["distance"] > input["distance"]:
            coordinatesDictionary[input["X"]][input["Y"]]["letter"] = input["letter"]
            coordinatesDictionary[input["X"]][input["Y"]]["distance"] = input["distance"]
        return 0
    else:
        coordinatesDictionary[input["X"]][input["Y"]]["letter"] = input["letter"]
        return 1

def isInsideLimites(input):
    if input["X"] > highestX or input["X"] < lowestX or input["Y"] > highestY or input["Y"] < lowestY:
        return False
    else:
        return True

file = open(INPUT_FILE_PATH)
data = file.read()
data = data.replace(" ", "")
lines = data.split("\n")
i = 0
for line in lines:
    coordinates = line.split(",")
    inputDictionary.append({"X" : int(coordinates[X_INDEX]), "Y" : int(coordinates[Y_INDEX]), "letter" : i})
    i = i + 1
for input in inputDictionary:
    if lowestX > input["X"]:
        lowestX = input["X"]
    if lowestY > input["Y"]:
        lowestY = input["Y"]
    if highestX < input["X"]:
        highestX = input["X"]
    if highestY < input["Y"]:
        highestY = input["Y"]
print(lowestX)
print(lowestY)
print(highestX)
print(highestY)

keepGoing = True
step = 0
while keepGoing:
    step = step + 1
    distance = (step * 1)
    keepGoing = False
    for input in inputDictionary:
        for state in sides:
            pointerX = input["X"] - distance
            for pointerY in range(input["Y"] - distance, input["Y"] + distance):
                cell = {"X": pointerX, "Y": pointerY, "letter": input["letter"], "distance": abs(abs(input["X"]) - abs(pointerX)) + abs(abs(input["Y"]) - abs(pointerY))}
                if isInsideLimites(cell):
                    result = saveCoordinates(cell, coordinatesDictionary)
                    if result:
                        keepGoing = True
            pointerY = input["Y"] + distance
            for pointerX in range(input["X"] - distance, input["X"] + distance):
                cell = {"X": pointerX, "Y": pointerY, "letter": input["letter"], "distance": abs(abs(input["X"]) - abs(pointerX)) + abs(abs(input["Y"]) - abs(pointerY))}
                if isInsideLimites(cell):
                    result = saveCoordinates(cell, coordinatesDictionary)
                    if result:
                        keepGoing = True
            pointerX = pointerX + distance
            for pointerY in range(input["Y"] + distance, input["Y"] - distance):
                cell = {"X": pointerX, "Y": pointerY, "letter": input["letter"], "distance": abs(abs(input["X"]) - abs(pointerX)) + abs(abs(input["Y"]) - abs(pointerY))}
                if isInsideLimites(cell):
                    result = saveCoordinates(cell, coordinatesDictionary)
                    if result:
                        keepGoing = True
            pointerY = pointerY - distance
            for pointerX in range(input["X"] + distance, input["X"] - distance):
                cell = {"X": pointerX, "Y": pointerY, "letter": input["letter"], "distance": abs(abs(input["X"]) - abs(pointerX)) + abs(abs(input["Y"]) - abs(pointerY))}
                if isInsideLimites(cell):
                    result = saveCoordinates(cell, coordinatesDictionary)
                    if result:
                        keepGoing = True
results = {}
for x in coordinatesDictionary:
    for y in coordinatesDictionary[x]:
        if coordinatesDictionary[x][y]["letter"] not in results:
            results[coordinatesDictionary[x][y]["letter"]] = 0
        results[coordinatesDictionary[x][y]["letter"]] += 1
        print("X : " + str(x) + " | Y : " + str(y));

highestResult = 0


for letter in results:
    if highestResult < results[letter]:
        highestResult = results[letter]

print(highestResult)




