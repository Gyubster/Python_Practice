#Topdown
def top_down(x):
    DP_table = [0]*300001
    for i in range(2, x+1):
        DP_table[i] = DP_table[i-1] + 1
        if i%5 == 0:
            DP_table[i] = min(DP_table[i], DP_table[i//5] + 1)
        elif i%3 == 0:
            DP_table[i] = min(DP_table[i], DP_table[i//3] + 1)
        elif i%2 == 0:
            DP_table[i] = min(DP_table[i], DP_table[i//2] + 1)
    return DP_table[x]

print(top_down(26))