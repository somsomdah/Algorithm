def dfs(L):
     global cnt
     if L==m:
          for i in range(m):
               print(res[i],end= " ")
          print()
          cnt+=1
     else:
          for i in range(1,n+1):
               if ch[i]==0: # 사용하지 않았다면
                    ch[i]=1 #사용했음을 체크
                    res[L]=i # 결과반영
                    dfs(L+1)#dfs
                    ch[i]=0 # 체크 풀어주기
                    



if __name__=="__main__":
     n,m=map(int,input().split())
     ch=[0]*(n+1)
     res=[0]*(m)
     cnt=0
     dfs(0)
     print(cnt)
