data = open("input.txt", "r").read().split("\n")

def count_increases(input):
    count = 0
    prev = 0
    for i in range(len(input)-2):
        curr = 0
        for it_ in range(i, i + 3):
            curr += int(input[it_])
        if prev != 0:
            if curr > prev:
                count += 1
        prev = curr
    return count

print(count_increases(data))