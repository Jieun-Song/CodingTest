# 양의 정수 N이 주어졌을 때, 이 수를 서로 다른 정수 M개의 팩토리얼 합으로
# 나타낼수 있을지 알아내는 프로그램 작성
# 예를 들어 2=0!+1!로 나타낼 수 있지만, 5는 이와 같은 방식으로 나타낼 수 없다.

# input = int(input())

# 1. 인풋받은 정수보다 작은 최대의 팩토리얼 구함
#   빼고, 남은 것을 가지고 최대의 팩토리얼 

# n!계산
# def factorial_recursive(n):
#     return n * factorial_recursive(n-1) if n>1 else 1

# def 


# def find_out(inputNum):
#     for i in range(0,20):
#         if factorial_recursive(i) > inputNum:
#             print(i-1)
#             print(factorial_recursive(i-1))
#             break
#     return find_out(input - factorial_recursive(i-1))

# find_out(input)

"""
내 풀이방법
- 주어진 수를 기준으로 뺄수있는 가장 큰 팩토리얼을 찾는다
- 찾은 팩토리얼을 빼고, 계속해서 뺄수있는 가장 큰 팩토리얼을 찾는다.

지피티의 풀이방법
- 입력받은 n을 기준... 1~n까지의 팩토리얼 값을 구함.(리스트로 저장해둠)
- 그리디 알고리즘 이용.. (N보다 작은것중 가장큰 팩토리얼 값을 찾아 N에서 뺌)
- 이때 중복된 팩토리얼 값 제외
- 남은게 0이면 가능, 아니면 불가능.

"""

def factorial_upto_n(n):
    """n 이하의 모든 팩토리얼 값을 계산"""
    factorials = []
    fact = 1
    i = 1
    while fact <= n:
        factorials.append(fact)
        fact *= i
        i += 1
    return factorials[::-1]  # 큰 값부터 작은 값으로 반환


def can_represent_as_factorial_sum(n):
    """n을 서로 다른 정수의 팩토리얼 합으로 나타낼 수 있는지 확인"""
    if n == 0:
        return True

    factorials = factorial_upto_n(n)
    for fact in factorials:
        if n >= fact:
            n -= fact

    return n == 0

# 테스트
n = int(input())
if n == 0:
    print("NO")
elif can_represent_as_factorial_sum(n):
    print("YES")
else :
    print("NO")

