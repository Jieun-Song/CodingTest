
for i in range(int(input())):
  myList = list(input().split(" "))
  myInt = int(myList[0])
  myStr = ""
  for i in range(len(myList[1])):
    myStr += myList[1][i]*myInt
  print(myStr)
