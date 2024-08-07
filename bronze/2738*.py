n,m =map(int, input().split())
listA = []
listB = []

for i in range(n):
  listA.append(list(map(int,input().split())))
for i in range(n):
  listB.append(list(map(int,input().split())))

cnt =[]
for i in range(n):
  for o in range(m):
    cnt.append(listA[i][o]+listB[i][o])

for i in range(n):
  print(*cnt[:m]) 
  # print(*리스트명) < 리스트 안에 있는 요소들을 꺼내서 출력
  del cnt[:m]

