import datetime


filename = "day05 input.txt"
input = open(filename)

inputString = input.read()

cursor = 0
while cursor < len(inputString) - 1:
    if inputString[cursor].lower() == inputString[cursor + 1].lower():
        if (inputString[cursor].isupper() and inputString[cursor + 1].islower()) or (inputString[cursor].islower() and inputString[cursor + 1].isupper()):
            inputString = inputString[:cursor] + inputString[cursor+2:]
            cursor -= 2
            
    cursor += 1

print (len(inputString))

