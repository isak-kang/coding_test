# 이진 변환 반복하기
# bin -> 2진화 oct, hex
# 내가 한거 진짜 쓰레기 코드.... while문을 잘 안쓰다보니 while문 쓸 생각을 못함....
# whlie, conut, bin 써서 풀기

zero_conut = 0
num_count = 0
one_count = 0

def solution(s):
    answer = []
    global zero_conut,num_count,one_count

    if s == "1":
        answer = [num_count,zero_conut]
        return answer
    else:
        for i in s:
            if i == "1":
                one_count += 1
            else :
                zero_conut += 1
        s = str(bin(one_count)[2:])
        one_count = 0
        num_count +=1
        return solution(s)

s="1111111"

print(solution(s))




# def solutuon(s):
#     a,b = 0,0
#     while s != '1':
#         a += 1 # 몇번 반복하는지
#         num = s.count('1') # 1의 갯수
#         b += len(s) - num # 전체에서 1의 갯수만 뺴기 == 0의 갯수
#         s = bin(num)[2:]
#     return[a,b]