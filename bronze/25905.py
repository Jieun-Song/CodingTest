'''
주어진 10개의 망치중 9개를 선택해 강화
i번째 망치는 pi의 확률로 강화성공, 차수 높임
9강에 도달할 확률의 최댓값

x강으로의 강화를 i번 망치로 진행할 때 pi/x

입력
10개의 줄에 걸쳐 i번째 줄에 pi가 주어진다.
( 0< pi<=1; pi는 최대 소수 둘째 자리까지 주어짐 )

출력
강화 최대치로 도달할 확률의 최댓값에 10**9를 곱한 값 출력

처음엔 DP로 만들다가,, 잘 안되더라,, 결국 시간이 너무 많이 걸리길래 걍 지피티 돌림
'''
# import math
# list = []
# result = 1
# # 일단 행렬을 만듦 (동적 프로그래밍)
# for i in range(9):
#     list.append(float(input()))

# list.sort()
# for j in list[:-1]:
#     result = result * j

# print(result / math.factorial(9) * 10**9)

'''
gpt가 만들어준 코드
문제 내용을 그대로 만들음
기억하면 좋을것 
itertools.. combinations(), permutations()

combinations(list, 9) : list에서 9개를 뽑아 조합만듦 
permutations(list) : list를 가지고 순열 만듦
https://seu11ee.tistory.com/5
'''


import itertools

def max_enhance_probability(probabilities):
    n = 10  # 총 10개의 강화망치
    max_probability = 0

    # 가능한 모든 9개의 망치 선택 조합
    for combination in itertools.combinations(probabilities, 9):
        # 강화 순서에 따른 확률 계산
        for perm in itertools.permutations(combination):
            current_probability = 1
            for x, p_i in enumerate(perm, start=1):
                current_probability *= p_i / x
            max_probability = max(max_probability, current_probability)

    return max_probability

# 입력 처리
probabilities = [float(input().strip()) for _ in range(10)]

# 최대 확률 계산
result = max_enhance_probability(probabilities)

# 결과 출력
print(f"{result * 10**9:.6f}")

