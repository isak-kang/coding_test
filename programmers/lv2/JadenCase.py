#JadenCase 
# capitalize() 함수사용 -> 첫글자 대문자 나머지 소문자
# title도 있음. -


def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for     the last week"))

def solution(s):
    answer = ""
    capitalize_next = True

    for char in s:
        if char == " ":
            answer += char
            capitalize_next = True 
        else:
            if capitalize_next:
                answer += char.upper()
            else:
                answer += char.lower()
            capitalize_next = False 
    
    return answer






# 공백이 2개 이상일 떄 안됨....
def solution(s):
    answer = ''
    
    s = "for the     last week"	

    s_split = s.split()
    s_save =[]
    for i in s_split:
        
        i = i[0].upper()+i[1:].lower()
        
        s_save.append(i)

    print(s_save)

    answer = " ".join(s_save)

    
    return answer


s = "for the     last week"	

s_split = s.split()
s_save =[]
for i in s_split:
    
    i = i[0].upper()+i[1:].lower()
    
    s_save.append(i)

print(s_save)



print(" ".join(s_save))

