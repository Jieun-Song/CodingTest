# num = int(input())
# listA = input().split(" ")
# listB = listA.copy()
# listB.sort()
# listP = []
# n = len(listA)

# for i in range(0, n):
#     for j in range(0, n):
#         if (listA[i] == listB[j]) and (j not in listP):
#             listP.append(j)
#             break

# print(*listP)

'''
위는 시간이 n제곱으로 너무 오래걸림..
지피티가 만들어준 코드는 아래
nlogn
'''
num = int(input())
listA = list(map(int, input().split()))

# A의 각 원소의 (인덱스, 값)을 저장
indexed_A = list(enumerate(listA))

# 값을 기준으로 정렬
indexed_A.sort(key=lambda x: x[1])

# P 배열을 생성
listP = [0] * num
for new_idx, (original_idx, _) in enumerate(indexed_A):
    listP[original_idx] = new_idx

print(*listP)
