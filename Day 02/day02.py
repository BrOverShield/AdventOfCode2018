
filename = "day02 input.txt"
input = open(filename)

lines = input.read().split()
lines = list(lines)
doubles = 0
triples = 0
doublesFlag = False
triplesFlag = False

for line in lines:
    dictionary = {}
    doublesFlag = False
    triplesFlag = False
    for character in line:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            value = dictionary.get(character)
            dictionary.update({character: value +1})
    for key, value in dictionary.items():
        if value == 3:
            triplesFlag = True
        if value == 2:
            doublesFlag = True
    if triplesFlag:
        triples += 1
    if doublesFlag:
        doubles += 1
    print(dictionary)
    print(doubles)
    print(triples)

input.close() 

print(doubles)
print(triples)

checksum = doubles * triples

print("answer : " + str(checksum))

def StringSplit(stream):
    return iter(stream.splitlines())