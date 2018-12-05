
filename = "day01 input.txt"
input = open(filename)

lines = input.read().split()
lines = list(lines)
frequencies = [0]
frequency = 0
loop = True

while loop :
    for line in lines:
        frequency += int(line)
        print(str(line))
        if frequency in frequencies:
            loop = False
            break
        else:
            frequencies.append(frequency)
            print(str(frequency) + " added to the frequencies")

input.close() 

print("answer : " + str(frequency))

def StringSplit(stream):
    return iter(stream.splitlines())