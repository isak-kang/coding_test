def solution(cards1, cards2, goal):

    for i in goal:
        if cards1 :
            if i == cards1[0] :
                cards1.pop(0)
                print(i)
                continue
        if cards2:
            if i == cards2[0]:
                cards2.pop(0)
                print(i)
                continue
        return "No"
    return "Yes"

goal = ["i", "want", "to", "drink", "water"]
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]

print(solution(cards1,cards2,goal))