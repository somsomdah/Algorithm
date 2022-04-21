def solution(rows, columns, queries):
    
    board = [[i for i in range(j*columns+1, (j+1)*columns+1)] for j in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries:
        h, w = x2-x1, y2-y1

        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        copy = [b[:] for b in board]        
        
        if h == 0 or w == 0:
            answer.append(min([min(b[y1:y2+1]) for b in board[x1:x2+1]]))
            continue
            
        else:
            lst = []
            lst.extend(board[x1][y1:y2+1])
            lst.extend(board[x2][y1:y2+1])
            lst.extend([b[y1] for b in board[x1:x2+1]])
            lst.extend([b[y2] for b in board[x1:x2+1]])
            # print(lst)
            answer.append(min(lst))
        
        # 회전
        board[x1][y1+1:y2+1] = copy[x1][y1:y2]
        board[x2][y1:y2] = copy[x2][y1+1:y2+1]
        
        for i in range(x1, x2):
            board[i][y1] = copy[i+1][y1]
        
        for i in range(x1+1, x2+1):
            board[i][y2] = copy[i-1][y2]
            
        # for b in board:
        #     print(b)
        # print('```````````````````````')


    
    return answer
