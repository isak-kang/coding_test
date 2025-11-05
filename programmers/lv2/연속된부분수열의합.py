from programmers.lv1.과일장수 import answer


# 첫숫자 기억하고 뒤에꺼 더하기
# 맞으면 인덱스 저장
# 두번째 숫자 기억하고 뒤에꺼 더하고 맞으면
# 앞에꺼 인덱스 길이랑 비교해서 바꾸기.
# 계속 반복?


# def solution(sequence, k):
# k_index = []
# for i in range(len(sequence)):
#     make_k = 0
#
#
#     if sequence[i] == k: # k 와 같은 값이 발견되면 종료하고 그 인덱스 출력하기,
#         return [i,i]
#
#     if i == (len(sequence)-1) : # 마지막이면 그냥 종료.
#         break
#
#     make_k += sequence[i]
#
#     for j in range(i+1,len(sequence)):
#         make_k += sequence[j]
#
#         if make_k > k :
#             break
#         elif make_k == k :
#             k_index.append([i,j])
#
# min_index = 100000000
# min_index_list = []
# for i,j in k_index:
#     if min_index > (j-i):
#         min_index_list = [i,j]
#         min_index =(j-i)
#
#
# return min_index_list
#

# 시간 복잡도 너무 높음.


# def solution(sequence, k):
#     count =0
#     k_index = []
#     for i in range(len(sequence)-1,-1,-1):
#         count += 1
#         make_k = 0
#         if sequence[i] == k:
#             return [i,i]
#
#         if i ==  0: # 마지막이면 그냥 종료.
#             break
#         make_k += sequence[i]
#
#         for j in range(len(sequence)-1-count,-1,-1):
#             make_k += sequence[j]
#
#             if make_k > k :
#                 if k_index :
#                     return k_index
#                 break
#
#             elif make_k == k :
#                 if not k_index:
#                     k_index = [j,i]
#                     break
#
#                 if (k_index[1] - k_index[0]) < (i -j):
#                     return k_index
#                 else :
#                     k_index = [j,i]
#                     break
#
#     return k_index

def solution(sequence, k):
    sum_sequence = 0
    end = 0
    min_len = len(sequence)

    for start in range(len(sequence)):

        while end < len(sequence) and sum_sequence < k:
            sum_sequence += sequence[end]
            end += 1
        if sum_sequence == k and end - start < min_len:
            answer = [start,end-1]
            min_len = end-1-start
        sum_sequence -= sequence[start]

    return answer




sequence = [2, 2, 2, 2, 2, 2]
k = 6

print(solution(sequence,k))