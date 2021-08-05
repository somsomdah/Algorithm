<<<<<<< HEAD
def num_bridges(N,M):
    temp = [[-1 for col in range(M+1)] for row in range(N+1)]
    
    for i in range(N+1):
        for j in range(M+1):
            if i>j:
                temp[i][j]=0
            elif i==j or i==0 :
                temp[i][j]=1
                
    for i in range(N+1):
        for j in range(M+1):
            if (temp[i][j]==-1):
                temp[i][j]=temp[i][j-1]+temp[i-1][j-1]            
                

    print(temp[N][M])
    
num_input=int(input())

for i in range(num_input):
    case=input().split(" ")
=======
def num_bridges(N,M):
    temp = [[-1 for col in range(M+1)] for row in range(N+1)]
    
    for i in range(N+1):
        for j in range(M+1):
            if i>j:
                temp[i][j]=0
            elif i==j or i==0 :
                temp[i][j]=1
                
    for i in range(N+1):
        for j in range(M+1):
            if (temp[i][j]==-1):
                temp[i][j]=temp[i][j-1]+temp[i-1][j-1]            
                

    print(temp[N][M])
    
num_input=int(input())

for i in range(num_input):
    case=input().split(" ")
>>>>>>> 4acc6d3e3f0c7294e97481adc3209f2a884bf1ef
    num_bridges(int(case[0]),int(case[1]))