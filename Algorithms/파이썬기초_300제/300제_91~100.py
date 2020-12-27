#91
inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바':[250, 100]}

#92, #93
print(inventory['메로나'][1], '개')

#94
inventory['월드콘'] = [500, 7]
print(inventory)

#95 keys method는 list로 저장.
ice = list(inventory.keys())
print(ice)

#96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)

#97
print(sum(ice))

#98 dic.update(newdict)
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#99 dict(), zip(keys, values) 기억하기.
eys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(eys, vals))
print(result)

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
