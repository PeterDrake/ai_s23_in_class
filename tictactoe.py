INITIAL_STATE = '.........'


def successor(board, player, index):
    return board[:index] + player + board[index+1:]


def legal_moves(board, player):
    # TODO What if the game is over?
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
