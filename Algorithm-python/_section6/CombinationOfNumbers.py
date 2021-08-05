def dfs(L,s,sum_): #레벨,시작점,해당 지점까지의 합
     
     global count
     
     if L==k: # 종료지점
          if sum_%m==0: # m의 배수이면
               count+=1 # 카운트
               
     else:
          for i in range(s,n): # 시작 인덱스 s부터 n-1까지
               res[L]=a[i] # 해당 레벨에서 간택받은 숫자
               dfs(L+1,i+1,sum_+a[i]) # 레벨 증가, 시작점 증가, 합
               
          


if __name__=="__main__":
     n,k=map(int,input().split()) # 정수의 갯수, 뽑는 수
     a=list(map(int,input().split())) # n개의 정수
     m=int(input()) # m

     res=[0]*k # 뽑히는수들
     count=0
     dfs(0,0,0)
     print(count)
     
