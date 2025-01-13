# def stick(a,b):
#     more_stick = 0
#     while a*4 < b:
#         a += 1
#         more_leaf += 1
#     return a, b, more_stick
#     #단점 : 한번에 얼마나 필요한지 계산 못함.

# def leaf(a,b):
#     more_leaf = 0
#     while a**3 > b:
#         b += 1
#         more_leaf += 1
#     return a, b, more_leaf
#     # 단점 : 위 문제와 같음

# def can(a,b):
#     # 4와 3을 이용해 b를 조합할수있는가?
#     for i in range(a+1):
#         if (4*(a-i)+3*i == b):
#             return True
#     return False
#     #범위가 클경우 비효율적

# n = int(input())
# list = []

# for _ in range(n):
#     a,b = map(int,input().split())
#     list.append((a,b))

# more = 0
# for i in list:
#     a, b, m = stick(a,b)
#     more += m
#     a, b, m = leaf(a,b)
#     more += m
#     flag = False
#     while flag != True:
#         can(a,b)
#         b += 1
#         more +=1
#     print(more)


# 함수 정의 및 테스트 입력
def solve_clover(a, b):
    min_leaves = 3 * a  # 최소 필요 잎 개수
    max_leaves = 4 * a  # 최대 필요 잎 개수

    # 잎이 부족한 경우
    if b < min_leaves:
        return min_leaves - b

    # 잎이 많은 경우
    if b > max_leaves:
        extra_stems = (b - max_leaves + 2) // 3  # 초과분 보정하는 줄기 수 계산
        return extra_stems + (extra_stems * 3 + max_leaves - b)

    # 조합 가능한 경우 확인
    # 주어진 잎이 충분히 많다면 줄기를 최대 3잎 또는 4잎으로 사용
    # 이 경우 추가가 필요 없다
    if (b - 3 * a) % 3 == 0 or (b - 4 * a) >= 0:
        return 0

    # 기타 추가 보정 필요
    return 0


n = int(input())
list = []

for _ in range(n):
    a,b = map(int,input().split())
    list.append((a,b))


# 결과 출력
results = [solve_clover(a, b) for a, b in list]
for i in results:
    print(i)

