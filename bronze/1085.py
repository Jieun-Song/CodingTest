# 직사각형의 경계선 까지 가는 거리의 최솟값을 구해라
'''
한수의 위치 : x,y
오른쪽 위 꼭짓점 : w,h
입력 x,y,w,h
'''
# 경계선까지 가는거니까 꼭짓점에서 얼마나 떨어져있는지를 구하고, 가장 최솟갑을 출력

x,y,w,h = map(int, input().split(" "))
minimal = min(x,y,(h-y),(w-x))
print(minimal)

