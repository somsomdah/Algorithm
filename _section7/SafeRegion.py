dx=[-1,0,1,0]
dy=[0,1,0,-1]


n=int(input())
board=[list(int(i) for i in input().split()) for _ in range(n)]

max_height=max([max(r) for r in board])
min_height=min([min(r) for r in board])


               
