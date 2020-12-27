#61
price = ['20180728', 100, 130, 140, 150, 160, 170]
price2 = price[1:]
print(price2)

#62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = nums[::2]
print(nums2)

#63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = nums[1::2]
print(nums2)

#64
nums = [1, 2, 3, 4, 5]
nums2 = nums[::-1]
print(nums2)

#65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66 - join method: 리스트를 문자열로 만드는 방법(" ".join(list이름): 빈칸을 리스트 성분간 틈에 넣어줌.)
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest2 = " ".join(interest)
print(interest2, type(interest2))

#67
interest3 = "/".join(interest)
print(interest3)

#68
interest4 = "\n".join(interest)
print(interest4)

#69
string = "삼성전자/LG전자/Naver"
list = string.split('/')
print(list)

#70 - data = data.sort()은되고 data2 = data.sort()은 안되는이유는?
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)