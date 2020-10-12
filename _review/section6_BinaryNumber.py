
def DFS(n):
     if n!=0:
          DFS(n//2)
          print(n%2,end="")

if __name__=="__main__":
     DFS(int(input()))
