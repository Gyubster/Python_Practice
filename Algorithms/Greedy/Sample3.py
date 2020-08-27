n, m = map(int, input().split())
Result = []

for i in range(n):
    Data = list(map(int, input().split()))
    Result.append(min(Data))

print(max(Result))