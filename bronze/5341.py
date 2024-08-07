while True:
  a = int(input())
  if a == 0:
    break
  result = 0
  for i in range(a):
    result += i+1
  print(result)
