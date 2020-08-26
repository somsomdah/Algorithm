import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

lt,rt=0,n-1
last=0
res=""
tmp=[]

# last보다 큰지 확인
while lt<=rt:
     if a[lt]>last:
          tmp.append((a[lt],'L'))
     if a[rt]>last:
          tmp.append((a[rt],"R"))
     tmp.sort() # 둘중에 작은 것을 선택해야 하기 때문에
     if len(tmp)==0:
          break
     else:
          res=res+tmp[0][1]
          last=tmp[0][0]
          if tmp[0][1]=='L':
               lt+=1
          else:
               rt-=1
     tmp.clear()

print(len(res))
print(res)


'''
n=int(sys.stdin.readline())
inpt=list(map(int,sys.stdin.readline().split()))
seq=[-1]
res=[]

for i in range(n-1):
     if min(inpt[0],inpt[-1])>seq[-1]:
          if inpt[0]<inpt[-1]: #left<fight
               seq.append(inpt.pop(0))
               res.append('L')
          else: # left>right
               seq.append(inpt.pop())
               res.append('R')
     elif max(inpt[0],inpt[-1])>seq[-1]:
          if inpt[0]>seq[-1]:
               seq.append(inpt.pop(0))
               res.append('L')
          else:
               seq.append(inpt.pop())
               res.append('R')
     else:
          break

#print(seq)
print(len(res))
for i in res:
     print(i,end="")
     
'''                        
