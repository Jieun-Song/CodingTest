a,b = input().split(" ")
a = int(a)
b = int(b)

if a < 0 :
  myAflag = False
else :
  myAflag = True

if b < 0:
  myBflag = False
else : 
  myBflag = True

if myAflag and myBflag :
  if a>b :
    print(a-b)
  elif a<b :
    print(b-a)
elif myAflag or myBflag :
  if a>b :
    print(a-b)
  elif a<b :
    print(b-a)
else :
  if a>b :
    print(abs(a-b))
  elif a<b :
    print(abs(b-a))