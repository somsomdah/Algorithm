
n, m = map(int,input().split())

tasks = [list(map(int, input().split())) for _ in range(n)]


res = 0

def dfs(L, score, time):

     global res

     if time > m:
          return

     if L == n:
          if score > res:
               res = score
          return

     dfs(L+1, score+tasks[L][0], time+tasks[L][1])
     dfs(L+1, score, time)



dfs(0, 0, 0)
print(res)
