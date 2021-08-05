

def dfs(L,P): 
     global cnt

     if L==n:
          cnt+=1
          print(res)
          for i in range(P):
               print(chr(65+res[i]),end="")
          print()
     else:
          for i in range(1,27): # 모든 알파벳의 경우 탐색
               if i<10:
                    if code[L]==i: #L번째 숫자가 i와 일치할 경우
                         res[P]==i
                         dfs(L+1,P+1)

               else: # if i>=10
                    if code[L]==i//10 and code[L+1]==i%10: #연속된 두개의 숫자가 i와 일치할 경우
                         res[P]=i
                         dfs(L+2,P+1) # code에서는 L+2부터 탐색을 하고, res의 P+1번째 숫자를 구함
          








if __name__=="__main__":

     code=[int(c) for c in input()]

     n=len(code)

     code.append(-1)

     res=[0]*n

     cnt=0

     dfs(0,0)

     print(cnt)
