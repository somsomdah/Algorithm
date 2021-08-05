
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
     global temp_count
     
     check[x][y]=0 # 백트래킹이 필요 없는 
     temp_count+=1
     
     
     for i in range(4):
          xx=x+dx[i]
          yy=y+dy[i]

          if 0<=xx<n and 0<=yy<n and check[xx][yy]==1:
               
               dfs(xx,yy)
               
     

     

if __name__=="__main__":

     n=int(input())

     board=[list(int(i) for i in input()) for _ in range(n)]

     check=board

     temp_count=0
     count=0
     houses=[]
     

     for i in range(n):
          for j in range(n):
               if check[i][j]==1:
                    dfs(i,j)
                    houses.append(temp_count)
                    count+=1
                    temp_count=0

     houses.sort()

     print(count) #print(len(houses))
     for h in houses:
          print(h)
     
                    

