# Bottom up
# A(i) = A(i-1) + A(i-2)*2

def Bottomup(N):
    DP_table = [0] * 1001
    DP_table[1] = 1
    DP_table[2] = 3

    for i in range(3,N+1):
        DP_table[i] = DP_table[i-1] + DP_table[i-2]*2

    return DP_table[N]