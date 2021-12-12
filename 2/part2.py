data = open("input.txt", "r").read().split("\n")

def main(data):
    x = 0
    y = 0
    aim = 0
    for it in data:
        splitted = it.split(" ")
        dir = splitted[0]
        steps = int(splitted[1])
        if dir == "forward":
            x += steps
            y += aim*steps
        elif dir == "down":
            aim += steps
        elif dir == "up":
            aim -= steps
    return x*y

print(main(data))