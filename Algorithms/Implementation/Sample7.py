PlaceData = input()
n = 0

PlaceData_X = int(ord(PlaceData[0]) - 96)
PlaceData_Y = int(PlaceData[1])

Movements_X = [1, 1, -1, -1, 2, 2, -2, -2]
Movements_Y = [2, -2, 2, -2, 1, -1, 1, -1]

for i in range(len(Movements_X)):
    Possible_Sites_X = PlaceData_X + Movements_X[i]
    Possible_Sites_Y = PlaceData_Y + Movements_Y[i]

    if Possible_Sites_X < 1 or Possible_Sites_Y < 1 or Possible_Sites_X > 8 or Possible_Sites_Y > 8:
        continue

    n += 1

print(n)
