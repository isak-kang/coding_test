def solution(board, h, w):
    answer = 0
    return answer

board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 3
w = 3

dh = [1,-1,0,0]
dw = [0,0,1,-1]
count = 0
color = board[h][w]

for i in range(4):
    dh_num = h + dh[i]
    dw_num = w + dw[i]

    if dh_num < 0 or dh_num > (len(board)-1):
        continue
    elif dw_num < 0 or dw_num > (len(board[0])-1):
        continue

    if board[dh_num][dw_num] == color:
        count += 1


print(count)
