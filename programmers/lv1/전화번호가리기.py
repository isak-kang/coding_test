def solution(phone_number):
    answer = ''

    phone_len = len(phone_number) # 5

    if phone_len > 4:
        for i in phone_number[0:phone_len-4]:
            answer += "*"

    else :
        return phone_number

    answer += phone_number[phone_len-4:]

    return answer


phone_number = "01033334444"

print(solution(phone_number))
