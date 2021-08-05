<<<<<<< HEAD
import sys

n,m=map(int,sys.stdin.readline().split())
k=[int(sys.stdin.readline()) for _ in range(n) ] # 지시사향
d=[int(sys.stdin.readline()) for _ in range(m)] # 주사위 결과
k.insert(0,-10000)
d.insert(0,-10000)

cnt=0
pos=1

# m번의 count 동안
for i in range(1,m+1):
     pos+=k[pos]
     if pos>=n:
          break
     pos+=d[i]
     cnt+=1
     if pos>=n:
          break

print(cnt)
=======
import sys

n,m=map(int,sys.stdin.readline().split())
k=[int(sys.stdin.readline()) for _ in range(n) ] # 지시사향
d=[int(sys.stdin.readline()) for _ in range(m)] # 주사위 결과
k.insert(0,-10000)
d.insert(0,-10000)

cnt=0
pos=1

# m번의 count 동안
for i in range(1,m+1):
     pos+=k[pos]
     if pos>=n:
          break
     pos+=d[i]
     cnt+=1
     if pos>=n:
          break

print(cnt)
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
