def solution(friends, gifts):
    answer = 0
    memo = {}

    for i in friends :
        memo[i] = {}
        for j in friends:
            memo[i][j] = 0

    print(memo)



    for gift in gifts:
        giver, receiver = gift.split()

        # print(memo)
        if receiver in memo[giver]:
            memo[giver][receiver] += 1

        if giver in memo[receiver]:
            memo[receiver][giver] -= 1


    next_gifts = []
    sum_gift_ratio = {}

    print(memo)

    for i in memo.keys():
        sum_gift_ratio[i] = sum(memo[i].values())
        # print(sum_gift_ratio)



    for friend in friends:
        count = 0
        for i in memo[friend]: #i = 
            # print(memo[friend][i])
            # print(sum_gift_ratio[i])

            if memo[friend][i] > 0 :
                count += 1
                # print(count)
            elif memo[friend][i] ==0 :
                if sum_gift_ratio[friend] > sum_gift_ratio[i]:
                    count += 1
        next_gifts.append(count)

    return max(next_gifts)



friends = ["joy", "brad", "alessandro", "conan", "david"]

gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]




        
        


pritn(s)

        


{"muzi": {"ryan : 1"}}

total_gifts = []
        