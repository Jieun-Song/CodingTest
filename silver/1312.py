
#numerator : 분자, denominator : 분모
# try:
#   print(str(num/denom).split(".")[1][loc-1])
# except:
#   print("error")



# 부동소수점때문에 안된다는데 부동소수점이라는걸 이해중이엇음
# 부동소수점이란 ?  실수를 컴퓨터상에서 근사하여 표현할 떄 소수점의 위치를 고정하지않고
# 그 위치를 나타내는 수를 따로 적는 것으로, 유효숫자를 나타내는 가수와 소수점의 위치를 

# 구글링 결과

# 단순 파이썬을 이용해 문자열 변환하는 것보단,,
# 소수점 15자리까지만 표시되니까 수학적 원리로 접근해서 풀어야한다.

num, denom, loc = map(int, input().split(" "))

for i in range(loc) :
  num = (num%denom)*10
  result = num//denom

print(result)