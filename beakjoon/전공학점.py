n = 20
total = 0

for i in range(20):
    major = input().split()
    # score = int(major[1]) * int(major[2])
    # print(score)

    if major[2] == "A+" :
        score += int(major[1]) * 4.5
        score2 += int(major[1])
    if major[2] == "A0" :
        score2 += int(major[1])
        score += int(major[1]) * 4.0
    if major[2] == "B+" :
        score2 += int(major[1])
        score += int(major[1]) * 3.5
    if major[2] == "B0" :
        score2 += int(major[1])
        score += int(major[1]) * 3.0
    if major[2] == "C+" :
        score2 += int(major[1])
        score += int(major[1]) * 2.5
    if major[2] == "C0" :
        score2 += int(major[1])
        score += int(major[1]) * 2.0
    if major[2] == "D+" :
        score2 += int(major[1])
        score += int(major[1]) * 1.5
    if major[2] == "D0" :
        score2 += int(major[1])
        score += int(major[1]) * 1.0
    if major[2] == "F" :
        score2 += int(major[1])
        score += int(major[1]) * 0
    if major[2] == "P" :
        pass

total = score / score2

print(total)


    