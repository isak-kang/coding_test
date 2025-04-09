a = list(map(int,input().split()))
b = [1,1,2,2,2,8]
c = []
for i in range(len(a)):
    c.append(b[i] - a[i])

for i in c:
    print(i, end=" ")