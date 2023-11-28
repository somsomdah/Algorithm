from collections import deque
t = int(input())


for _ in range(t):
    n =int( input())
    parent = [0 for _ in range(n+1)]
    
    for _ in range(n-1):
        p, c = map(int, input().split())
        parent[c] = p
    v1, v2 = map(int, input().split())
    
    root = 0
    for i in range(1, n+1):
        if parent[i] == 0:
            root = i
            break

    
    ancestors1 = deque([v1])
    ancestors2 = deque([v2])
    tmp1, tmp2 = v1, v2
    while tmp1 != root:
        tmp1 = parent[tmp1]
        ancestors1.append(tmp1)
    while tmp2 != root:
        tmp2 = parent[tmp2]
        ancestors2.append(tmp2)


    while  len(ancestors1) > len(ancestors2):
            ancestors1.popleft()
    while  len(ancestors2) > len(ancestors1):
            ancestors2.popleft()
            
    answer = 0
    while ancestors1 and ancestors2:
        tmp1, tmp2 = ancestors1.popleft(), ancestors2.popleft()
        if tmp1 == tmp2:
            answer = tmp1
            break


    print(answer)
        
        

            
            
        

        


    
    
