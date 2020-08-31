import heapq

heap=[]
while True:
     i=int(input())
     if i==-1:
          break
     elif i==0:
          if len(heap)==0:
               print(-1)
          else:
               print(-heapq.heappop(heap))
     else:
          heapq.heappush(heap,-i)
               
