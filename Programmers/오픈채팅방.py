def solution(record):
    
    
    answer = []
    
    db = {}
    
    for r in record:
        if r.split()[0] == 'Leave':
            continue
            
        cmd, uid, name = r.split()
        if cmd == 'Enter' or cmd == 'Change':
            db[uid] = name
    
    for r in record:
        if r.split()[0] == 'Enter':
            _, uid, _ = r.split()
            answer.append('{}님이 들어왔습니다.'.format(db[uid]))
        if r.split()[0] == 'Leave':
            _, uid = r.split()
            answer.append('{}님이 나갔습니다.'.format(db[uid]))

    return answer
