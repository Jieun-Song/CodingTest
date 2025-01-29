from collections import deque
import sys

# def editor(myString, edit, cursor):
#     type = edit[0]
#     if type == "P":
#         _, d = map(str,edit.split())
#         myString = myString[:cursor]+d+myString[cursor:]
#         cursor = cursor+1
#     elif type == "L":
#         if cursor > 0:
#             cursor = cursor - 1
#     elif type == "D":
#         if cursor < len(myString):
#             cursor = cursor + 1
#     elif type == "B":
#         if cursor > 0:
#             # 
#             cursor = cursor-1
#     else:
#         print("Something gone wrong")
#     return myString,cursor

# myString = input()
# cursor = len(myString)
# for _ in range(int(input())):
#     #처리하는 함수 호출
#     myString,cursor = editor(myString, input(), cursor)
# print(myString)

#deque이용해서 구현

def editor(myDeque, edit, cursor):
    type = edit[0]
    if type == "P":
        _, d = map(str,edit.split())
        if cursor == "0":
            myDeque.appendleft(d)
        else:
            myDeque.append(d)
        cursor = cursor+1
        
    elif type == "L":
        if cursor > 0:
            myDeque.rotate(1)
            cursor = cursor-1
    elif type == "D":
        if cursor < len(myString):
            myDeque.rotate(-1)
            cursor = cursor + 1
    elif type == "B":
        if cursor > 0:
            myDeque.pop()
            cursor = cursor-1
    else:
        print("Something gone wrong")
    return myDeque,cursor

myString = input()
cursor = len(myString)
myDeque = deque(list(myString))
print(myDeque)
for _ in range(int(input())):
    #처리하는 함수 호출
    myDeque,cursor = editor(myDeque, input(), cursor)
    print(myDeque)

myDeque.rotate(cursor)
print(*myDeque)
