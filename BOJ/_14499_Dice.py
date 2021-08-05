
n,m,x,y,k=map(int,input().split()) # n : 세로길이 / m : 가로길이
mapp=[list(map(int,input().split())) for _ in range(n)]
commands=list(map(int,input().split()))


dice=[
     [0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0]
     ]


def go_east(): #오른쪽으로 굴림
     dice[1][0],dice[1][1],dice[1][2],dice[3][1]=dice[3][1],dice[1][0],dice[1][1],dice[1][2]


def go_west(): # 왼쪽으로 굴림
     dice[1][0],dice[1][1],dice[1][2],dice[3][1]=dice[1][1],dice[1][2],dice[3][1],dice[1][0]


def go_north(): # 윗쪽으로 굴림
     dice[0][1],dice[1][1],dice[2][1],dice[3][1]=dice[1][1],dice[2][1],dice[3][1],dice[0][1]


def go_south(): # 아랫쪽으로 굴림
     dice[0][1],dice[1][1],dice[2][1],dice[3][1]=dice[3][1],dice[0][1],dice[1][1],dice[2][1]



for c in commands:

     if c==1: # east
          temp_y=y+1
          if temp_y<m:
               y=temp_y
               go_east()
          else:
               continue
               
     elif c==2: # west
          temp_y=y-1
          if temp_y>=0:
               y=temp_y
               go_west()
          else:
               continue

     elif c==3: # north
          temp_x=x-1
          
          if temp_x>=0:
               x=temp_x
               go_north()
          else:
               continue               
               
     else:# c==4: # south
          temp_x=x+1
          if temp_x<n:
               x=temp_x
               go_south()
          else:
               continue               
               
     if mapp[x][y]==0:
          mapp[x][y]=dice[3][1]
     else:
          dice[3][1]=mapp[x][y]
          mapp[x][y]=0


     print(dice[1][1])


     
