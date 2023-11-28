string = input()
n = len(string)
i = 0
m = string.count("b")
answer = n

while i  <  n:
    if i + m  <= n:
        cnt = string[i:i+m].count("a")
    else:
        cnt =( string[i:] + string[:(i+m)%n]).count('a')
    if cnt < answer:
        answer = cnt
    i += 1
    
print(answer)
