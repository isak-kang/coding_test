

def solution(k, score):
    top=[]
    answer = []
    for i in score:
        if k-1 >= len(top) :
            top.append(i)

        else:
            if top[k-1] < i :
                top.pop(k-1)
                top.append(i)
        print(top)
        top.sort(reverse=True)
        answer.append(top[-1])
        print(answer)
    return answer

score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]



p