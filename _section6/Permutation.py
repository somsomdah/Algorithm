
def DFS(L):
     global cnt
     
     if L==m: #level==m이 되었을 때
          for j in range(L):
               print(res[j],end=" ")
          print()
          cnt+=1

     else:
          for i in range(1,n+1):
               if ch[i]==0: # i를 사용하지 않음
                    ch[i]=1 # i를 사용하겠다
                    res[L]=i # ;level L은 i값을 가짐
                    DFS(L+1) # DFS L+1 호출
                    ch[i]=0 # i 사용한 것 풀어줌









if __name__=="__main__":
     n,m=map(int,input().split())
     res=[0]*m
     ch=[0]*(n+1)
     cnt=0
     DFS(0)

     print(cnt)
