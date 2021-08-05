import sys

sudoku = [list(map(int,input().split())) for _ in range(9)]
a=[1,2,3,4,5,6,7,8,9]

for i in range(9):

     temp = sorted(sudoku[i])
     if temp != a:
          print('NO')
          sys.exit(0)

     temp2 = sorted(r[i] for r in sudoku)
     if temp2!=a:
          print('NO')
          sys.exit(0)


for i in range(3):
     for j in range(3):
          temp = [row[3*j:3*(j+1)] for row in sudoku[3*i:3*(i+1)]]
          temp_t=[]
          
          for t in temp:
               temp_t+=t

          temp_t.sort()

          if temp_t !=a:
               print('NO')
               sys.exit(0)


print('YES')
