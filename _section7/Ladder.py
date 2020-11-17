def dfs(x,y):

     board[x][y]=0

     if x==0:
          print(y)

     if 0<=y+1<10 and board[x][y+1]==1:
          dfs(x,y+1)
          
     elif 0<=y-1<10 and board[x][y-1]==1:
          dfs(x,y-1)
          
     elif 0<=x-1<10:
          dfs(x-1,y)







if __name__=="__main__":
     
     board=[list(map(int,input().split())) for _ in range(10)]

#     for b in board:
#          print(b)

     
     for i in range(10):
          if board[9][i]==2:
               dfs(9,i)
