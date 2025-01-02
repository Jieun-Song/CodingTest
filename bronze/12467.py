'''
N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성해라

3개의 테스트셋, 

'''

for i in range(3):
    rep = int(input())
    sum = 0
    for j in range(rep):
        sum = sum + int(input())
    if sum == 0:
        print(0)
    elif sum>0:
        print('+')
    elif sum<0 :
        print('-')