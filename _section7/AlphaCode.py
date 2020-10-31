
def dfs(L,P): # Level, Position(res의 현재 index)
     global cnt
     if L==n:
          cnt+=1 # 카운트 증가
          for j in range(P): # 해당 position의
               print(chr(64+res[j]),end='') # 숫자를 문자로 변환하여 출력, 65부터가 A
          print()
     else:
          for i in range(1,27): # 알파벳이 26개이므로 26개의 가지를 펼침
               
               if code[L]==i: # L번째 코드가 i번째 알파벳이라면 (i=10), code의 모든 원소는 1자리 수이므로
                    
                    res[P]=i # 결과 배열에 저장
                    
                    dfs(L+1,P+1) # 다음레벨, res의 다음 position 접근
                    
               elif i>=10 and code[L]==i//10 and code[L+1]==i%10: # i가 두자리 수라면, 코드의( L번째 자리수,L+1번째 자리 수) 가 i가 맞다면
                    res[P]=i # 결과 배열 res의 인덱스 P 위치에는 해당 숫자 i가 들어감
                    dfs(L+2,P+1) # 다다음 레벨, res의 다음 position







if __name__=="__main__":

     code=list(map(int,input())) # 입력된 코드를 정수로 받음
     
     n=len(code) # 입력된 코드의 길이 -> 레벨이 코드의 길이과 같아지면 종착점
     code.insert(n,-1) #index n에 -1 추가 :  out of index 방지

     res=[0]*n # 각 알파벳에 해당하는 숫자가 이 답길 리스트
     cnt=0 # 총 단어 갯수
     dfs(0,0)
     print(cnt)
