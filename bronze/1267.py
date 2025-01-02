''' 두가지 요금제
1. 30초에 10원씩 (29~0)
2. 60초에 15원씩 (59~0)
기존에 전화한걸 가지고 어느 요금제가 더 나을지(저렴할지)

입력
전에 이용한 통화의 개수 N
각 통화의 길이들

출력
싼 요금제의 이름, 요금이 몇원 나오는지.
'''
def getPrice(charge, time):
    telecom = {10:30, 15:60}.get(charge, "?")
    count = time // telecom
    left = time % telecom
    if left >= 0:
        count = count + 1
    return count * charge

num = int(input())
list = map(int,input().split(" "))
ySum = 0
mSum = 0
for i in list:
    ySum = ySum+ getPrice(10, i)
    mSum = mSum+ getPrice(15, i)

if ySum < mSum:
    print("Y", ySum)
elif ySum == mSum:
    print("Y","M",ySum)
elif ySum > mSum:
    print("M",mSum)