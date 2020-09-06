
n,m=map(int,input().split())

weights=list(map(int,input().split()))
weights.sort()

left=m
count=0

     
while len(weights)>0:
     
     if len(weights)==1:
          count+=1
          weights.pop()
          break
          
     if weights[0]+weights[-1]<=m:
          weights.pop(0)
          weights.pop()
          count+=1
     else:
          weights.pop()
          count+=1
          
print(count)
