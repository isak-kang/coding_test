

def solution(name, yearning, photo):

    answer = []

    for photo_people in photo:
        total_score = 0
        for people in photo_people:
            if people in name :
                name_index = name.index(people)
                score = yearning[name_index]
                total_score += score
        answer.append(total_score)


    return answer




