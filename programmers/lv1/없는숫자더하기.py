def solution(numbers):
    answer = -1
    return answer


numbers = [1,2,3,4,6,7,8,0]

total_numbers = [0,1,2,3,4,5,6,7,8,9]

add_number = 0

for number in numbers:
    if number in total_numbers:
        add_number += number
        print(number)
print(45-add_number)