
MAX=100000

ch=[0]*(MAX+1)
dis=[0]*(MAX+1)

n,m=map(int,input().split())


ch[n]=1
dis[n]=0


q=[]
q.append(n)

while q:
     parent=q.pop(0) # 부모노드의 value
     
     for child in (parent-1,parent+1,parent+5): # 자식 노드의 value
          if 0<child<=MAX:
               if ch[child]==0:
                    q.append(child)
                    ch[child]=1
                    dis[child]=dis[parent]+1
                    
print(dis[:m+1])
print(ch[:m+1])
                    
print(dis[m])
