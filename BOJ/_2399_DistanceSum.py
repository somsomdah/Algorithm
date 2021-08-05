<<<<<<< HEAD
N = int(input())
X=list(map(int,input().split()))
X.sort();

result=0;
for i in range(N):
    result+=(i-(N-(i+1)))*X[i]
    
result*=2;

=======
N = int(input())
X=list(map(int,input().split()))
X.sort();

result=0;
for i in range(N):
    result+=(i-(N-(i+1)))*X[i]
    
result*=2;

>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
print(result)