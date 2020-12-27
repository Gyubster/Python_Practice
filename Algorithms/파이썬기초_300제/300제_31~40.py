#31

#32

#33

#34
t1 = 'python'
t2 = 'java'
t = t1 + ' ' + t2 + ' '
print(t*4)

#35 - % formatting: %s를 이용. 내용 %s % (가지고올 것.) 선호 x
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s, 나이: %s" % (name1, age1))
print("이름: %s, 나이: %s" % (name2, age2))

#36 - %format 보다 선호
print("이름: {}, 나이: {}".format(name1, age1))
print("이름: {}, 나이: {}".format(name2, age2))

#37 - 가장 최근. 훨씬 직관적
print(f"이름: {name1}, 나이: {age1}")
print(f"이름: {name2}, 나이: {age2}")

#38
상장주식수 = "5,969,782,550"
상장주식수2 = 상장주식수.replace(',','')
print(int(상장주식수2))

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#40 - strip은 strip('지우고 싶은 내용')
data = "   삼성전자    "
data2 = data.strip(' ')
print(data2)