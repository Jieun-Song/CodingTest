##지그재그
#총 448층
# 짝수층은 위로
# 홀수증은 아래로 감

num = int(input())
floor = 0

while True:
  floor += 1
  # 몇층인지/해당 층에 몇개가 있는지
  # print(floor,"층입니다.")
  # num은 방금들어온 수... 찾고있는 위치
  if (num-floor)<=0:
    #찾고있는 위치가 있는 층에 도달함
    # print(num,"개 더가야합니다.")
    break
  num -= floor

if (floor % 2 == 0):
  #짝수층..
  firstNum = floor - (floor - num)
  LastNum = floor - (num -1)
  print(str(firstNum)+"/"+str(LastNum))
else :
  firstNum = floor - (num-1)
  LastNum = floor - (floor-num)
  print(str(firstNum)+"/"+str(LastNum))