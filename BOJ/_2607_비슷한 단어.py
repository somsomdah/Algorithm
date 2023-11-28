n = int(input())
words = [input() for _ in range(n)]
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters1 = {}
for a in alphabets:
    letters1[a] = 0

def composition(word):
    letters = letters1.copy()
    for w in word:
        letters[w] += 1
    return list(letters.values())

count = 0
w1 = composition(words[0])


for i in range(1, n):
    w2 = composition(words[i])
    tmp = [w1[i] - w2[i] for i in range(26)]
    if tmp.count(0) == 26:
        count += 1
    elif tmp.count(0) == 25:
        if tmp.count(1) == 1 or tmp.count(-1) == 1:
            count += 1
    elif tmp.count(0) == 24:
        if tmp.count(-1) == 1 and tmp.count(1) == 1:
            count += 1


print(count)
        



