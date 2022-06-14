n = int(input())

t = []
p = []

for _ in range(n):
     tmpt, tmpp = map(int, input().split())

     t.append(tmpt)
     p.append(tmpp)


res = 0

def dfs(day, money):


     global res
     
     if day >= n:
          if money > res:
               res = money
          return
     
     dfs(day+t[day], money+p[day]) # 해당 day에 상담을 했을 경우
     dfs(day + 1, money)



dfs(0, 0)


print(res)
