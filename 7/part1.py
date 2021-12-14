data = open("input.txt", "r").read().split("\n")
data = list(map(lambda x : int(x), data[0].split(",")))

def calc_fuel(list, pos):
    count = 0
    for it in list:
        count += abs(pos - it)
    return count


hi = -1
for it in data:
    hi = max(it, hi)

lo_fuel = 999999
lo_idx = -1
for i in range(hi):
    fuel = calc_fuel(data, i)
    if fuel < lo_fuel:
        lo_fuel = fuel
        lo_idx = i

print(lo_fuel)