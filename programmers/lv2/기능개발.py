def solution(progresses, speeds):
    count = 1
    day_count = 0
    current_day_count = 0
    answer = []

    day_count_memo = []

    for i in range(len(progresses)):
        progresse = progresses[i]
        speed = speeds[i]

        while progresse < 100: #100일 때 스탑
            progresse += speed
            current_day_count += 1

        day_count_memo.append(current_day_count)   

        if len(day_count_memo) == 1:
            current_day_count = 0
            continue

        if day_count_memo[0] >= current_day_count: #앞에꺼가 뒤에꺼 보다 크다면
            count += 1

        else: #앞에꺼보다 뒤에꺼가 더 크다면
            answer.append(count) 
            day_count_memo = []
            day_count_memo.append(current_day_count)
            count = 1
        
        print(i)
        if i == (len(progresses)-1):
            answer.append(count)

        current_day_count = 0

    return answer


progresses = [95, 90, 99, 99, 80, 99]	

speeds = [1, 1,1,1,1,1]


print(solution(progresses,speeds))

    
