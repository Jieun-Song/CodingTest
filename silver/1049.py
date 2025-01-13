broken, brands = map(int, input().split())
sets = []
ones = []

for _ in range(brands):
    set, one = map(int, input().split())
    sets.append(set)
    ones.append(one)

setn = broken//6
leftn = broken % 6

combo = setn * min(sets) + leftn * min(ones)
if leftn != 0 :
    setn = setn + 1

onlySet = setn * min(sets)
onlyOne = broken * min(ones)
# print(combo, onlySet, onlyOne)
print(min(combo, onlySet, onlyOne))