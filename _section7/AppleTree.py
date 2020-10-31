


dx,dy=[-1,0,1,0],[0,1,0,-1]

n=int(input())
a=[]
for _ in range(n):
     a.append(list(map(int,input().split())))

ch=[[0]*n for _ in range(n)]
sum=0
Q=[]
ch[n//2][n//2]=1
sum+=a[n//2][n//2]

Q.append((n//2,n//2))
L=0


while True:
     if L==n//2:
          break
     size=len(Q)
     for i in range(size):
          
          tmp=Q.pop(0)
          for j in range(4):
               x=tmp[0]+dx[j]
               y=tmp[1]+dy[j]
               if ch[x][y]==0:
                    sum+=a[x][y]
                    ch[x][y]=1
                    Q.append((x,y))
     L+=1
     print(L,size)
     for x in ch:
          print(x)

print(sum)
