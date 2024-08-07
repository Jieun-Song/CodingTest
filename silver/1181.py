# 알파벳 소문자 N개의 단어 정렬프로그램
# 길이가 짧은 것부터 -> 사전순으로
# 중복X

num = int(input())
words = []

for i in range(0, num):
  words.append(input())

words = list(set(words))
words.sort()
words.sort(key = len)

# for i in range(0,len(words)-1):
#   if len(words[i]) == len(words[i+1]):
#     # print("글자수 같음!", words[i],words[i+1])
#     # 만약 앞글자보다 뒷글자랑 글자수가 같을시
#     if words[i]>words[i+1]:
#       # print("바꿀거임!", words[i],words[i+1])
#       # 앞글자가 사전순으로 먼저가 아닐시
#       temp = words[i]
#       words[i] = words[i+1]
#       words[i+1] = temp

for j in words:
  print(j)