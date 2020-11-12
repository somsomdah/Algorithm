dx,dy=[-1,0,1,0],[0,1,0,-1]

n=int(input())
a=[] # 격자판
for _ in range(n):
     a.append(list(map(int,input().split())))
     

visit=[[0]*n for _ in range(n)] # 격자판에서 방문했는지의 여부

sum=0 # 사과의 총 갯수

Q=[] # queue
visit[n//2][n//2]=1
sum+=a[n//2][n//2]

Q.append((n//2,n//2))
L=0 #level


while True:
     
     if L==n//2: # level이 끝까지 가면 break
          break
     
     size=len(Q) # queue의 길이
     
     for i in range(size): # queue의 길이 동안
          
          tmp=Q.pop(0) # queue에서 가장 첫번째 원서 제거
          
          for j in range(4): # 상하좌우
               x=tmp[0]+dx[j]
               y=tmp[1]+dy[j]
               
               if visit[x][y]==0: # 상하좌우 위치에서, 방문하지 않았다면
                    sum+=a[x][y] # 총 합에 더함
                    visit[x][y]=1 # 방문함
                    Q.append((x,y)) # 상하좌우 좌표
     L+=1
     #print(L,size)
     for x in visit:
         # print(x)

print(sum)
