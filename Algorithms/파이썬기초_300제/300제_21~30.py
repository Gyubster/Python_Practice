# 21번
letters = 'python'
print(letters[0], letters[2])

# 22번 - 슬라이싱. [시작:끝]/ 안쓸시에는 0으로 인식
license_plate = "24가 2210"
print(license_plate[-4:])

# 23번 - [start:end:stride] / stride는 간격 / 거꾸로 가능
string = "홀짝홀짝홀짝"
print(string[::2])

# 24번
string = "PYTHON"
print(string[::-1])

# 25번 - replace('old', 'new')
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', ' ')
print(phone_number1)

# 26번
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')
print(phone_number1)

# 27번 - split('standard')로 나누어 리스트로 표현이된다. 이를 호출.
url = "http://sharebook.kr"
url2 = url.split('.')
print(url[-2:])
print(url2[1])

# 28번 - immutable: string, number, tuple mutable: list, dictionary, ndarray
lang = 'python'
# lang[0] = 'P'
print(lang)

# 29번
string = 'abcdfe2a354a32a'
string2 = string.replace('a', 'A')
print(string2)

# 30번
