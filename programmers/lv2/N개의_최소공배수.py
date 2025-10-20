
def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = lcm(answer, arr[i])
        print(f"arr {i-1}과 {i}의 최소공배수: {answer}")
    return answer


arr = [2,6,8,14]

def gcd(a,b):
    while b:
        a,b = min(a,b),  max(a,b)
        if b%a == 0: # 6 8 
            return a 
        b = b%a 

def lcm( a,b ):
    print(a, b, gcd(a,b))
    answer = (a*b) / gcd(a,b)
    return answer


# print(answer)
print(solution(arr))

