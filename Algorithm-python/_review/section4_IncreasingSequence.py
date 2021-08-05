
n=int(input())
seq=list(map(int,input().split()))
end=0
res=''

lt,rt=0,n-1
tmp=[]
while lt<=rt:
     if seq[lt]>end:
          tmp.append((seq[lt],'L'))
     if seq[rt]>end:
          tmp.append((seq[rt],'R'))
     tmp.sort()

     if len(tmp)==0:
          break
     else:
          res=res+tmp[0][1]
          end=tmp[0][0]
          if tmp[0][1]=='L':
               lt+=1
          else:
               rt-=1
     tmp.clear()
               
'''
while True:
     if seq[0]<end and seq[-1]<end:
          break
     if seq[0]<end and end<seq[-1]:
          end=seq[-1]
          seq.pop()
          res=res+'R'
     if seq[-1]<end and end<seq[0]:
          end=seq[0]
          seq.pop(0)
          res=res+'L'
     if min(seq[-1],seq[0])>end:
          if seq[-1]<seq[0]:
               end=seq[-1]
               seq.pop()
               res=res+'R'
          else:
               end=seq[0]
               seq.pop(0)
               res=res+'L'             
'''               

print(len(res))
print(res)


     
