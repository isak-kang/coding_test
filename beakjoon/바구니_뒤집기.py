# 바구니 뒤집기
n,m = map(int,input().split())
a = [i for i in range(1, n+1)]

for i in range(m):
    j, k = map(int,input().split())
    b = a[j-1:k]
    b.reverse()
    a[j-1:k] = b
print(a)

for i in a:
    print(i,end= " ")