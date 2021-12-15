data = open("input.txt", "r").read().split("\n")

# 0. ):  3 points.
# 1. ]: 57 points.
# 2. }: 1197 points.
# 3. >: 25137 points.

score_val = [3, 57, 1197, 25137]

starting = "([{<"
ending = ")]}>"

def my_eval(s):
    started = ""
    for c in s:
        if c in starting:
            started += c
        else:
            if starting.find(started[-1]) == ending.find(c):
                started = started[:-1]
            else:
                return c
        

res = 0

for it in data:
    val = my_eval(it)
    if val != None:
        res += score_val[ending.find(val)]

print(res)