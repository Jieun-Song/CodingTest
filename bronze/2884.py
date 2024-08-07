myHour, myMin = list(map(int,input().split(" ")))
myMin -= 45
if myMin < 0:
  myHour -= 1
  myMin += 60
  if myHour<0:
    myHour = 23

print(myHour, myMin)