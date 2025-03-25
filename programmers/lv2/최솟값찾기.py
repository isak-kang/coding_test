# 최솟값찾기(두개의 리스트에서 한숫자 곱하고 더해서 가장 낮게 만들어라.)


def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
        
    print(answer)
    return answer

# 처음에는 정렬하지 않고 max, min으로 찾고 remove로 지우면서 했는데 이렇게 하면 시간 복잡도가 O(n log n)이 되서 속도가 안남.





# def solution(A,B):
#     answer = 0
    
#     for i in range(len(A)):
#         a_min = min(A)
#         b_max = max(B)

#         answer += a_min * b_max

        
#         A.remove(a_min)
#         B.remove(b_max)
#     print(answer)
#     return answer

A = [1,2,3]
B = [4,5,6]

solution(A,B)

