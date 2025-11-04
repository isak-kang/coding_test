def solution(diffs, times, limit):
    def get_amount_time(mid) :
        amount_time = 0
        time_prev = 0
        for j in range(len(diffs)):
            if mid >= diffs[j]:
                amount_time += times[j]
            elif mid < diffs[j]:
                amount_time += (diffs[j]-mid) * (time_prev+times[j]) + times[j]
            time_prev = times[j]
        return amount_time

    left,right = 1,max(diffs)

    while left <= right:
        mid = (left+right) // 2
        amount_time = get_amount_time(mid)

        if amount_time <= limit:
            answer = mid
            right = mid - 1  # 더 낮은 level 가능한지 탐색
        else:
            left = mid + 1  # level 올려야 함

    return answer


diffs = [1, 328, 467, 209, 54]
times = [2, 7, 1, 4, 3]
limit = 1723


