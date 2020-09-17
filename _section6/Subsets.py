
def DFS(v):
     if v==n+1: # 종료조건
          for i in range(1,n+1):
               if check[i]==1: #원소 i 가 check 되어 있음
                    print(i, end=' ')
          print()
          return
     else:
          check[v]=1 # v 포함
          DFS(v+1) # v+1번재 원소부터 트리
          check[v]=0 # v불포함
          DFS(v+1)

if __name__=="__main__":
     n=int(input())
     check=[0]*(n+1) # 원소 n이 포함되었는지 여부
     DFS(1)
