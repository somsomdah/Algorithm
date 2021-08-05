n=int(input())
stack=[]

for _ in range(n):
     i=int(input())
     if i!=0:
          stack.append(i)
     else:
          stack.pop()

print(sum(stack))
