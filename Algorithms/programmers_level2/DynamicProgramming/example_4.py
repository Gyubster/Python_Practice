def maximum_route(arr):
    # DP table
    DP_col = len(arr[0])
    DP_row = len(arr)

    DP_table = []
    DP_table_row = []

    for i in range(DP_col):
        DP_table_row.append(0)
    for j in range(DP_row):
        DP_table.append(DP_table_row)

    # Top lef to Bottom right
    DP_table[0][0] = arr[0][0]
    DP_table[0][1] = max(DP_table[])

    for i in range(1, DP_row):
        for j in range(1, DP_col):
            DP_table[i][j] = max(DP_table[i-1][j], DP_table[i][j-1] + arr[i][j])

    return DP_table[DP_row][DP_col]

arr = [    [3, 7, 9, 2, 7],
           [9, 8, 3, 5, 5],
           [1, 7, 9, 8, 5],
           [3, 8, 6, 4, 10],
           [6, 3, 9, 7, 8]  ]
print(maximum_route(arr))