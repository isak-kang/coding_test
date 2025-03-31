# math함수 최대 공약수 gcd / 최소 공배수 lcm 
def solution(brown, yellow):
    total = brown+yellow
    save = []
    for i in range(1, int(total**(1/2)) + 1):
        if total % i == 0:
            j = total / i 
            save.append((i,int(j)))
    print(save)

    for i,j in save:
        print(i,j)
        if (i-2)*(j-2) == yellow:
            return [j,i] 


print(solution(24,24))
