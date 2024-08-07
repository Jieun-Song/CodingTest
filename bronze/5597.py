# 1부터 30번까지 있는 리스트를 생성하고, 있는 사람을 없애는 방법으로
# 숫자를 남긴 다음에 남은 숫자를 출력하자
myList =[]

for i in range(30):
  myList.append(i+1)

for j in range(28):
  a = int(input())
  myList.remove(a)

for l in myList:
  print(l)
