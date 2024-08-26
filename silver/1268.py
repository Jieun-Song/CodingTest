# #가장 공통되는 반이 많은 어린이 뽑기.

# biggest = 0
# bigOne = 0
# num = []
# stNum = int(input())
# dic =[[0 for row in range(6)] for col in range(stNum)]

# #저장
# for i in range(0, stNum):
#   dic[i][0], dic[i][1], dic[i][2], dic[i][3], dic[i][4] = input().split()

# #비교
# for i in range(0, stNum):
#   myList = []

#   for grade in range(0,5):
#     #열 리스트 만들기
#     myList.append(dic[i][grade])
  
#   newDic = myList[:]

#   for j in list(set(myList)):
#     newDic.remove(j)
    
#   num += newDic

#   for n in num:
#     # 뽑아낸 숫자들에 대해서.. 
#     if n in dic[i]:
#       #뽑아낸 숫자들에 이게 있으면
#       dic[i][5] += 1
      
#   if dic[i][5] > biggest :
#     biggest = dic[i][5]
#     bigOne = i+1

# print(bigOne)

# 아래는 gpt

biggest = 0
bigOne = 0
stNum = int(input())
dic = [list(map(int, input().split())) for _ in range(stNum)]

# 비교
for i in range(stNum):
    count = 0  # 같은 반이었던 학생 수를 셀 변수
    
    for j in range(stNum):
        if i != j:  # 자기 자신과 비교할 필요 없음
            for grade in range(5):
                if dic[i][grade] == dic[j][grade]:
                    count += 1
                    break  # 한 학년이라도 같은 반이었다면 더 이상 비교할 필요 없음
    
    if count > biggest:
        biggest = count
        bigOne = i + 1  # 학생 번호는 1번부터 시작
    elif count == biggest:
        bigOne = min(bigOne, i + 1)

print(bigOne)
