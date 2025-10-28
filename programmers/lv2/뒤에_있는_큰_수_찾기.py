# start 2025.10.27 9:25
# end 2025.10.27 9:35

# 틀림 (시간복잡도가 너무 높음.) -> 스택방식으로 수정.

# def solution(numbers):
#     answer = []

#     for i in range(len(numbers)): # # O(N)
#         if max(numbers[i:]) == numbers[i]: # O(N) -> # O(N^2)
#             answer.append(-1)
#             continue
        
#         else:
#             for j in numbers[i+1:]:
#                 if j > numbers[i]:
#                     answer.append(j)
#                     break
#     return answer



def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)

    return answer

numbers = [9,1,5,3,6,2]

print(solution(numbers))