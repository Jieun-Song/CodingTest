# def change(list, a, b):
#     temp = list[a]
#     list[a] = list[b]
#     list[b] = temp

# listA = []
# listB = []
# for i in range(int(input())):
#     w,h = map(int, input().split())
#     listA.append(w**2+h**2)
#     listB.append(i)

# for n in range(len(listA)):
#     biggestA = -1
#     biggestB = -1
#     for m in range(n, len(listA)):
#         if listA[m] > biggestA:
#             biggestA = listA[m]
#             biggestB = m
#     change(listA, n, biggestB)
#     change(listB, n, biggestB)

# for k in listB:
#     print(k+1)

# 지피티가 짜준 코드

# 입력값 받기
points = []
for i in range(int(input())):
    w, h = map(int, input().split())
    distance = w**2 + h**2
    points.append((distance, i + 1))  # (거리, 1부터 시작하는 인덱스)

# 거리 기준 내림차순 정렬
sorted_points = sorted(points, key=lambda x: x[0], reverse=True)

# 결과 출력
for _, index in sorted_points:
    print(index)


