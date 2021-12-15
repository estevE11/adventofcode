data = open("input.txt", "r").read().split("\n")

for i, it in enumerate(data):
    data[i] = list(map(lambda x: int(x), it))

def print_state():
    for i, it in enumerate(data):
        print(data[i])

def inc(x, y, flashed):
    global flashes

    if x < 0 or x > len(data[0]) - 1 or y < 0 or y > len(data) - 1 or (str(x) + "," + str(y)) in flashed:
        return flashed

    data[y][x] += 1
    if data[y][x] > 9:
        flashed = flash(x, y, flashed)
    return flashed

def flash(x, y, flashed):
    global flashes

    if (str(x) + "," + str(y)) in flashed:
        return flashed

    data[y][x] = 0
    flashes += 1

    flashed[str(x) + "," + str(y)] = 1

    for yy in range(y-1, y+2):
        for xx in range(x - 1, x + 2):
            if not (xx == x and yy == y):
                flashed = inc(xx, yy, flashed)

    return flashed

flashes = 0

for i in range(100):
    flashed = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            flashed = inc(x, y, flashed)
    print("after step " + str(i + 1))
    print_state()
    print("")

print(flashes)