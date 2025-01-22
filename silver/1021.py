# 1번기능 pop
# popped.append(myList.pop(0))

# 2번기능 첫번째꺼 맨 뒤로
def secondF(myList):
    firstOne = myList.pop(0)
    myList = myList + [firstOne]
    # print("secondF", myList)
    return myList

# 3번째 기능 맨뒤꺼 맨 앞으로
def thirdF(myList):
    lastOne = myList.pop()
    myList = [lastOne] + myList
    # print("thirdF", myList)
    return myList

def doit(myList, type, wanted):
    num = 0
    firstOne = myList[0]
    while wanted != firstOne:
        if type == 2:
            myList = secondF(myList)
        elif type == 3:
            myList = thirdF(myList)
        num = num + 1
        firstOne = myList[0]
    return myList, num

n, _ = map(int, input().split())
myList = list(range(1, n+1))
wantedList = list(map(int, input().split()))
popped = []
result = 0
# print(myList)

for wanted in wantedList:
    # print(wanted)
    sampleList = myList[:]
    myList_2, num_2 = doit(sampleList, 2, wanted)
    myList_3, num_3 = doit(myList, 3, wanted)
    # print(num_2, num_3, myList)
    if num_2>num_3:
        myList = myList_3
        result = result + num_3
    else:
        myList = myList_2
        result = result + num_2
    popped.append(myList.pop(0))
    # print(result, myList)
print(result)


# 1. wantedList에서 원하는거가 나올때까지(==) 반복해서 각각 2번과 3을 수행
# 2. 그 숫자를 비교해서 적은걸 저장
# 3. 반복..
# 4. 첫번째숫자가 ==이면 pop