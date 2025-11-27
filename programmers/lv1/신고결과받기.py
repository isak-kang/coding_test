def solution(id_list, report, k):
    report=set(report)
    print(report)
    answer = [0] * len(id_list)

    memo = {}
    report_numbers = {}
    for id in id_list:
        memo[id] = []
        report_numbers[id] = 0

    for i in report:
        i_list = list(map(str, i.split(" ")))
        j,v = i_list[0],i_list[1]
        memo[j].append(v)
        report_numbers[v] += 1

    print(report_numbers,memo)

    for key in report_numbers:

        if int(report_numbers[key]) >= k :
            for y in memo.keys():
                if key in memo[y]:
                    answer[id_list.index(y)] += 1


    return answer

id_list= ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list,report,k))






