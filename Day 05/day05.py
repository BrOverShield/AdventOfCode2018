import datetime
import os

os.chdir("C:/Users/PPoucH/Documents/GitHub/AdventOfCode2018/Day 05")

filename = "day05 input.txt"
input = open(filename)

inputString = input.read()

cursor = 0
while cursor < len(inputString) - 1:
    print(cursor)
    #print(inputString[:cursor] + " " + inputString[cursor] + " " +  inputString[cursor+1:cursor+10])
    if inputString[cursor].lower() == inputString[cursor + 1].lower():
        if (inputString[cursor].isupper() and inputString[cursor + 1].islower()) or (inputString[cursor].islower() and inputString[cursor + 1].isupper()):
            #print(inputString[:cursor] + " " + inputString[cursor:cursor+2] + " " + inputString[cursor+2:cursor+10])
            inputString = inputString[:cursor] + inputString[cursor+2:]
            cursor -= 1
            if cursor < 0:
                cursor = 0
        else:
            cursor += 1    
    else:
        cursor += 1

print ("answer : " + str(len(inputString)))
print("last : " + str(inputString[len(inputString)]))

