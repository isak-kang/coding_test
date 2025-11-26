def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[0:2]) * 60 + int(video_len[3:5])
    pos = int(pos[0:2]) * 60 + int(pos[3:5])
    op_start = int(op_start[0:2]) * 60 + int(op_start[3:5])
    op_end = int(op_end[0:2]) * 60 + int(op_end[3:5])


    if pos <= op_end and pos >= op_start:
        pos = op_end



    for command in commands:

        if command == "prev":
            if pos - 10 < 0:
                pos = 0
            else :
                pos -= 10
        elif command == "next":
            if pos + 10 > video_len:
                pos = video_len
            else :
                pos += 10
        if pos <= op_end and pos >= op_start:
            pos = op_end



    pos = f"{pos // 60:02d}:{pos%60:02d}"
    return pos

video_len = "34:33"
pos = "13:00"
op_start = "00:55"
op_end	 = "02:55"
commands	=["next", "prev"]



