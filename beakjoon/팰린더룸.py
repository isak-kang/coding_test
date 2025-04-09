a = input().upper()
a_list = list(set(a))
b = []

for i in a_list:
    count = a.count(i)
    b.append(count)

if b.count(max(b)) >= 2:
    print("?")
else:
    print(a_list[b.index(max(b))])