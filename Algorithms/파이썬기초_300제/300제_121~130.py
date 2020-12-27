#121 - islower
word = input()
if word.islower():
    word = word.upper()
else:
    word = word.lower()
print(word)

#122
Score = int(input())
if Score>=81:
    print('A')
elif 61 <= Score <= 80:
    print('B')
elif 41 <= Score <= 60:
    print('C')
elif 21 <= Score <= 40:
    print('D')
elif 0 <= Score <= 20:
    print('E')

#123
Amount, MoneyType = input().split()
Amount = float(Amount)
if MoneyType == '달러':
    Total = Amount * 1167
    print(Total, '원')
elif MoneyType =='엔':
    Total = Amount * 1.096
    print(Total, '원')
elif MoneyType =='유로':
    Total = Amount * 1268
    print(Total, '원')
elif MoneyType =='위':
    Total = Amount * 171
    print(Total, '원')

환율 = {"달러": 1167,
      "엔": 1.096,
      "유로": 1268,
      "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

#124

#125
TelecomDict = {'011': 'SKT', '016': 'KT', '019': 'LGU', '010': '알수없음'}
PhoneNumber = input()
Front = PhoneNumber[0:3]
print('당신은', TelecomDict[Front],'사용자입니다.')

number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

#126 ~ #130


