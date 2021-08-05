import sys

n,m,K=list(map(int,sys.stdin.readline().split()))
G=[[-1 for i in range(n+1)]for j in range(n+1)]

J=[]
for i in range(K):
     IJappend(int(sys.stdin.readline()))

for i in range(m):
     inp=list(map(int,sys.stdin.readline().split()))
     n1,n2,w=inp
     G[n1][n2]=w
     G[n2][n1]=w

#print(G)

#Dijkstra 반대
def Backtrack(node,I):
     for j in J:
          if node
     
