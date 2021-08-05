dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]


t=int(input())

for _ in range(t):
     l=int(input())
     start_x,start_y=map(int,input().split())
     dest_x,dest_y=map(int,input().split())

     
     dist=[[0]*l for _ in range(l)]
     queue=[(start_x,start_y)]

     while queue:
          tmp_x,tmp_y=queue.pop(0)
          if tmp_x==dest_x and tmp_y==dest_y:
               break
          for i in range(8):
               x=tmp_x+dx[i]
               y=tmp_y+dy[i]

               if 0<=x<l and 0<=y<l and dist[x][y]==0:
                    dist[x][y]=1
                    queue.append((x,y))
                    dist[x][y]=dist[tmp_x][tmp_y]+1
                    
     print(dist[dest_x][dest_y])
