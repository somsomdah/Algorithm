
n=int(input())

players=[]
for _ in range(n):
     h,w=map(int,input().split())
     players.append((h,w))

players.sort(reverse=True) # height 기준으로 sort
#print(players)
x=players[0][1]
count=1

for i in range(1,n):
     if players[i][1]>x:
          x=players[i][1]
          count+=1

print(count)
     
