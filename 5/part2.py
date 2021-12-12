data = open("input.txt", "r").read().split("\n")

positions = {}
count = 0

for i, it in enumerate(data):
    parsed = it.split(" -> ")
    start = list(map(lambda x : int(x), parsed[0].split(",")))
    end = list(map(lambda x : int(x), parsed[1].split(",")))

    x,y = start[0],start[1]

    #print(" ")
    while x != end[0] or y != end[1]:
        key = str(x) + "," + str(y)
        if key in positions:
            positions[key] += 1
            if positions[key] == 2:
                count += 1
        else:
            positions[key] = 1
        #print(key, positions[key])
        if x != end[0]:
            if x > end[0]:
                x -= 1
            else:
                x += 1
        if y != end[1]:
            if y > end[1]:
                y -= 1
            else:
                y += 1
    key = str(x) + "," + str(y)
    if key in positions:
        positions[key] += 1
        if positions[key] == 2:
            count += 1
    else:
        positions[key] = 1
    #print(key, positions[key])
print(count)
