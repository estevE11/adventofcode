data = open("input.txt", "r").read().split("\n")

def main(data):
    epsilon = ""
    gamma = ""
    counts = [0]*len(data[0])
    for it in data:
        for i, bit in enumerate(it):
            if int(bit) == 0:
                counts[i] += 1
    for count in counts:
        if count > len(data)/2:
            epsilon += "1"
            gamma += "0"
        else:
            epsilon += "0"
            gamma += "1"
    return int(epsilon, 2)*int(gamma, 2)

print(main(data))