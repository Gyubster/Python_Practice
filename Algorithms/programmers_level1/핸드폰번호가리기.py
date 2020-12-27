def solution(phone_number):

    print(PhoneNumberList)
    answer = phone_number
    return answer

phone_number = '"01033334444"'
PhoneNumberList = list(map(str, str(phone_number)))
for i in range(1, len(PhoneNumberList)-5):
    PhoneNumberList[i] = '*'
print(''.join(PhoneNumberList))
