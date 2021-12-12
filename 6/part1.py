data = open("input.txt", "r").read().split("\n")
data = list(map(lambda x : int(x), data[0].split(",")))

for j in range(256):
    print(j)
    for i, it in enumerate(data):
        if it == 0:
            data[i] = 6
            data.append(9)
        else:
            data[i] = it - 1
print(len(data))