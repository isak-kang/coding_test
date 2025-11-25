import string
def solution(s, skip, index):
    answer = ''
    ascii_words = [i for i in string.ascii_lowercase if i not in skip]

    for i in s:
        pos = ascii_words.index(i)
        char = ascii_words[(pos+index)%len(ascii_words)]
        answer += char




    return answer
