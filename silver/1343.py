# AAAA BB

def listSplit(list):
  #문자열끼리 더하고 append하고, *끼리 더하고 append하고

  result = []
  appendString = ""
  
  for i in list :
    if i == "*":
      stars = stars + i
    else :

  result.append(i)
  print(result)
  return result

try:
  # .으로 나눈 문자열들이 짝수 문자열이어야함
  # .으로 나눈 문자열을 4로 먼저 나누고 나머지가 2이면 가능.
  list = listSplit(input().split())

  for i in list:
    fourTime = len(i) // 4
    left = len(i) % 4
    if left % 2 == 1:
      raise ValueError
    
except:
  print(-1)


# 해야할 것
# 출력하기