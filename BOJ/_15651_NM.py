<<<<<<< HEAD
M,N=map(int,input().split())

def sequence(M,N):
    if N==1:
        return [[i] for i in range(1,M+1)]
    else:
        new_sequence=[]
        for i in range(1,M+1):
            for j in sequence(M,N-1):
                j.insert(0,i)
                new_sequence.append(j)
        return new_sequence
            
            
result=sequence(M,N)
for row in result:
    for i in row:
        print(i,end=' ')
    print()
=======
M,N=map(int,input().split())

def sequence(M,N):
    if N==1:
        return [[i] for i in range(1,M+1)]
    else:
        new_sequence=[]
        for i in range(1,M+1):
            for j in sequence(M,N-1):
                j.insert(0,i)
                new_sequence.append(j)
        return new_sequence
            
            
result=sequence(M,N)
for row in result:
    for i in row:
        print(i,end=' ')
    print()
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
