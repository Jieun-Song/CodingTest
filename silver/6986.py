# from decimal import *

# n,k = map(int, input().split())
# scores = []

# for _ in range(n):
#     scores.append(float(input()))

# sorted_score = sorted(scores)
# jul = sorted_score[2:-2]
# jul_mean = sum(jul)/len(jul)

# sorted_score[0:2] = sorted_score[2],sorted_score[2]
# sorted_score[-2:] = sorted_score[-3],sorted_score[-3]
# bo = sum(sorted_score)/len(sorted_score)

# print("{:.2f}".format(int(Decimal(jul_mean)*1000)/1000 + 0.00000001))
# print("{:.2f}".format(int(Decimal(bo)*1000)/1000 + 0.00000001))

from decimal import *

n, k = map(int, input().split())
scores = []

for _ in range(n):
    scores.append(float(input()))

sorted_score = sorted(scores)
jul = sorted_score[2:-2]
jul_mean = sum(jul) / len(jul)

sorted_score[0:2] = sorted_score[2], sorted_score[2]
sorted_score[-2:] = sorted_score[-3], sorted_score[-3]
bo = sum(sorted_score) / len(sorted_score)

# 주어진 소수점 자리에 맞춰 Decimal로 포매팅
jul_mean_decimal = Decimal(jul_mean).quantize(Decimal('0.00'))
bo_decimal = Decimal(bo).quantize(Decimal('0.00'))

# 출력
print(f"{jul_mean_decimal:.2f}")
print(f"{bo_decimal:.2f}")
