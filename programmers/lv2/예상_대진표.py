import math

def solution(n,a,b):
    answer = 0

    a_participant = min(a,b)
    
    b_participant = max(a,b)
    
    count = 0
    
    while (n != 1) :
        count += 1
        
        if (abs((a_participant - b_participant)) == 1) and (a_participant % 2 == 1):
            return count
        a_participant = participant(a_participant)
        print(a_participant)
        
        b_participant = participant(b_participant)
        print(b_participant)
        
        n = n // 2
        # print(n)
        # print(count)
        
    # return 

def participant(a):
    if a % 2 == 1 :
        a = a // 2 + 1
    else :
        a = a // 2

    return a
    

n = 8
a = 4
b = 7

print(solution(n,a,b))

# print(participant(b))
