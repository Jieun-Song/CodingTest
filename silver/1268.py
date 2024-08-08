#가장 공통되는 반이 많은 어린이 뽑기.

stNum = int(input())
dic =[[0 for row in range(6)] for col in range(stNum)]

for i in range(0, stNum):
  dic[i][0], dic[i][1], dic[i][2], dic[i][3], dic[i][4] = input().split()

# 표 저장 완료. 이제 비교해서 누가 반장할지만 구하면 됨