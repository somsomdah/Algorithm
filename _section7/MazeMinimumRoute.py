
dx=[-1,0,1,0]
dy=[0,1,0,-1]

maze=[list(map(int,input().split())) for _ in range(7)] # visit
dist=[[0]*7 for _ in range(7)]

Q=[]
Q.append((0,0))
maze[0][0]=1

while Q:
     tmp=Q.pop(0)

     for i in range(4):
          
          x=tmp[0]+dx[i]
          y=tmp[1]+dy[i]

          if 0<=x<=6 and 0<=y<=6 and maze[x][y]==0:
               maze[x][y]=1
               dist[x][y]=dist[tmp[0]][tmp[1]]+1
               
               Q.append((x,y))


if dist[6][6]==0:
     print(-1)
else:
     print(dist[6][6])
