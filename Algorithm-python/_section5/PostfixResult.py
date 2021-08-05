import sys

equation=[s for s in sys.stdin.readline() if s!='\n']

stack=[]

for e in equation:
     if e.isdecimal():
          stack.append(int(e))
     else:
          b=stack.pop()
          a=stack.pop()

          if e=='+':
               stack.append(a+b)
          if e=='-':
               stack.append(a-b)
          if e=='*':
               stack.append(a*b)
          if e=='/':
               stack.append(a/b)

print(stack[0])
