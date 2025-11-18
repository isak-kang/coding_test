

def solution(x, y, n):
    x_copy = x
    count = 0
    count_list = []
    x_add_count = 1
    a = True

    while a :
        count = 0
        x = x_copy

        if x*(2*x_add_count) < x+(n*x_add_count):
            x += (n * x_add_count)
            count += x_add_count
            x_add_count += 1
        else :
            a = False

        if x > y :
            break

        while x < y:
            if (y/x) % 3 == 0 :
                x *= 3
            elif (y/x) % 2 == 0 :
                x *= 2
            else :
                x += n
            count += 1

        if x == y :
            count_list.append(count)


    if count_list :
        return max(count_list)
    else :
        return -1


x = 10
y = 80
n = 30
print(solution(x, y, n))

# 2,3 으로 나눠지는가?
# 안나누어 진다면 더하기

# 근데 만약에








# 먼저 나누어 지는지 확인 안되면 더하기. 어때?
