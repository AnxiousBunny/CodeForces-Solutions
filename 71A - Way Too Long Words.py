n = int(input())
words = []

for i in range(0,int(n)):
    words.append(input())
    if len(words[i]) > 10:
        words[i] = words[i][0] + str(len(words[i])-2) + words[i][-1]
    print(words[i])

        




