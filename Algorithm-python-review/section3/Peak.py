n=int(input())

a=[list(map(int,input().split())) for _ in range(n)]

for l in a:
     l.insert(0,0)
     l.append(0)


a.insert(0,[0]*(n+2))
a.append([0]*(n+2))

count = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(1,n+1):
     for j in range(1,n+1):

          for k in range(4):
               if a[i][j]<=a[i+dx[k]][j+dy[k]]:
                    break
          else:
               count+=1
          


print(count)
