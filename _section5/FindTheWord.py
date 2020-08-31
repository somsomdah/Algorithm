
n=int(input())
p=dict()

for _ in range(n):
     word=input()
     p[word]=1

for _ in range(n-1):
     word=input()
     p[word]=0


for key,val in p.items():
     if val==1:
          print(key)
          break;





# 성공한 코드
'''
import sys

n=int(sys.stdin.readline())
words=[]

for _ in range(n):
     words.append(input())

for _ in range(n-1):
     words.remove(input())

print(words[0])
'''
