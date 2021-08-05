
n=int(input())

'''Bottom Up'''
D=[0]*(n+1)

D[1]=1
D[2]=2

for i in range(3,n+1):
     D[i]=D[i-1]+D[i-2]


print(D[n])


'''Top Down'''
D=[0]*(n+1)


def dfs(s):
     if D[s]!=0:
          return D[s]
     if s==1 or s==2:
          return s
     else:
          D[s]=dfs(s-1)+dfs(s-2)
          return D[s]

print(dfs(n))



