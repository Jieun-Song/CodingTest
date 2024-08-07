#  서쪽에 N개, 동쪽에 M개(N<=M)
#  다리의 갯수는 최대 N개 (0 < N ≤ M < 30)
#  겹쳐지기 안됨
# 경우의 수

def factorial(num):
    result = num
    if num == 0 or num ==1:
        return 1
    a = num - 1
    while a > 0:
        result = result * (num-a)
        a -= 1
    return result

a = int(input())
for i in range(0,a):
    m, n = input().split(" ")
    m,n = int(m), int(n)
    
    facN = factorial(n)
    facM = factorial(m)
    facN_M = factorial(n-m)
    
    result = facN // (facM*facN_M)
    
    print(result)
    

