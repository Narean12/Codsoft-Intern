import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print(' | '.join(row))
            print('-' * 9)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
        else:
            print("Invalid move. Try again.")

    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def check_winner(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.check_winner('X') or self.check_winner('O') or self.is_full()

    def get_winner(self):
        if self.check_winner('X'):
            return 'X'
        elif self.check_winner('O'):
            return 'O'
        else:
            return None

def minimax(board, depth, maximizing_player):
    if board.check_winner('X'):
        return -1
    if board.check_winner('O'):
        return 1
    if board.is_full():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in board.available_moves():
            board.make_move(move)
            eval = minimax(board, depth + 1, False)
            board.board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in board.available_moves():
            board.make_move(move)
            eval = minimax(board, depth + 1, True)
            board.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for move in board.available_moves():
        board.make_move(move)
        eval = minimax(board, 0, False)
        board.board[move] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    game = TicTacToe()
    while not game.is_game_over():
        game.print_board()

        if game.current_player == 'X':
            player_move = int(input("Enter your move (0-8): "))
            if player_move in game.available_moves():
                game.make_move(player_move)
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn...")
            ai_move = find_best_move(game)
            game.make_move(ai_move)

    game.print_board()
    winner = game.get_winner()
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
