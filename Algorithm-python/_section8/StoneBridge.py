
n=int(input())+1

D=[0]*(n+1)

D[1],D[2]=1,2

for i in range(3,n+1):
     D[i]=D[i-2]+D[i-1]

print(D[n])
