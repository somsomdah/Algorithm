import heapq

def solution(scoville, K):
    
    heap = []
    count = 0
    
    for s in scoville:
        heapq.heappush(heap, s)
        
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        
        tmp = a + b * 2
        heapq.heappush(heap, tmp)
        
        count += 1
        
        if heap[0] >= K:
            return count
            
    return -1
