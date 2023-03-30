import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.board = [" "]*9
        self.buttons = []
        self.current_player = "X"
        self.game_over = False
        self.draw_board()
    
    def draw_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda x=i, y=j: self.player_move(x, y))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def player_move(self, x, y):
        if not self.game_over and self.board[3*x+y] == " ":
            self.board[3*x+y] = self.current_player
            self.buttons[x][y].config(text=self.current_player)
            self.check_game_over()
            self.current_player = "O"
            self.computer_move()
    
    def computer_move(self):
        if not self.game_over:
            index = random.choice([i for i in range(9) if self.board[i] == " "])
            self.board[index] = "O"
            x, y = index // 3, index % 3
            self.buttons[x][y].config(text="O")
            self.check_game_over()
            self.current_player = "X"
    
    def check_game_over(self):
        for i in range(3):
            if self.board[3*i] == self.board[3*i+1] == self.board[3*i+2] != " ":
                self.show_game_over_message(self.board[3*i])
                return
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                self.show_game_over_message(self.board[i])
                return
        if self.board[0] == self.board[4] == self.board[8] != " ":
            self.show_game_over_message(self.board[0])
            return
        if self.board[2] == self.board[4] == self.board[6] != " ":
            self.show_game_over_message(self.board[2])
            return
        if all([pos != " " for pos in self.board]):
            self.show_game_over_message(None)
            return
    
    def show_game_over_message(self, winner):
        self.game_over = True
        if winner:
            message = f"O jogador {winner} ganhou!"
        else:
            message = "Empate!"
        message_label = tk.Label(self.window, text=message, font=("Helvetica", 20))
        message_label.grid(row=4, column=0, columnspan=3)
        restart_button = tk.Button(self.window, text="Jogar novamente", font=("Helvetica", 15),
                                    command=self.restart_game)
        restart_button.grid(row=5, column=0, columnspan=3)
    
    def restart_game(self):
        self.board = [" "]*9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        self.game_over = False
        self.current_player = "X"
        message_label = self.window.grid_slaves(row=4, column=0)[0]
        restart_button = self.window.grid_slaves(row=5, column=0)[0]
        message_label.grid_forget()
        restart_button.grid_forget()
    
    def play(self):
        self.window.mainloop()

game = TicTacToe()
game.play()