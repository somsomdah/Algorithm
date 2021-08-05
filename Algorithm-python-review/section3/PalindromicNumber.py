grid = [list(map(int,input().split())) for _ in range(7)]

count = 0

for i in range(3):
     j = i + 5

     for row in grid:
          #print(row[i:j], list(reversed(row[i:j])))
          if row[i:j] == list(reversed(row[i:j])):
               count+=1


     for k in range(7):
          col = [row[k] for row in grid]
          #print(col[i:j], list(reversed(col[i:j])))
          if col[i:j] == list(reversed(col[i:j])):
               count+=1


print(count)
               
