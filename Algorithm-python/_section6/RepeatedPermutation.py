

def DFS(L):
     global cnt
     if L==m: # 종착점
          for j in range(m): #res에 들어있는 정답 출력
               print(res[j],end=" ")
          print()
          cnt+=1 # 카운트 증가 (종착점에 왔으므로)

     else:
          for i in range(1,n+1):
               res[L]==i # res의 인덱스 L의 값이 i 일 때
               DFS(L+1) # 다음 레벨의 DFS 호출

if __name__=="__main__":
     n,m=map(int,input().split())
     res=[0]*n # 1줄의 출력을 저장하는 배
     cnt=0
     DFS(0)
     print(cnt)
