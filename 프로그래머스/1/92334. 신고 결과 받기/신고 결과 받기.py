from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dic = defaultdict(set)
    email_dic = defaultdict(int)
    
    for i in range(len(report)):
        report_from, report_to = report[i].split()
        report_dic[report_to].add(report_from)

    for report_to, reporters in report_dic.items():
        if len(reporters) >= k:
            for reporter in reporters:
                email_dic[reporter] += 1
    
    for name in id_list:
        answer.append(email_dic[name])
    
    return answer