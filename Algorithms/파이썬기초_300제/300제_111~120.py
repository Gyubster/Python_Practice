#111
user = input('입력:')
print(user * 2)

#112
user1 = int(input('숫자를 입력하세요:')) + 10
print(user1)

#113
user2 = int(input())
if user2%2 == 0:
    print('짝수')
else:
    print('홀수')

#114
user3 = int(input()) + 20
if user3 > 255:
    print(255)
else:
    print(user3)

#115
user4 = int(input()) - 20
if user3 < 0:
    print(0)
else:
    print(user4)

#116
time = input('현재시간:')
if time[-2:] == 00:
    print('정각입니다.')
else:
    print('정각이아닙니다.')

#117~ #118
fruit = ["사과", "포도", "홍시"]
FruitQuestion = input('좋아하는 과일은?')
if FruitQuestion in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

#119 dic의 경우에도 in dict.values(), in dict.keys()로 체크가능.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
Season = input('좋아하는 계절은?')
if Season in fruit():
    print('정답입니다.')
else:
    print('오답입니다.')

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
Season = input('좋아하는 과일은?')
if Season in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')