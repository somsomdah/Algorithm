<<<<<<< HEAD
M,N=map(int,input().split())
numbers=list(map(int,input().split()))
queue=list(range(1,M+1))

count=0

for number in numbers:
    p=queue.index(number);
    
    if (p==0):
        queue.remove(number)
        continue;

    temp=queue[:p]
    queue=queue[p+1:]
    queue.extend(temp)
     
    if(p<=len(queue)/2):
        count+=p
    elif(p>len(queue)/2):
        count+=(len(queue))-p+1
        

print(count)
=======
M,N=map(int,input().split())
numbers=list(map(int,input().split()))
queue=list(range(1,M+1))

count=0

for number in numbers:
    p=queue.index(number);
    
    if (p==0):
        queue.remove(number)
        continue;

    temp=queue[:p]
    queue=queue[p+1:]
    queue.extend(temp)
     
    if(p<=len(queue)/2):
        count+=p
    elif(p>len(queue)/2):
        count+=(len(queue))-p+1
        

print(count)
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
