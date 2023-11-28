import sys
sys.stdin = open("in5.txt","r")


tmp = ""

string = input()

for ch in string:
    # if ch.isdecimal():
    # res * 10 + int(ch)
    if ch.isdigit():
        tmp += ch

res = int(tmp)

cnt = 1

for i in range(1, res//2 + 1):
    if res % i == 0:
        cnt  += 1


print(res)
print(cnt)
