
filename = "day02 input.txt"
input = open(filename)

lines = input.read().split()
lines = list(lines)

answer = False
end = False
mismatch = False
position = 0
string1_iter = 0
while answer == False:
    
    string1 = lines[string1_iter]

    string2_iter = 0

    while answer == False and end == False:

        string2 = lines[string2_iter]

        if string1 == string2 or len(string1) != len(string2):
            break
        else:
            mismatch = False
            i = 0
            while i < len(string1):
                if string1[i] != string2[i]:
                    if mismatch == True:
                        mismatch = False
                        break
                    else:
                        mismatch = True
                        position = i
                i += 1
            if mismatch == True:
                answer = True
                print("string1 : " + str(string1))
                print("string2 : " + str(string2))
                print("answer  : " + string1[:position] + string1[position+1:])

        string2_iter += 1
    
    string1_iter += 1


def StringSplit(stream):
    return iter(stream.splitlines())