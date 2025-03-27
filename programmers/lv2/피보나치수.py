# 원래는 아래처럼 재귀함수 사용했는데 런타임에러났음 . 찾아보니 재귀에 깊이 제한이 있는거임...
# 그래서 변수를 이용한 반복문을 이용하는게 좋음.

def solution(n):
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, (a + b) 
    
    return b % 1234567

# memo = {1 : 1, 2: 1}

# def solution(n):

#     if n not in memo: 
#         memo[n] = solution(n-1) + solution(n-2)
#         return memo[n]
    
#     else:
#         return memo[n]



# n = 30

# print(solution(n))