<<<<<<< HEAD
import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

p=[-1]*n

for i in range(n):
     idx=a.index(min(a))
     p[idx]=i
     a[idx]=1001

for i in p:
     print(i,end=" ")
     

=======
import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

p=[-1]*n

for i in range(n):
     idx=a.index(min(a))
     p[idx]=i
     a[idx]=1001

for i in p:
     print(i,end=" ")
     

>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
