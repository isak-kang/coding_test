from dataclasses import replace
from tokenize import endpats


def solution(book_time):
    book_room = []

    for i in range(len(book_time)):
        h, m = map(int, book_time[i][0].split(":"))
        bt1 = h * 60 + m

        h, m = map(int, book_time[i][1].split(":"))
        bt2 = h * 60 + m + 10

        book_room.append([bt1, bt2])

    book_room = sorted(book_room)
    print(book_room)
    books = []
    for i in range(len(book_room)):
        for k in range(len(books)):
            if books[k] <= book_room[i][0]:
                books[k] = book_room[i][1]
                break
        else:
            books.append(book_room[i][1])
    return len(books)
import datetime

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]






# 처음꺼 확인은 그냥 넘어가
# 두번째꺼는 첫번째꺼 사이에 들어가는지 확인
# 세번째꺼는 1,2 사이에 들어가는지 확인.
# 아니면 룸 마다.?


#For break + else 같이 쓰기 가능.