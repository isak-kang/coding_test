def solution(want, number, discount):
    answer = 0

    for j in range(len(discount) - sum(number)+ 1):
        number_copy = number.copy()
        for i in range(sum(number)):
            print(discount[i+j])
            if discount[i+j] in want:
                wnat_index = want.index(discount[i+j]) 
                if number_copy[wnat_index] != 0:
                    number_copy[wnat_index] -= 1
        
        
                    print("sum",sum(number_copy),number_copy)
        if sum(number_copy) == 0 :
            answer += 1
        
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", 
            "apple", "pork", "banana", "pork", "rice", "pot", 
            "banana", "apple", "banana"]


print(solution(want,number,discount))
