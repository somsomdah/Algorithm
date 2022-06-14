def solution(new_id):
    new_id = new_id.lower()
    tmp = ''
    
    for ch in new_id:
        if ch.isalpha():
            tmp += ch
        elif ch.isnumeric():
            tmp += ch
        elif ch in ['-','_','.']:
            tmp += ch
        else:
            continue
    if tmp == '': tmp += 'a'
    
    while '..' in tmp:
        tmp = tmp.replace('..','.')
    if tmp == '': tmp += 'a'
        
    if tmp[0] == '.': tmp = tmp[1:]
    if tmp == '': tmp += 'a'
    
    if tmp[-1] == '.': tmp = tmp[:-1]
    if tmp == '': tmp += 'a'
    
    if len(tmp) >= 16: tmp = tmp[:15]
    if tmp[-1] == '.': tmp = tmp[:-1]
    
    if len(tmp) <= 2:
        while len(tmp) < 3:
            tmp += tmp[-1]
    
    
    
    
    answer = tmp
    return answer
