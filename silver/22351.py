myNum = input()
for i in range(1,4):
  result = myNum[:i]
  n = int(myNum[:i])

  while len(myNum) > len(result):
    n += 1
    result += str(n)

  if myNum == result:
    print(myNum[:i], n)
    break
  # else:
    # print(result)



# result = ""
# n = 0

# if myNum[0]=="9":
#   # 맨 앞자리가 9일때,,
#   # 99일때, 9일때 만 잡으면 될거같음
#   if myNum == "999":
#     # print(3)
#     print("999 999")
#   elif myNum == "99":
#     print("99 99")
#   elif myNum == "9":
#     print("9")
#   elif (myNum[0] == "9") and (int(myNum[0])+1 == int(myNum[1:3])):
#     # print("첫 숫자가 9인..")
#     while len(myNum) != len(result):
#       result += str(int(myNum[0])+n)
#       n+=1
#     print(myNum[0], str(int(myNum[0])+n-1))
#   elif (myNum[0:2] == "99") and (int(myNum[0:2])+1 == int(myNum[2:5])):
#     while len(myNum) != len(result):
#       result += str(int(myNum[0:2])+n)
#       n+=1
#     print(myNum[0:2], str(int(myNum[0:2])+n-1))
#     # print(2)
#   print(9)  


#   # elif len(myNum)>=2 & (int(myNum[0])+1 == int(myNum[1:3])):
#   #   print(1)
#   #   while len(myNum) != len(result):
#   #     result += str(int(myNum[0])+n)
#   #     n+=1
#   #   print(myNum[0], str(int(myNum[0])+n-1))

#   # elif len(myNum)>=4 & (int(myNum[0:2])+1 == int(myNum[2:5])):
#   #   while len(myNum) != len(result):
#   #     result += str(int(myNum[0:2])+n)
#   #     n+=1
#   #   print(myNum[0:2], str(int(myNum[0:2])+n-1))
#   #   print(2)

#   # else :
#   #   print(4)
#   #   print(myNum, myNum)

# else:
#   if (len(myNum)>=2 and (int(myNum[0])+1 == int(myNum[1:2]))):
#     while len(myNum) != len(result):
#       result += str(int(myNum[0])+n)
#       n+=1
#     print(myNum[0], str(int(myNum[0])+n-1))
#     # print(5)
#   elif (len(myNum)>=4 and (int(myNum[0:2])+1 == int(myNum[2:4]))):
#     while len(myNum) != len(result):
#       result += str(int(myNum[0:2])+n)
#       n+=1
#     print(myNum[0:2], str(int(myNum[0:2])+n-1))
#     # print(6)
#   elif (len(myNum)>=6 and (int(myNum[0:3])+1 == int(myNum[3:6]))):
#     while len(myNum) != len(result):
#       result += str(int(myNum[0:3])+n)
#       n+=1
#     print(myNum[0:3], str(int(myNum[0:3])+n-1))
#     # print(7)
#   else:
#     print(myNum, myNum)
#     print(8)
  

# # 9가 중간에 들어있으면 그 다음은 2개짜리
