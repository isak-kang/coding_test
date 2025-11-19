def solution(array, commands):
    answer = []

    for command in commands:
        arr_command = []

        first_idx = command[0]
        last_idx = command[1]
        select_idx = command[2]

        arr_command = array[first_idx-1:last_idx]
        arr_command.sort()
        answer.append(arr_command[select_idx-1])


    return answer



array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


print(solution(array,commands))