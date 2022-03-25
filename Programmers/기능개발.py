import math

def solution(progresses, speeds):
    n = len(progresses)
    queue = []
    answer = []
    
    
    leftdays = []
    
    for i in range(n):
        leftdays.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    gijun = 0 # 이 인덱스의 작업이 끝날때까지 뒤에 있는 것들은 끝날 수 없음
    count = 1 # 배포되지 못하고 쌓여있는 작업의 갯수
    
    for i in range(1, n):
        if leftdays[i] <= leftdays[gijun]:
            count += 1
        else:
            answer.append(count) # 배포되지 못하고 쌓여있던 것
            gijun = i
            count = 1
    
    answer.append(count)
        
    return answer
