n=int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

def rotate(l,d,k):
     if d==0: # 왼쪽으로 회전
          for _ in range(k):
               l.append(l.pop(0))
     else: # if d==1: # 오른쪽으로 회전
          for _ in range(k):
               l.insert(0,l.pop())
          
m = int(input())

for _ in range(m):
     a,b,c = map(int,input().split())
     rotate(grid[a-1],b,c)


lt, rt = 0,n



total=0

for i in range(n):
     total+=sum(grid[i][lt:rt])

     if i<n//2:
          lt+=1
          rt-=1
     else:
          lt-=1
          rt+=1


print(total)

