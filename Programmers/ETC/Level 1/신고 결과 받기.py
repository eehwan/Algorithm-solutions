def solution(id_list, report, k):
    report_cnt = {x : 0 for x in id_list}   # x가 신고당한 횟수
    report_list = {x : [] for x in id_list} # x를 신고한 사람
    result = [0 for _ in range(len(id_list))]
    for r in set(report):
        a,b = r.split(" ")
        report_cnt[b] += 1
        report_list[b].append(a)
    for x in report_list.keys():
        if report_cnt[x] >= k:
            for reporter in report_list[x]:
                _index = id_list.index(reporter)
                result[_index] += 1
    return result