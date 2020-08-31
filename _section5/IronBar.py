import sys

string=sys.stdin.readline()

stack=[]
count=0

for i in range(len(string)-1): #'\n' 제외
     
     if string[i]=='(':
          stack.append(string[i])
     else:
          stack.pop()
          if string[i-1]=='(':
               count+=len(stack)
          else:             
               count+=1
print(count)
