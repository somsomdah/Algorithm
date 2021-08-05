
def recursion(n):
     if n==0:
          return
     else:
          recursion(n//2)
          print(n%2, end='')


n=int(input())
recursion(n)
