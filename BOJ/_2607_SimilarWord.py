n = int(input())

words = [input() for _ in range(n)]


count = 0

s = words[0]

for i in range(1, n):
     w = words[i]

     s_l = len(s)
     w_l = len(w)

     if abs(s_l - w_l) > 1:
          continue
     
     w_split = [ch for ch in w]
     s_split = [ch for ch in s]

     w_split.sort()
     s_split.sort()

     if w_split == s.split:
          count += 1
          continue;


     if s_l > w_l:
          short = w_split
          long = s_split
     else:
          short = s_split
          long = w_split

     for ch in short:
          if ch in long:
               long.remove(ch)

     if len(long) <= 1:
          count += 1
               

print(count)
               
