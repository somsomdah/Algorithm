def solution(places):
    
    answer = []
    
    
    for place in places:
        
        spots = []
        blocks = []
        
        nearests = []
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    for spot in spots:
                        x, y = spot
                        if abs(x-i) + abs(y-j) <= 2:
                            nearests.append([spot, (i, j)]) # 맨해튼 거리가 2 이하인 경우
                    spots.append((i, j))
                elif place[i][j] == 'X':
                    blocks.append((i, j))
                    
        # print(nearests)
        # print(blocks)
        # print()
        
        flag  = 0
        for near in nearests:
            (x1, y1), (x2, y2) = near
            dx = abs(x1-x2)
            dy = abs(y1-y2)
            
            if (dx == 1 and dy == 0) or (dx == 0 and dy == 1): # 둘이 붙어 있는 경우
                answer.append(0)
                flag = 1
                break
                
            elif dx == 1 and dy == 1:
                if (x1, y2) in blocks and (x2, y1) in blocks:
                    continue
                else:
                    answer.append(0)
                    flag = 1
                    break
                    
            elif dx == 2 and dy == 0:
                if (min(x1, x2)+1, y1) in blocks:
                    continue
                else:
                    answer.append(0)
                    flag = 1
                    break
                    
            elif dy == 2 and dx == 0:
                if (x1, min(y1, y2) + 1) in blocks:
                    continue
                else:
                    answer.append(0)
                    flag = 1
                    break
                    
        if flag == 1:
            continue
        else:
            answer.append(1)
                
        
    return answer
