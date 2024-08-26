num, denom, loc = map(int, input().split(" "))
#numerator : 분자, denominator : 분모
try:
  print(str(num/denom).split(".")[1][loc-1])
except:
  print("error")



# 부동소수점때문에 안된다는데 부동소수점이라는걸 이해중이엇음