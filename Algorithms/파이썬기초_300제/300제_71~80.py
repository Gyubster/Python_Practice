#71
my_variable = ()
print(type(my_variable))

#72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

#73 - ,를 넣어주어야 꼭 하나의 튜플로 인식. 안그러면 정수로 인식
my_tuple = (1, )

#74

#75

#76

#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest2 = list(interest)
print(interest2, type(interest2))

#78
interest3 = tuple(interest2)
print(interest3, type(interest3))

#79 -> 튜플에서만 되는건지?
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80 -> range(start, end, stride)
data = tuple(range(2, 100, 2))
print(data)
