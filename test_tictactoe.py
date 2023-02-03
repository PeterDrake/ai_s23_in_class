from unittest import TestCase
from tictactoe import *


class Test(TestCase):

    def test_generates_successor(self):
        before = 'XOX......'
        after = successor(before, 'O', 5)
        self.assertEqual('XOX..O...', after)

    def test_generates_legal_moves(self):
        before = '.OXO...X.'
        moves = legal_moves(before, 'X')
        self.assertEqual((0, 4, 5, 6, 8), moves)

    def test_finds_win_for_x(self):
        board = 'XXXO.O.O.'
        result = winner(board)
        self.assertEqual(1, result)
