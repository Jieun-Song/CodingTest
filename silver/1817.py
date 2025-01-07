bookN, boxN = map(int, input().split())
if bookN == 0:
    print(0)
else :
    books = list(map(int, input().split()))

    num = 0
    boxes = 0
    sum = 0

    while (num < bookN):
        sum += books[num]
        num += 1
        if (sum > boxN):
            sum = 0
            boxes += 1
            num -= 1

    print(boxes+1)
