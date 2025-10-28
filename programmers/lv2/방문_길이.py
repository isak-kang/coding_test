# start 2025.10.25 8:50
# end 2025.10.25 9:20

def solution(dirs):
    total_memo = []
    start_dot = [0,0]
    count = 0
    for dir in dirs:
        memo = []
        memo.append(start_dot)
        if dir == "U":
            if (start_dot[1] +1) > 5 :
                continue
            end_dot = [start_dot[0], start_dot[1]+1]
            memo.append(end_dot)

        elif dir == "D":
            if (start_dot[1] -1) < -5 :
                continue
            end_dot = [start_dot[0], start_dot[1]-1]
            memo.append(end_dot)
            
        elif dir == "L":
            if (start_dot[0] -1) < -5 :
                continue
            end_dot = [start_dot[0]-1, start_dot[1]]
            memo.append(end_dot)
            
        else :# dir == "R"
            if (start_dot[0] +1) > 5 :
                continue
            end_dot = [start_dot[0]+1, start_dot[1]]
            memo.append(end_dot)


        if memo not in total_memo and list(reversed(memo)) not in total_memo: # 현재 점이 저장된 점과 같지 않을 때 +1
            count += 1

        total_memo.append(memo)
        start_dot = end_dot
    return count

dirs = "ULLLLLLU"



print(solution(dirs))