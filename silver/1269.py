# _ =  input()
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# setAB = a+b
# doubleAB = setAB[:]
# for i in set(setAB):
#     doubleAB.remove(i)
# setAB = list(set(setAB) - set(doubleAB))
# print(len(setAB))

# GPT코드
from collections import Counter

_, _ = map(int, input().split())  # 두 집합 크기는 사용되지 않음
a = map(int, input().split())
b = map(int, input().split())

counter = Counter(a) + Counter(b)  # 두 리스트를 합쳐 Counter로 중복을 셈
result = [num for num, count in counter.items() if count == 1]  # 한 번만 등장한 숫자 추출
print(len(result))
