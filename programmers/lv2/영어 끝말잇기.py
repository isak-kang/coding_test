def solution(n, words):
    answer = []

    use_words = []

    for i in range(len( words)):
        if words[i] in use_words :
            use_words.append(words[i])
            if len(use_words) % n == 0:
                a = n
                b = len(use_words) // n
            else:
                a = len(use_words) % n
                b = len(use_words) // n +1
            return [a, b]
        
        if use_words:
            if words[i][0] != use_words[-1][-1]:
                use_words.append(words[i])
                if len(use_words) % n == 0:
                    a = n
                    b = len(use_words) // n
                else:
                    a = len(use_words) % n
                    b = len(use_words) // n +1
                return [a, b]
    
        use_words.append(words[i])

        


        # for i in range(j,len(words),n):
        #     if words[i] in use_words :
        #         a.append(words[i])
        #         b = [j+1, len(a)]
        #         return b
        #     a.append(words[i])
        
        
            
        print(use_words)
    
            




    return [0,0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print (solution(n,words))

