import threading

data = open("input.txt", "r").read().split("\n")
data = list(map(lambda x : int(x), data[0].split(",")))

fish = [0]*9

for i, it in enumerate(data):
    fish[it] += 1


for j in range(256):
    old_fish = fish.copy()
    for i, it in reversed(list(enumerate(fish))):
        if i == 0:
            fish[8] = old_fish[0]
            fish[6] += old_fish[0]
        else:
            fish[i-1] = old_fish[i]

count = 0
for it in fish:
    count += it
print(count)
