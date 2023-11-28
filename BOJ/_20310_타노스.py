from collections import deque
S =deque([ch for ch in input()])
m = len(S)//2
o, z = S.count('1')//2, S.count('0')//2
stack = []

while S:

     tmp = S.popleft()

     if tmp  == "1":
          if o > 0:
             o -= 1
          else:
               stack.append(tmp)

     else:
          if z > 0:
               stack.append(tmp)
               z -= 1
          else:
               pass

ans = ""
for ch in stack:
     ans += ch

print(ans)

