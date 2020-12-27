#41 upper: 모두 대문자
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#42
ticker2 = ticker1.lower()
print(ticker2)

#43
a = "hello"
a = a.capitalize()
print(a)

#44, 45 ends with: 또는으로 할시에는 (a, b)
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))

#46 starts with
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

#47
a = "hello world"
b = a.split(' ')
print(b)

#48
a = "btc_krw"
b = a.split('_')
print(b)

#49
date = "2020-05-01"
date2 = date.split('-')
print(date2)

#50
data = "039490     "
data2 = data.rstrip()
data3 = data.strip()
print(data2)
print(data3)