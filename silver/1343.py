# AAAA BB

def listSplit(list):
  result = []
  for i in list :
    if i != "":
      result.append(i)
  return result

try:
  # .으로 나눈 문자열들이 짝수 문자열이어야함
  # .으로 나눈 문자열을 4로 먼저 나누고 나머지가 2이면 가능.
  list = listSplit(input().split("."))

  for i in list:
    fourTime = len(i) // 4
    left = len(i) % 4
    if left % 2 == 1:
      raise EOFError
    print
except:
  print(-1)


# 해야할 것
# .의 갯수들 구하기(결과 출력용)
# 적절한 error를 raise하기
# 출력하기