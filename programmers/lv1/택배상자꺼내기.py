def solution(n, w, num):
    answer = 0
    return answer




n = 22
w =6
num = 8

print(n//w)

delivery_box = []

if n % w == 0:
    height = n // w
else :
    height = n // w + 1

amount_list = []
line_list = []

for i in range(1, n+1):

    line_list.append(i)

    if len(line_list) == w:
        if (i//n) % 2 == 1:
            amount_list.append(line_list)
            line_list.sort(reverse=True)
        else:
            amount_list.append(line_list)
        line_list = []

print(amount_list)
