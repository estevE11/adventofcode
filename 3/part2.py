data = open("input.txt", "r").read().split("\n")

def main(data):
    col = 0
    oxygen = data.copy()
    #while len(oxygen) > 0:
    count = 0
    for it in oxygen:
        bit = it[col]
        if bit == 1:
            count += 1
    to_delete = 0
    if count > len(data)/2:
        to_delete = 1
    for i, it in enumerate(oxygen):
        bit = int(it[col])
        print(bit)
        if bit == to_delete:
            del oxygen[i]
    return oxygen

main(data)