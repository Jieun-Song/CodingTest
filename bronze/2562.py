myList = []
while True:
  try:
    myList.append(int(input()))
  except:
    break
print(max(myList))
print(myList.index(max(myList))+1)