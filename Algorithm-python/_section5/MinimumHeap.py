import heapq as hq
a=[]
while True:
     n=int(input())
     if n==-1:
          break
     if n==0:
          if len(a)==0:
               print(-1)
          else:
               print(hq.heappop(a))
     else:
          hq.heappush(a,n)







# wrong answer
'''
def downheap(heap): # 노드 제거
     res=heap[1]
     temp=heap.pop()
     if len(heap)==1:
          return res
     heap[1]=temp
     i=1
     while True:

          if len(heap)>2*i+1:
               if heap[i]<min(heap[2*i+1],heap[2*1]):
                    if heap[2*i]<heap[2*i+1]:
                         heap[2*i],heap[i]=heap[i],heap[2*i]
                         i=2*i
                    else:
                         heap[2*i+1],heap[i]=heap[i],heap[2*i+1]
                         i=2*i+1
               else:
                    return res
          else:
               if heap[i]<heap[2*i]:
                    heap[2*i],heap[i]=heap[i],heap[2*i]
               else:
                    return res


def upheap(heap,a): # 노드 삽입
     heap.append(a)
     i=len(heap)-1

     while True:
          if i>=2 and heap[i]<heap[i//2]:
               heap[i],heap[i//2]=heap[i//2],heap[i]
               i=i//2
          else:
               break


heap=[-1]    
while True:
     #print(heap)
     num=int(input())
     if num==-1:
          break;
     elif num==0:
          print(downheap(heap))
     else:
          upheap(heap,num)

'''
          
          
