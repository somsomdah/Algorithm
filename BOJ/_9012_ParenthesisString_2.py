t = int(input())

for _ in range(t):
     ps = [ch for ch in input()]

     stack = []

     flag = 0

     while(ps) :
          k = ps.pop(0)

          if k == '(' :
               stack.append(k)
          else:
               if stack:
                    stack.pop()
               else:
                    print('NO')
                    flag = 1
                    break

     if flag :
          continue;
               

     if stack:
          print('NO')
     else:
          print('YES')
          
