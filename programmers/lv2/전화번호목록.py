from fcntl import FASYNC


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        number_length = len(phone_book[i])

        if number_length >= len(phone_book[i+1]):
            continue

        if phone_book[i] in phone_book[i+1][:number_length]:
            return False
    return True


phone_book = ["12","123","1235","567","88"]

# 123 456 4567

# 11 12 123 111





print(solution(phone_book))




