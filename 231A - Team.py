n = input()
count = 0
for i in range(0,int(n)):
    vote = input()
    votes = vote.split(' ')
    if int(votes[0]) + int(votes[1]) + int(votes[2]) >= 2:
        count += 1
print(count)
         