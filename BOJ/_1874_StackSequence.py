n=int(input())

stack=[]
res=[]
k=1
for _ in range(n):
    
    i=int(input())
    
    if not stack:
        stack.append(k)
        res.append('+')
        k+=1

    if stack:
        while stack[-1]<i:
            stack.append(k)
            res.append('+')
            k+=1
        stack.pop()
        res.append('-')

if stack:
    print('NO')
else:
    for r in res:
        print(r)
        
