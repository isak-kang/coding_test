def solution(citations):
    citations.sort()
    for i in range(1,len(citations)+1): # 1112 45 1이상인거니깐.
        count = 0
        for citation in citations: # 1, 1
            if i <= citation: #1, 0
                count += 1
            if count == i:
                break
        if count < i :
            return (i-1)
    return len(citations)




# n편의 논문.
# h번 이상 인ㅇ용된 논문이 h편 이상.
# 나머지 논문이 h의 최댓값이 

# 일단 다 더해 # 갯수 구해.




# 9 7 6 2 1 ->3회 이상이 3개
# -> 6
# 97 321
# ->3
# 978 661 -> 5회 이상이 5개
# 100 100 0 0 -> 2회 이상이 2개. (2)

# 1 1 1 1 1 2 -> 1이상인게 1개 이상 


# 978

# 아니면 9 7 6 2 1 -> 1보다 높은걸 찾아 근데 그게 i개 이상이 됐을 때 스탑.
citations = [1]
print(solution(citations))


        