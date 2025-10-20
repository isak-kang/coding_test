def solution(s):
    s_list = []
    count = 0
    for i in range(len(s)):
        s_list = []
        count_a =0
        # print(s)
        for j in range(len(s)):
            # print(s[j])
            if s[j] == "[" or s[j] == "(" or s[j] == "{" :
                s_list.append(s[j])
                # print(s_list)

            else:
            # print(1)
                if not s_list:
                    break
                if s[j] == "]" and "[" != s_list[-1]:
                    break 
                if s[j] == ")" and "(" != s_list[-1] :
                    break
                if s[j] == "}" and "{" != s_list[-1]:
                    break

                s_list.pop(-1)

            count_a += 1
            # print(count_a)
            
        if count_a == len(s) and not s_list:
            count += 1
        s = s[1:]+s[0]
        
    return count


s = "}]()[{"

print(solution(s))
