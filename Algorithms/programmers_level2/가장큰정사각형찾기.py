def solution(board):
    board_row = len(board)
    board_col = len(board[0])

    max_point = 0

    for i in range(board_row):
        max_point+=sum(board[i][:])
    if max_point == 0:
        return 0

    max_point = 0

    for i in range(1, board_row):
        for j in range(1, board_col):
            if board[i][j] == 0:
                continue
            else:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
                if max_point < board[i][j]:
                    max_point = board[i][j]

    if max_point>0:
        answer = max_point**2
    else:
        answer = 1

    return answer

# 케이스를 분류.
