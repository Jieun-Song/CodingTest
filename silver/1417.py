votes = []
result = 0

for i in range(int(input())):
    votes.append(int(input()))

if len(votes) == 1:
    print(result)
else :
    me = votes[0]
    others = votes[1:]

    while True:
        max_vote = max(others)

        if me > max_vote:
            break
        
        for i in range(len(others)):
            if others[i] == max_vote:
                others[i] -= 1
                me += 1
                result += 1
                break
    print(result)