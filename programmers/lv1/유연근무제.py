def solution(schedules, timelogs, startday):
    available_time = []

    fail = 0
    for i in range(len(schedules)):
        day = startday
        available_time.append(schedules[i])
        for _ in range(10):
            schedules[i] += 1
            
            if schedules[i] % 100 >= 60:
                schedules[i] = 100 + schedules[i] - (schedules[i]%100)

            available_time.append(schedules[i])
        print(available_time)
        for j in range(7):
            
            if day == 8:
                day = 1

            elif day == 6 or day == 7 :
                day += 1
                continue
            
            # day 1~5
            if timelogs[i][j] not in available_time and timelogs[i][j] > schedules[i]:
                print(day,timelogs[i][j])
                fail +=1
                break
            
            day += 1
        
        available_time = []
    return len(schedules)-fail



timelogs = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
schedules = [730, 855, 700, 720]
startday = 1 #금
# 6 55 - 7 05



print (solution(schedules, timelogs, startday))