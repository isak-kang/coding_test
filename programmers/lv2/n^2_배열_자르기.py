# 인텍스를 좌표로 변환

# 1 2 3 4 5 / 2 2 3 4 5 / 33345 /44445/55555
# 

def solution(n, left, right):
    answer = []
    
    for i in range(left,right+1): # 2,6 // 2,3,4,5
        answer.append(max(i//n,i%n)+1) # 2//5 2%5 2
    return answer


    # one_line = list(range(1,n+1))

    # for i in range(1,n+1):
    #     one_line_copy = one_line.copy()
    #     print(one_line_copy)
    #     one_line_copy[:i] = [i]* i
    #     print(one_line_copy)
    #     answer.extend(one_line_copy)


    # for j in range(1,n+1):
    #     for i in range(1,n+1):
    #         if i < j : 
    #             answer.append(j)
                
    #         else :
    #             answer.append(i)

    # answer = answer[left:right+1]
    # return answer

n = 3
left = 2
right = 5
result = [3,2,2,3]

answer=[]


print(solution(n,left,right))
    