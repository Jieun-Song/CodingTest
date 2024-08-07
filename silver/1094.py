# 1. 가지고 있는 막대들 중 길이가 가장 짧은 것을 절반으로 자른다
#  (처음엔 64cm -> 32cm)
# 2. if X>=32 , throw one of 32
# 3. 32

x = int(input())

stick = 64
total = stick
num = 1

while (total > x):
  half = stick//2
  num +=1
  if total-half>=x:
    total -= half
    num -=1
  stick = half

print(num)