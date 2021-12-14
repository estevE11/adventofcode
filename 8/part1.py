data = open("input.txt", "r").read().split("\n")

count = 0

for it in data:
    out = it.split(" | ")[1]
    digits = out.split(" ")
    print(digits)
    for d in digits:
        if len(d) == 2 or  len(d) == 3 or len(d) == 4 or len(d) == 7:
            count += 1

print(count)
