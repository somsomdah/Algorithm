n=int(input())

res=0 # 정답
temp=4 # 순위 - 같은 눈이 많을수록 순위가 높음, 같은 눈이 3개 나왔을 때 앞으로 같은 눈이 1개,2개 나오는 경우는 고려할 필요가 없음
for _ in range(n):
     n1,n2,n3=map(int,input().split())
     a=[n1,n2,n3]
     
     if len((set(a)))>temp:
            continue

     temp=len(set(a))
     if temp==1:
          res=max(res,a[0]*1000+10000)
     elif temp==2:
          for e in a:
               if a.count(e)==2:
                    res=max(res,e*100+1000)
                    break               
     else : #temp==3
          res=max(res,max(list(a)))


print(res)
          
     
