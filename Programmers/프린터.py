def solution(priorities, location):
    answer = 0
    queue = priorities[:]
    pos = location
    
    while(queue):
        
        print(queue, pos)
        n = len(queue)
        tmp = queue.pop(0)
        
        
        for q in queue:
            if q > tmp:
                queue.append(tmp)
                break
        else:
            answer += 1
            if pos == 0:
                break
                
        pos = (pos-1) % n
                
    return answer
