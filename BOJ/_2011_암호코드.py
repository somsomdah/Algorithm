import sys

num = int(input())
numlist = [int(ch) for ch in str(num)]
n = len(numlist)

if num <= 0:
     print(0)
     sys.exit(0)


D = [0] * (n)

D[0] = 1



if numlist[0] * 10 + numlist[1] <= 26:
     if numlist[1] != 0:
          D[1] = 2
     else:
          D[1] = 0
          
elif numlist[1] == 0:
     print(0)
     sys.exit(0)
     
else:
     D[1] = 1


for i in range(2, n):

     prevnum = numlist[i-1]
     thisnum = numlist[i]

     if thisnum == 0:
          if prevnum > 2:
               sys.exit(0)
               

     
     if thisnum > 0 :
          D[i] = D[i-1]
     if prevnum * 10 + thisnum <= 26:
          D[i] += D[i-2]



print(D[n-1] % 1000000)

