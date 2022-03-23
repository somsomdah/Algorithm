
def solution(phoneBook):
    
    phoneBook = sorted(phoneBook)
    ### 사전순으로 정렬하기 때문에 서로 인접한 것끼리의 앞자리가 가장 유사하다. ###
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
