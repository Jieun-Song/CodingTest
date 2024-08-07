# 몇개가 추가로 주어져야하는지 출력

myChess = list(map(int, input().split()))
defChess = [1, 1, 2, 2, 2, 8]
result = []

for i in range(6):
  result.append(defChess[i] - myChess[i])

print(*result)