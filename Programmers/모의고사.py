def solution(answers):
    count1 = 0
    count2 = 0
    count3 = 0
    
    pattern1 = [1, 2, 3, 4, 5,]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5,]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    n1 = len(pattern1)
    n2 = len(pattern2)
    n3 = len(pattern3)
    
    for i, answer in enumerate(answers):
        if pattern1[i%n1] == answer:
            count1 += 1
        if pattern2[i%n2] == answer:
            count2 += 1
        if pattern3[i%n3] == answer:
            count3 += 1
    
    max_count = max([count1, count2, count3])
    answer = []
    
    for i, count in enumerate([count1, count2, count3]):
        if count == max_count:
            answer.append(i+1)
    return answer
