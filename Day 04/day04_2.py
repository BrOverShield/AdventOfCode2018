import datetime


filename = "day04 input.txt"
input = open(filename)

lines = input.read().split("\n")
lines = list(lines)

entries = []
guards = {}

for line in lines:
    year = int(line[1:5])
    month = int(line[6:8])
    day = int(line[9:11])
    hour = int(line[12:14])
    minute = int(line[15:17])
    message = line[19:]
    date = datetime.datetime(year, month, day, hour, minute)
    entries.append({"date": date, "message": message})

# sort
entries.sort(key=lambda x: x['date'])

guards = {}
guardID = 0
falls = datetime.datetime.now()
wakes = datetime.datetime.now()

for entry in entries:
    
    if entry.get("message")[0] == "G":
        info = entry.get("message").split(" ")
        guardID = info[1][1:]
        if guardID not in guards:
            guards[guardID] = {"total": 0, "times": {}}

    if entry.get("message")[0] == "w":
        wakes = entry.get("date")
        if falls.date() == wakes.date():
            sleepTime = wakes.minute-falls.minute
            guards.get(guardID)["total"] += sleepTime
            i = 0
            while i < sleepTime:
                if falls.minute + i not in guards.get(guardID)["times"]:
                    guards.get(guardID)["times"][falls.minute + i] = 1
                else:
                    guards.get(guardID)["times"][falls.minute + i] += 1
                i += 1
        else:
            print("TROUBLE!!!!!!!!!!!!!!!!!!")


    if entry.get("message")[0] == "f":
        falls = entry.get("date")

maxTime = {"time": 0, "guard": 0, "number": 0}

for guard, times in guards.items():
    for time, value in times["times"].items():
        if value > maxTime["number"]:
            maxTime["number"] = value
            maxTime["guard"] = guard
            maxTime["time"] = time

print("time : " + str(maxTime["time"]))
print("guard : " + str(maxTime["guard"]))

print("answer : " + str(int(maxTime["time"]) * int(maxTime["guard"])))