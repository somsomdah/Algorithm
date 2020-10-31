def dfs(L): 
     global res
     if L==n: # 종착점 도달, 각 가지는 해당 동전을 쓸지, 안 쓸지 결정
          cha=max(money)-min(money) # 가장 큰 총액-가장 작은 총액
          if cha<res: # 총액의 차가 더 작은 경유가 있고
               if len(set(money))==3: # 세 사람의 총액이 서로 다르다면
                    res=cha # 결과값은 아까 구한 cha
     
     else:
          for i in range(3):
               money[i]+=coin[L] # i번째 사람에게 L번째 동전을 줌
               dfs(L+1) # 다음 레벨 탐색 : index L+1번째 동전을 쓸지 말지 탐색
               money[i]-=coin[L] # 다시 back 할 때 동전 줬던 것을 무효화 해야 함
               


if __name__=="__main__":
     n=int(input()) # 동전의 갯수
     coin=[int(input()) for _ in range(n)] # 동전의 금액
     money=[0,0,0] # 세 사람이 가질 돈
     res=sum(coin) # 최대 결과값
     dfs(0)
     print(res) # 최소 결과값
