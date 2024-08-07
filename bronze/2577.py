num1 = int(input())
num2 = int(input())
num3 = int(input())

myNum = str(num1*num2*num3)
myDic = {}
for j in range(10):
  myDic[str(j)] = 0

for i in myNum:
  myDic[i] +=1 

for j in range(10):
  print(myDic[str(j)])