import sys

board=[list(map(int,sys.stdin.readline().split())) for _ in range(7)]


count=0

for i in range(3): # 시작 index
     for j in range(7): # row
          if all(board[j][k]==board[j][4+2*i-k] for k in range(i,i+3)) :  
               count+=1
          if all(board[k][j]==board[4+2*i-k][j] for k in range(i,i+3)) :
               count+=1

print(count)



# 행방향의 경우 다음과 같은 코드도 가능                   
# tmp=board[j][i:i+5]
# if tmp==tmp[::-1]:
#    count+=1
