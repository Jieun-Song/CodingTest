n, k = map(int, input().split())
listA = list(range(1, n+1))

indexK = k-1
removed = []
while len(listA)>0:
    try:
        one = listA[indexK]
        listA.remove(one)
        indexK = indexK + k-1
        removed.append(one)
        
    except IndexError:
        if indexK >= len(listA):
            indexK = indexK - len(listA)

print("<"+", ".join(map(str, removed))+">")
