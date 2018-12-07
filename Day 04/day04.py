import datetime


filename = "day4.txt"
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

seq = [value["total"] for key, value in guards.items()]

maxTime = max(seq)
target = 0

for guardID, values in guards.items():
    if values["total"] == maxTime:
        target = guardID
        break

print("guard target: " + str(target))

seq = [value for key, value in guards[target]["times"].items()]

maxMinute = max(seq)

for minute, value in guards[target]["times"].items():
    if value == maxMinute:
        targetMinute = minute
        break

print("minuteTarget: " + str(targetMinute))

print("nombre de fois : " + str(maxMinute))

answer = int(target) * int(targetMinute)

print("answer : " + str(answer))