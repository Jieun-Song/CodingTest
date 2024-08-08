# 3 이상 50 이하 영어 소문자 단어 주어짐
# 임의의 두군데 잘라서 뒤집고 합침
# 자를때 2개이상..
# 사전순으로 가장 앞서는 단어를 출력

# 이게 사전순으로 가장 앞서야하니까...
# 가장 앞선 알파벳 다음을 자르는게 제일 베스트일듯.

######첫번째 자르기는 완료. 근데 그 다음 자르기가 잘 안된다.#########

def findTheFast(cha):
  listCha = [*cha]
  minCha = min(listCha)
  return myCha.index(minCha)
  

myCha = input()
cnt = 0

minIndex = findTheFast(myCha)

lastCha = myCha

while cnt <3:
  if minIndex>=1:
    #Index가 1보다 클때만 자르기 수행
    newCha = lastCha[0 : minIndex+1]
    lastCha = lastCha[minIndex+1:]
    cnt += 1
    print(newCha, lastCha, cnt)
    minIndex = findTheFast(lastCha)
    print(minIndex)




