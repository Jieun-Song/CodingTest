n = int(input())
aps = []
suns = {}

for _ in range(n):
    ap_line = input().split()
    aps.append([ap_line[0]]+list(map(int, ap_line[1:])))

for _ in range(n):
    sun_line = input().split()
    suns[sun_line[0]] = int(sun_line[1])

cal = [[0 for j in range(7)] for i in range(11)]

for i in range(n):
    if suns[aps[i][0]] >= aps[i][3]:
        cal[aps[i][1]][aps[i][2]] = 1

date = 0
max = 0
for w in cal:
    for d in w:
        if d != 0:
            date += 1
            if date > max:
                max = date
        if d == 0:
            date = 0

print(max)