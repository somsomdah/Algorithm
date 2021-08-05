n=int(input())

def check_vps(string):
     ps_list=[c for c in string]
     stack=[]

     for p in ps_list:
          if stack and (stack[-1]=='(' and p==')'):
                    stack.pop()
          else:
               stack.append(p)
          #print(stack)

     if stack:
          return False
     else:
          return True

for _ in range(n):
     if check_vps(input()):
          print('YES')
     else:
          print('NO')

