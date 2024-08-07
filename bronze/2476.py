a = input().split(" ")
result = 0
for i in a:
  result += int(i)*int(i)
print(result%10)