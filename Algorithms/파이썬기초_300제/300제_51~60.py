#51
movie_rank = ['닥터스트레인지', '스플릿', '럭키']
print(movie_rank)

#52
movie_rank.append('배트맨')
print(movie_rank)

#53 : insert로 원하는 인덱스에 요소 추가, (index,object)
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

#54 : del list[index]
del movie_rank[3]
print(movie_rank)

#55
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#57
nums = [1, 2, 3, 4, 5, 6, 7]
print('max:', max(nums))
print('min:', min(nums))

#58: sum 함수가 있음
nums = [1, 2, 3, 4, 5]
Sum = 0
for i in range(len(nums)):
    Sum += nums[i]
print(Sum)
print(sum(nums))

#59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))