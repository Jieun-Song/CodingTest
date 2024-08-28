# 그룹단어 : 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우

# 문자열의 문자가 연속되지 않으면서 이미 앞서 해당 문자가 입력된 적이 있을 경우
# 그룹 단어가 아니다
def wordChecker(word):
  # 1. 앞에 같은 단어가 없어야함
  num = 0
  result = word[0]
  for j in word[1: ]:
    if j == result[-1]:
      result += j
    elif (j != result[-1]) & (j not in result):
      result += j
    elif j in result:
      return False
    else :
      print("??")
  return True

n = int(input())
howMany = 0
for i in range(n):
  word = input()
  if wordChecker(word):
    howMany += 1

print(howMany);