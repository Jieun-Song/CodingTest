myStr = input().upper()
myDic = {}

for i in myStr:
  if i in myDic:
    myDic[i] += 1
  else:
    myDic[i] = 1

result = []
values = myDic.values()

for j in list(myDic.keys()):
  if myDic[j] == max(values):
    result.append(j)

if len(result)>1:
  print("?")
elif len(result) == 1:
  print(*result)
else :
  print("error")

# 