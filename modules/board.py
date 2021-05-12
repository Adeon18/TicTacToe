"""
TicTacToe Board Module
"""
import copy

from btree import LinkedBinaryTree


class Board:
    """
    A TicTacToe board
    """
    PC_SYMBOL = "0"
    USR_SYMBOL = "x"

    def __init__(self):
        self._board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.last_change = tuple()

    def __str__(self):
        strr = ""
        for i in self._board:
            strr += str(i) + "\n"

        return strr[:-1]

    def check_horizontal(self, board, player):
        """
        Check fo horisontal status
        """
        for i, _ in enumerate(board):
            flag = True
            for j, _ in enumerate(board):
                if board[i][j] != player:
                    flag = False
            if flag:
                return flag
        return flag

    def check_vertical(self, board, player):
        """
        Check fo vertical status
        """
        for i, _ in enumerate(board):
            flag = True
            for j, _ in enumerate(board):
                if board[j][i] != player:
                    flag = False
            if flag:
                return flag
        return flag

    def check_diagonal(self, board, player):
        """
        Check diag status
        """
        flag = True
        j = 0
        for i in range(len(board)):
            if board[i][i] != player:
                flag = False
        if flag:
            return flag
        flag = True
        if flag:
            for i in range(len(board)):
                j = len(board) - 1 - i
                if board[i][j] != player:
                    flag = False
        return flag

    def get_status(self):
        """
        Get the current game status
        """
        if (
            self.check_vertical(self._board, self.PC_SYMBOL)
            or self.check_horizontal(self._board, self.PC_SYMBOL)
            or self.check_diagonal(self._board, self.PC_SYMBOL)
        ):
            return self.PC_SYMBOL

        if (
            self.check_vertical(self._board, self.USR_SYMBOL)
            or self.check_horizontal(self._board, self.USR_SYMBOL)
            or self.check_diagonal(self._board, self.USR_SYMBOL)
        ):
            return self.USR_SYMBOL

        for row in self._board:
            for i in row:
                if i == " ":
                    return "continue"

        return "draw"

    def make_move(self, pos, player):
        """
        Make the move by a certaon player to a certain position
        """
        if (
            self._board[pos[0]][pos[1]] == self.PC_SYMBOL
            or self._board[pos[0]][pos[1]] == self.USR_SYMBOL
        ):
            raise IndexError("The position is occupied!")

        self._board[pos[0]][pos[1]] = player
        self.last_change = pos

    def make_computer_move(self):
        """
        Generate a computer move
        """
        self._board = self.build_tree(self, self.USR_SYMBOL)._board

    def get_positions(self):
        """
        Get all th avaliable board positions
        """
        positions = []
        for i, _ in enumerate(self._board):
            for j, _ in enumerate(self._board[i]):
                if self._board[i][j] == " ":
                    positions.append((i, j))

        return positions

    def build_tree(self, board, player):
        """
        Build a game tree
        """
        tree = LinkedBinaryTree(board)

        def recurse(board, tree, prev_move):
            positions = board.get_positions()

            if len(positions) == 1:
                pos = positions[0]
                board1 = copy.deepcopy(board)
                board2 = copy.deepcopy(board)
                if prev_move == self.USR_SYMBOL:
                    board1.make_move(pos, self.PC_SYMBOL)
                    board2.make_move(pos, self.PC_SYMBOL)
                elif prev_move == self.PC_SYMBOL:
                    board1.make_move(pos, self.USR_SYMBOL)
                    board2.make_move(pos, self.USR_SYMBOL)
                tree.insert_left(board1)
                tree.insert_right(board2)
                return
            else:
                pos1 = positions[0]
                pos2 = positions[1]
                positions.remove(pos1)
                positions.remove(pos2)
                if prev_move == self.PC_SYMBOL:
                    curr_move = self.USR_SYMBOL
                else:
                    curr_move = self.PC_SYMBOL
                board1 = copy.deepcopy(board)
                board1.make_move(pos1, curr_move)
                board2 = copy.deepcopy(board)
                board2.make_move(pos2, curr_move)
                tree.insert_left(board1)
                tree.insert_right(board2)
                recurse(board1, tree.get_left_child(), curr_move)
                recurse(board2, tree.get_right_child(), curr_move)

        recurse(board, tree, player)
        points_left = self.get_points(tree.left)
        points_right = self.get_points(tree.right)
        if points_left > points_right:
            return tree.left.key
        return tree.right.key

    def get_points(self, tree):
        """
        Get the ceitain tree points
        """
        points = 0

        def recurse(tree, points):
            board = tree.key
            # If continuing
            if board.get_status() == "continue":
                points += recurse(tree.left, points)
                points += recurse(tree.right, points)
                return points
            # If somebody won
            elif board.get_status() == self.PC_SYMBOL:
                points += 1
                return points
            elif board.get_status() == self.USR_SYMBOL:
                points -= 1
                return points
            else:
                return points
        return recurse(tree, points)


if __name__ == "__main__":
    b = Board()

    b._board = [
        [" ", "x", "x"],
        ["x", " ", "0"],
        [" ", "x", " "],
    ]
    # b.check_horizontal(b._board, b.PC_SYMBOL)
    print(b.get_status())
    print(b)
    print(b.get_positions())
