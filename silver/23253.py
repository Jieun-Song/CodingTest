# # n, m = map(int, input().split())

# # lists = []

# # for _ in range(m):
# #     booksOnPile = int(input())
# #     lists.append(list(map(int, input().split())))

# # num = 1
# # for _ in range(n):
# #     for list in lists:
# #         if list and list[-1] == num:
# #             list.pop()
# #             num +=1
# #             break
# #     else:
# #         print("No")
# #         exit()
# # print("Yes")


# import sys
# from collections import deque

# # 입력 처리
# input = sys.stdin.read
# data = input().split()
# N, M = map(int, data[:2])

# # 더미 정보 읽기
# piles = []
# index = 2
# for _ in range(M):
#     k = int(data[index])
#     index += 1
#     piles.append(deque(map(int, data[index:index + k])))
#     index += k

# # 순서대로 꺼낼 수 있는지 확인
# current_num = 1
# while current_num <= N:
#     found = False
#     for pile in piles:
#         if pile and pile[-1] == current_num:
#             pile.pop()
#             current_num += 1
#             found = True
#             break
#     if not found:
#         print("No")
#         sys.exit()

# print("Yes")


# 결국 그냥 내림차순으로 되어있는지 확인하는 문제였다. 아하!

n, m = map(int, input().split())

lists = []

for _ in range(m):
    booksOnPile = int(input())
    a = list(map(int, input().split()))
    if a != sorted(a, reverse=True):
        print("No")
        exit()
print("Yes")