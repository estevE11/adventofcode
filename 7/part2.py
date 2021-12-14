data = open("input.txt", "r").read().split("\n")

data = open("input.txt", "r").read().split("\n")
data = list(map(lambda x : int(x), data[0].split(",")))

def calc_fuel(list, pos):
    count = 0
    for it in list:
        d = abs(pos - it)
        count += (d * (d + 1)) / 2
    return count


hi = -1
for it in data:
    hi = max(it, hi)

lo_fuel = 9999999999999
lo_idx = -1
for i in range(hi):
    print("calc", i, "of", hi, int(i/hi*100), "%")
    fuel = calc_fuel(data, i)
    print(fuel)
    if fuel < lo_fuel:
        lo_fuel = fuel
        lo_idx = i

print(lo_fuel)