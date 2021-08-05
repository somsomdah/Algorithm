import sys
while True:
     sentence=input()
     if sentence=='.':
          break

     stack=[]

     for s in sentence:
          if s=='(' or s=='[' or s==')' or s==']':
               stack.append(s)
          if len(stack)>=2 and (stack[-2]=='(' and stack[-1]==')'):
               stack.pop()
               stack.pop()
          if len(stack)>=2 and (stack[-2]=='[' and stack[-1]==']'):
               stack.pop()
               stack.pop()

     if len(stack)==0:
          print('yes')
     else:
          print('no')
