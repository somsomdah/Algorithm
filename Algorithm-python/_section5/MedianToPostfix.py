import sys

# stack top의 우선순위가 자기보다 낮게
a=input()
stack=[]
res=""

for x in a:
     if x.isdecimal():
          res+=x
     else: # 문자일 경우
          if x=='(': # 일단 append
               stack.append(x)
          elif x=='*' or x=='/' or x=='+' or x=='-':
               while stack and (stack[-1]=='*' or stack[-1]=='/'): # 우선순위가 작을때 pop
                    res+=stack.pop()
               stack.append(x)
          elif x==')':
               while stack and stack[-1]!='(': # 괄호 안의 연산자
                    res+=stack.pop()
               stack.pop()

while stack:
     res+=stack.pop()

print(res)
                        


'''
equation=[c for c in sys.stdin.readline() if c!='\n']
stack=[]
result=[]

for e in equation:    
     if e.isdecimal():
          result.append(e)
          if stack and (stack[-1]=='*' or stack[-1]=='/'):
               result.append(stack.pop())
     elif e==')':
          while stack[-1]!='(':
               result.append(stack.pop())
          stack.pop()
     else:
          stack.append(e)

while stack:
     result.append(stack.pop())

for r in result:
     print(r,end='')
     
'''
