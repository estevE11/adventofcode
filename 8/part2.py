data = open("input.txt", "r").read().split("\n")

# acedgfb: 8x
# cdfeb:   5
# acdeg:   2
# abcdf:   3
# dab:     7x
# abcdfg:  9x
# abdefg:  6x
# eafb:    4x
# abcefg:  0x
# cf:      1x

count = 0

def get_number(digit):
    if len(d) == 2:
        return 1
    elif len(d) == 3:
        return 7
    elif len(d) == 4:
        return 4
    elif len(d) == 7:
        return 8
    elif len(d) == 6:
        if "c" in d and "e" in d:
            return 9
        elif "c" in d:
            return 0
        else:
            return 6
    elif len(d) == 5:
        if "e" not in d:
            return 3
        elif "g" in d:
            return 2
        else:
            return 5
    
count = 0
for it in data:
    out = it.split(" | ")[1]
    digits = out.split(" ")
    curr = ""
    
    for d in digits:
        num = get_number(d)
        print(d, num)
        curr += str(num)
    print()
    print(curr)
    print()
    print()
    count += int(curr)
        

print(count)
