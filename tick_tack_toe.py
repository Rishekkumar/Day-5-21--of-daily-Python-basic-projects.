import random

class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
        print()

    def is_winner(self, player):
        
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or all([self.board[j][i] == player for j in range(3)]):
                return True
        
        
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def is_board_full(self):
        return all([cell != '-' for row in self.board for cell in row])

    def start_game(self):
        current_player = 'X' if random.randint(0, 1) == 0 else 'O'

        while True:
            self.print_board()
            print(f"Player {current_player}'s turn")
            
            # Get user input
            row, col = map(int, input("Enter row and column (1-3 each, space-separated): ").split())
            row -= 1
            col -= 1

           
            if self.board[row][col] != '-':
                print("This spot is already taken! Try again.")
                continue

            
            self.board[row][col] = current_player

            
            if self.is_winner(current_player):
                self.print_board()
                print(f"Player {current_player} wins!")
                break

            
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
