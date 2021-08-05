n,m=map(int,input().split())
A=list(map(int,input().split()))

lt,rt=0,0
count=0
total=A[0]

while rt<n:
     if total==m:
          #print(lt,rt)
          count+=1
          if lt+1<n and rt+1<n:
               lt+=1
               rt+=1
               total=total-A[lt-1]+A[rt]
          else:
               break

     if total<m:
          if rt+1<n:
               rt+=1
               total+=A[rt]
          else:
               break

     if total>m:
          if lt+1<n:
               lt+=1
               total-=A[lt-1]
          else:
               break

print(count)

