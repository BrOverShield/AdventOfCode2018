import datetime
import os

os.chdir("C:/Users/PPoucH/Documents/GitHub/AdventOfCode2018/Day 05")

filename = "day05 input.txt"
input = open(filename)

inputText = input.read()

letters = "abcdefghijklmnzopqrstuvwxy"
answers = {}

for letter in letters:
    print(letter)
    inputString = inputText.replace(letter, "").replace(letter.upper(), "")

    cursor = 0
    while cursor < len(inputString) - 1:
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

    answers[letter] = len(inputString)

for letter, answer in answers.items():
    print(letter + " : " + str(answer))

seq = [value for key, value in answers.items()]

minimum = min(seq)

print(minimum)






