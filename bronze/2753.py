myNum = int(input());
if myNum % 4 == 0:
  if myNum % 400 == 0:
    flag = 1
  else:
    flag =0
    if myNum % 100 != 0:
      flag = 1
else :
  flag = 0

print(flag)

# 1. 4의 배수일것
# 2. 100의 배수가 아닐것
# 3. 400의 배수일 때