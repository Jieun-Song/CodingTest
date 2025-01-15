stNum = int(input())
sts = {}
stList = list(input().split(" "))

for st in stList:
    sts[st] = 0

for _ in range(stNum):
    preferList = list(input().split(" "))
    for i in preferList:
        sts[i] += 1

result = []
for i in list(sts.keys()):
    result.append((i, sts[i]))
result = sorted(result, key = lambda x : x[1], reverse=True)
for n in result:
    print(*n)
