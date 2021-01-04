# Bottomup
# Arr i = max(Arr i-1, Arr i-2 + k i)

def BottomUp(arr, n):
    DP_table = [0] * 101

    DP_table[0] = arr[0]
    DP_table[1] = max(arr[0], arr[1])

    for i in range(2, n):
        DP_table[i] = max(DP_table[i-1], DP_table[i-2] + arr[i])

    return DP_table[n-1]