myList = list(map(int, input().split(" ")))
flag = True

if myList[0]>myList[1]:
  des = True
elif myList[0]<myList[1]:
  des = False

if des:
  for i in range(len(myList)-1):
    if myList[i]<myList[i+1]:
      flag=False
      
else:
  for i in range(len(myList)-1):
    if myList[i]>myList[i+1]:
      flag = False

if des and flag:
  print("descending")
elif not des and flag:
  print("ascending")
elif not flag:
  print("mixed")