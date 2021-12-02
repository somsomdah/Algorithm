def solution(numbers, target):
    n=len(numbers)
    count=0
    
    def DFS(L,sum_):
        nonlocal count
        if L==n:
            if sum_==target:
                count+=1
        else:
            DFS(L+1,sum_-numbers[L])
            #DFS(L+1,sum_)
            DFS(L+1,sum_+numbers[L])
    DFS(0,0)
    answer = count
    return answer
