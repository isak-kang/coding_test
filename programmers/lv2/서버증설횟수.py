def solution(players, m, k):
    
    servers = [0] * 100

    count = 0

    for i in range(len(players)):
        server = players[i] // m #필요한 서버수

        add_server = server - servers[i] # 원래있던 서버 수에서 더해야하는 서버 수
        if add_server > 0:
            for j in range(k):
                servers[i+j] += add_server

        
            count += add_server
    return count


# m 명 늘어날 때 서버 +1
# k는 증설된거 가지고 있는 시간.
# 

players = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
m = 5
k = 1



print(solution(players, m, k))