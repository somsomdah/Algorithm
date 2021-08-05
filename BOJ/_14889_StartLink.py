<<<<<<< HEAD
import itertools
import sys
#N=int(sys.stdin.readline())
N=int(input())

S=[]
for i in range(N):
    #S.append(list(map(int,sys.stdin.readline().split())))
    S.append(list(map(int,input().split())))

result=N*N*100-N

for c in itertools.combinations(range(N),int(N/2)):
    start_members=list(c)
    link_members=[i for i in range(N) if i not in start_members]

    start=0; link=0;
    for i,j in itertools.combinations(start_members,2):
        start+=S[i][j]+S[j][i]
    for i,j in itertools.combinations(link_members,2):
        link+=S[i][j]+S[j][i]
    temp=abs(start-link)
    if temp<result:
        result=temp

print(result)
=======
import itertools
import sys
#N=int(sys.stdin.readline())
N=int(input())

S=[]
for i in range(N):
    #S.append(list(map(int,sys.stdin.readline().split())))
    S.append(list(map(int,input().split())))

result=N*N*100-N

for c in itertools.combinations(range(N),int(N/2)):
    start_members=list(c)
    link_members=[i for i in range(N) if i not in start_members]

    start=0; link=0;
    for i,j in itertools.combinations(start_members,2):
        start+=S[i][j]+S[j][i]
    for i,j in itertools.combinations(link_members,2):
        link+=S[i][j]+S[j][i]
    temp=abs(start-link)
    if temp<result:
        result=temp

print(result)
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
