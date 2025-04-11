# distinct_tangerine = set(tangerine)
# count_tang = {}

# for i in distinct_tangerine:
#      count_tang[i] = tangerine.count(i)
# 처음에 이렇게 했느넫 이게 시간복잡도 올리는 길이였음.;;


k= 6	
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

count_tang = {}

for i in tangerine:
     if i in count_tang:
          count_tang[i] += 1
     else : 
          count_tang[i] = 1 

count_tang = sorted(count_tang.items(), key= lambda x: x[1],reverse=True)

result = 0

for i,j in count_tang:
     while k >= 1 :
          k -= j
          
          result += 1
     
