# 처음에 완전 잘못 생각함. 최대 2명인줄 몰랐음.....

def solution(people, limit):
    
    people.sort()

    start = 0
    end = len(people) - 1

    a = 0

    while start <= end :
        if people[start] + people[end] > limit:
             end -= 1
        else :
             start += 1
             end -= 1
        a += 1
        
    return a
