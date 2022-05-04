import math

def toMin(time):
    HH, MM = map(int, time.split(':'))
    return HH * 60 + MM

def solution(fees, records):
    
    baseTime, baseFee, unitTime, unitFee = map(int, fees)
    
    lastInTime = dict()
    total = dict()
    
    for record in records:
        time, carId, state = record.split()
        
        if carId not in total:
            total[carId] = 0
        
        if state == 'IN':
            lastInTime[carId] = toMin(time)
        else:
            inTime = lastInTime[carId]
            lastInTime[carId] = -1
            outTime = toMin(time)
            total[carId] += (outTime-inTime)
    
    lastTimeOfTheDay = toMin('23:59')
    for carId, inTime in lastInTime.items():
        if inTime >= 0:
            total[carId] += (lastTimeOfTheDay - inTime)
        
    
    res = list(total.items())
    res.sort()
    
    answer = []
    # print(res)
    for r in res:
        carId, totalTime = r
        
        if totalTime <= baseTime:
            answer.append(baseFee)
        else:
            answer.append(baseFee + math.ceil((totalTime-baseTime)/unitTime)*unitFee)
        
    return answer
