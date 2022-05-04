def solution(id_list, report, k):
    
    report = list(set(report)) # 중복 제거
    report_dict = dict()
    count = dict()
    
    for id in id_list:
        report_dict[id] = []
        count[id] = 0
        
    for r in report:
        reporter,  reported = r.split()
        report_dict[reporter].append(reported)
        count[reported] += 1
    
    result = []
    for id in id_list:
        reported = report_dict[id]
        tmp = 0
        for r in reported:
            if count[r] >= k:
                tmp += 1
        result.append(tmp)
    
    return result
