n=int(input())

arr=[['*']*n for _ in range(n)]

def recursion(n,x1,y1,x2,y2):

     if n<3:
          return

     a0,a1,a2,a3 =x1,x1+n//3,x2-n//3,x2
     b0,b1,b2,b3=y1,y1+n//3,y2-n//3,y2

     #print(a0,a1,a2,a3)
     #print(b0,b1,b2,b3)
     for i in range(a1,a2):
          for j in range(b1,b2):
               arr[i][j]=' '

     recursion(n//3,a0,b0,a1,b1)
     recursion(n//3,a1,b0,a2,b1)
     recursion(n//3,a2,b0,a3,b1)
                      
     recursion(n//3,a0,b1,a1,b2)
     recursion(n//3,a2,b1,a3,b2)
                      
     recursion(n//3,a0,b2,a1,b3)
     recursion(n//3,a1,b2,a2,b3)
     recursion(n//3,a2,b2,a3,b3)



recursion(n,0,0,n,n)

for i in range(n):
     for j in range(n):
          print(arr[i][j],end='')
     print()
