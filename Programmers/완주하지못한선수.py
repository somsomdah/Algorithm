
def solution(participant, completion):
    temp = set(participant) - set(completion)
    if temp:
        return list(temp)[0]
    else:
        for c in completion:
            if completion.count(c) != participant.count(c):
                return c
        else:
            return 0
