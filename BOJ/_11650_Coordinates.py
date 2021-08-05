<<<<<<< HEAD
import sys

q=[]

N=int(sys.stdin.readline()) # input 보다 빠름

for i in range(N):
    c=list(map(int,sys.stdin.readline().split()))
    q.append(c)
q.sort(key=lambda c:(c[0],c[1])) # 다중키 sort

for c in q:
=======
import sys

q=[]

N=int(sys.stdin.readline()) # input 보다 빠름

for i in range(N):
    c=list(map(int,sys.stdin.readline().split()))
    q.append(c)
q.sort(key=lambda c:(c[0],c[1])) # 다중키 sort

for c in q:
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
    print(c[0],c[1]);