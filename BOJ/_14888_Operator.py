import sys

n=int(input())
numbers=list(map(int,input().split()))
pl,mn,mt,dv=map(int,input().split())

res_max=-sys.maxsize
res_min=sys.maxsize

def dfs(L,op_list,total):
     #print(op_list)
     global res_max,res_min
     
     if L==n-1:
          #print("max",res_max,total)
          res_max=max(res_max,total)
          res_min=min(res_min,total)
          return

     else:
          for i in range(4):
               if op_list[i]>0:
                    op_list[i]-=1
                    if i==0:
                         dfs(L+1,op_list,total+numbers[L+1])
                    if i==1:
                         dfs(L+1,op_list,total-numbers[L+1])
                    if i==2:
                         dfs(L+1,op_list,total*numbers[L+1])
                    if i==3:
                         dfs(L+1,op_list,int(total/numbers[L+1]))
                    op_list[i]+=1

dfs(0,[pl,mn,mt,dv],numbers[0])
print(res_max)
print(res_min)




                         
               
          
          
     
