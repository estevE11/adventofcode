data = open("input.txt", "r").read().split("\n")

positions = {}
count = 0

for i, it in enumerate(data):
    parsed = it.split(" -> ")
    start = list(map(lambda x : int(x), parsed[0].split(",")))
    end = list(map(lambda x : int(x), parsed[1].split(",")))
    pos_idx = 0
    if start[0] == end[0]:
        pos_idx = 1
    elif start[1] == end[1]:
        pos_idx = 0
    else:
        continue
    pos = start[pos_idx]
    while pos != end[pos_idx]:
        key = ""
        if pos_idx == 0:
            key = str(pos) + "," + str(start[not bool(pos_idx)])
        else:
            key = str(start[not bool(pos_idx)]) + "," + str(pos)
        #print(key)
        if key in positions:
            positions[key] += 1
            if positions[key] == 2:
                count += 1
        else:
            positions[key] = 1
        #print(key, positions[key])
        if pos < end[pos_idx]:
            pos += 1
        else:
            pos -= 1
    key = ""
    if pos_idx == 0:
        key = str(pos) + "," + str(start[not bool(pos_idx)])
    else:
        key = str(start[not bool(pos_idx)]) + "," + str(pos)
    if key in positions:
        positions[key] += 1
        if positions[key] == 2:
            count += 1
    else:
        positions[key] = 1
    #print(key, positions[key])
print(count)    