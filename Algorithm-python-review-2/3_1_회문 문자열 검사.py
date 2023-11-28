import sys
sys.stdin = open("in5.txt", "r")

t = int(input())

for c in range(t):
    string = input().lower()
    n = len(string)

    # if string == string[::-1]:
    for i in range(n//2):
        if string[i] != string[n-1-i]:
            print("#{} NO".format(c+1))
            break
    else:
        print("#{} YES".format(c+1))
    
