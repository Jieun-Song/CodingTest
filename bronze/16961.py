'''
탭파 vs 공백파
윤년 - 366 1일~366일
예약한 사람 N명
투숙시작일(9시)/종료일(18)

탭파와 공백파가 만나면 싸우나 수가 일치하면 안싸운다.
각각이 한명도 없으면 안된다.

입력
예약한 수N
c(어느파),s(투숙시작일),e(투숙 종료일)

출력
1. 투숙객이 있었던 날의 수
2. 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
3. 싸움이 없는 날의 수
4. 안싸운날 가장 많은 투숙객이 있었던 날에 투숙한 사람 수
5. 가장 오랜 기간 투숙한 사람이 투숙한 날의 수
'''
visitors = []
for i in range(int(input())):
    visitor = input().split(" ")
    visitor[1],visitor[2] = map(int, [visitor[1],visitor[2]])
    visitors.append(visitor)
# print(visitors)

# 투숙객이 1명 이상인 날의 수
s1 = set([])
for visitor in visitors:
    s1 = s1 | set([*range(visitor[1],visitor[2]+1)])
print(len(s1))

# 가장 많은 투숙객이 있었던 날에 투숙한 사람의 수
count = {}
for visitor in visitors:
    s2 = set([])
    s2.update([*range(visitor[1],visitor[2]+1)])
    for i in s2:
        try: count[i] = count[i] + 1
        except: count[i]=1
print(max(count.values()))

# 싸움이 없는 날의 수
countT = {}
countS = {}
for visitor in visitors:
    s2 = set([])
    s2.update([*range(visitor[1],visitor[2]+1)])
    if visitor[0] == "T":
        for i in s2:
            try: countT[i] = countT[i] + 1
            except: countT[i] = 1
    else:
        for i in s2:
            try: countS[i] = countS[i] + 1
            except: countS[i] = 1
result = 0
result4 = []
for d in countS.keys():
    try :
        if countS[d] == countT[d]:
            result4.append(countS[d]+countT[d])
            result += 1
    except : 
        continue
print(result)
print(max(result4))

# 가장 오래 투숙한 사람
max = 0
for visitor in visitors:
    if max<(visitor[2]-visitor[1]):
        max = visitor[2]-visitor[1]
print(max+1)