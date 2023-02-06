INITIAL_STATE = '.........'


def successor(board, player, index):
    return board[:index] + player + board[index+1:]


def legal_moves(board, player):
    if winner(board) != 0:
        return ()
    return tuple([i for i in range(len(board)) if board[i] == '.'])


def winner(board):
    winning_lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c]:
            if board[a] == 'X':
                return 1
            if board[a] == 'O':
                return -1
    return 0

# def minimax(board):
#     moves = legal_moves(board, 'O')
#     if moves:
#         return min([maximin(successor(board, 'O', m)) for m in moves])
#     return winner(board)
#
# def maximin(board):
#     moves = legal_moves(board, 'X')
#     if moves:
#         return max([minimax(successor(board, 'X', m)) for m in moves])
#     return winner(board)

def opposite(player):
    if player == 'X':
        return 'O'
    return 'X'

def value(board, player):
    moves = legal_moves(board, player)
    if moves:
        if player == 'X':
            best = max
        else:
            best = min
        return best([value(successor(board, player, m), opposite(player)) for m in moves])
    return winner(board)

def less(x, y):
    return x < y

def greater(x, y):
    return x > y

def best_move(board, player):
    moves = legal_moves(board, player)
    if moves:
        if player == 'X':
            best_value = -2
            better = greater
        else:
            best_value = 2
            better = less
        for m in moves:
            v = value(successor(board, player, m), opposite(player))
            if better(v, best_value):
                best_value = v
                result = m
        return result

def main():
    board = INITIAL_STATE
    player = 'X'
    while legal_moves(board, player):
        if player == 'X':
            move = best_move(board, player)
        else:
            move = int(input('Your move (0-8): '))
        board = successor(board, player, move)
        print(f'{board[0:3]}\n{board[3:6]}\n{board[6:9]}\n')
        player = opposite(player)
    w = winner(board)
    if w == 1:
        print('X wins!')
    elif w == -1:
        print('O wins!')
    else:
        print('Tie.')


if __name__ == '__main__':
    main()