n = input()

hr = 24
min = 60
sec = 60

count = 0

for i in range(hr+1):
    for j in range(min):
        for k in range(sec):
            if n in str(i)+str(j)+str(k):
                count += 1

print(count)
