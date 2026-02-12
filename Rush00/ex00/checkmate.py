def find_king(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                return r, c
    return -1, -1


def check_direction(board, kr, kc, directions, piece_type):
    n = len(board)

    for dr, dc in directions:
        #[(-1,0),(1,0),(0,-1),(0,1)]
        #[(-1,-1),(-1,1),(1,-1),(1,1)]
        #[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        r = kr + dr
        c = kc + dc

        while 0 <= r < n and 0 <= c < n:
            if board[r][c] != '.':
                if board[r][c] in piece_type:
                    return True
                break
            r += dr
            c += dc

    return False


def check_pawn(board, kr, kc):
    n = len(board)

    for dr, dc in [(1, -1), (1, 1)]:
        r = kr + dr
        c = kc + dc
        if 0 <= r < n and 0 <= c < n:
            if board[r][c] == 'P':
                return True

    return False


def checkmate(board):
    board = board.split()
    
    kr, kc = find_king(board)

    if kr == -1:
        print("Fail")
        return

    # Rook directions
    rook_dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    # Bishop directions
    bishop_dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]

    # Queen = rook + bishop
    queen_dirs = rook_dirs + bishop_dirs

    if check_direction(board, kr, kc, rook_dirs, 'R'):
        print("Success")
        return

    if check_direction(board, kr, kc, bishop_dirs, 'B'):
        print("Success")
        return

    if check_direction(board, kr, kc, queen_dirs, 'Q'):
        print("Success")
        return

    if check_pawn(board, kr, kc):
        print("Success")
        return

    print("Fail")