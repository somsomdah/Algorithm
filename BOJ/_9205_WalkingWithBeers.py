import sys

t=int(input())

def dist(v1,v2):
    x1,y1=v1
    x2,y2=v2
    return abs(x1-x2)+abs(y1-y2)

def dfs(v,visit):
    global graph
    for i in range(n+2):
        if graph[v][i]==1 and visit[i]==0:
            visit[i]=1
            dfs(i,visit)

for _ in range(t):
    n=int(input())
    # print(n)
    
    sx,sy=map(int,input().split())
    stores=[tuple(map(int,input().split())) for _ in range(n)]
    ex,ey=map(int,input().split())

    virtices=[(sx,sy)]
    virtices.extend(stores)
    virtices.append((ex,ey))

    # print(virtices)

    graph=[[sys.maxsize]*(n+2) for _ in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            dist_=dist(virtices[i],virtices[j])
            if dist_<=1000:
                graph[i][j]=1

    visit=[0]*(n+2)
    visit[0]=1
    dfs(0,visit)

    if visit[n+1]==0:
        print('sad')
    else:
        print('happy')
    


