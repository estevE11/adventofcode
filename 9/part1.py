data = open("input.txt", "r").read().split("\n")

def get_num(x, y):
    if x < 0 or x > len(data[0])-1 or y < 0 or y > len(data)-1:
        return 99
    return int(data[y][x])

count = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        hole = True
        curr = get_num(x, y)
        if get_num(x-1, y) <= curr:
            hole = False
        elif get_num(x+1, y) <= curr:
            hole = False
        elif get_num(x, y-1) <= curr:
            hole = False
        elif get_num(x, y+1) <= curr:
            hole = False
        if hole:
            count += 1+curr
            print(curr)

print(count)

