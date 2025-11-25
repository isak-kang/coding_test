def solution(wallet, bill):
    answer = 0
    wallet.sort(reverse=True)
    bill.sort(reverse=True)


    while wallet[0] < bill[0] or wallet[1] < bill[1] :
        answer += 1
        bill[0] = bill[0] // 2

        bill.sort(reverse=True)

    return answer


wallet = [50, 50]
bill = [100, 241]

