import sys
n,m=map(int,(sys.stdin.readline().split()))
trees=list(map(int,sys.stdin.readline().split()))

def total(height):
     ans=0
     for t in trees:
          if t-height>0:
               ans+=t-height
     return ans


def binary_search(m):
     lt,rt=0,max(trees)
     res=0
     while lt<=rt:
          mid=(lt+rt)//2
          total_=total(mid)
          if total_==m:
               res=mid
               break;
          if total_<m: # 절단기가 너무 높은 위치에 있을 때
               rt=mid-1

          elif total_>m: # 절단기가 너무 낮은 위치에 있을 때
               lt=mid+1
               if res<mid:
                    res=mid
     return res
               
print(binary_search(m))
          
#시간초과의 원인!#
'''
def total(height):
     a=sum(map(lambda x:max(x-height,0),trees))
     return a
'''
