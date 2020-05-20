### Tic Tac Toe

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.buttonArray = [0,0,0],[0,0,0],[0,0,0]
        self.playerTurn = 1
        self.turnCount = 0
        self.gameOver = 0
        self.create_widgets()
        
    def create_widgets(self):

        self.instructionsLabel = Label(self, text = "Welcome to Tic Tac Toe V1. Click the spot you'd like to move to.")
        self.instructionsLabel.grid(row = 0, column = 0, columnspan = 4, sticky = W)

        self.notificationLabel = Label(self, text = "Player 1's turn (X's turn)")
        self.notificationLabel.grid(row = 1, column = 4)
        
        self.buttonArray[0][0] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(0,0))
        self.buttonArray[0][0].grid(row=1, column = 0)

        self.buttonArray[0][1] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(0,1))
        self.buttonArray[0][1].grid(row=1, column = 1)

        self.buttonArray[0][2] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(0,2))
        self.buttonArray[0][2].grid(row=1, column = 2)

        self.buttonArray[1][0] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(1,0))
        self.buttonArray[1][0].grid(row=2, column = 0)

        self.buttonArray[1][1] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(1,1))
        self.buttonArray[1][1].grid(row=2, column = 1)

        self.buttonArray[1][2] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(1,2))
        self.buttonArray[1][2].grid(row=2, column = 2)

        self.buttonArray[2][0] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(2,0))
        self.buttonArray[2][0].grid(row=3, column = 0)

        self.buttonArray[2][1] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(2,1))
        self.buttonArray[2][1].grid(row=3, column = 1)

        self.buttonArray[2][2] = Button(self, text = " ", height=8, width=16, bg='black', fg='white', command = lambda: self.buttonsClicked(2,2))
        self.buttonArray[2][2].grid(row=3, column = 2)

        for i in range(len(self.buttonArray)):
            for j in range(len(self.buttonArray[i])):
                self.buttonArray[i][j].grid(row = i + 4, column = j)

    def disableButtons(self):
        self.buttonArray[0][0].configure(state = DISABLED) 
        self.buttonArray[0][1].configure(state = DISABLED) 
        self.buttonArray[0][2].configure(state = DISABLED) 
        self.buttonArray[1][0].configure(state = DISABLED) 
        self.buttonArray[1][1].configure(state = DISABLED) 
        self.buttonArray[1][2].configure(state = DISABLED) 
        self.buttonArray[2][0].configure(state = DISABLED) 
        self.buttonArray[2][1].configure(state = DISABLED) 
        self.buttonArray[2][2].configure(state = DISABLED) 

    def checkForWin(self):
        if(self.turnCount == 9):
            self.notificationLabel["text"] = "It's a tie"
            self.gameOver = 1
            
        elif(self.buttonArray[0][0]["text"] == self.buttonArray[0][1]["text"] and self.buttonArray[0][0]["text"] == self.buttonArray[0][2]["text"] and self.buttonArray[0][0]["text"] == "X" or
            self.buttonArray[0][0]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[0][0]["text"] == self.buttonArray[2][2]["text"] and self.buttonArray[0][0]["text"] == "X" or
            self.buttonArray[0][0]["text"] == self.buttonArray[1][0]["text"] and self.buttonArray[0][0]["text"] == self.buttonArray[2][0]["text"] and self.buttonArray[0][0]["text"] == "X" or
            self.buttonArray[0][1]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[0][1]["text"] == self.buttonArray[2][1]["text"] and self.buttonArray[0][1]["text"] == "X" or
            self.buttonArray[0][2]["text"] == self.buttonArray[1][2]["text"] and self.buttonArray[0][2]["text"] == self.buttonArray[2][2]["text"] and self.buttonArray[0][2]["text"] == "X" or
            self.buttonArray[1][0]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[1][0]["text"] == self.buttonArray[1][2]["text"] and self.buttonArray[1][0]["text"] == "X" or
            self.buttonArray[2][0]["text"] == self.buttonArray[2][1]["text"] and self.buttonArray[2][0]["text"] == self.buttonArray[2][2]["text"] and self.buttonArray[2][0]["text"] == "X" or
            self.buttonArray[0][2]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[0][2]["text"] == self.buttonArray[2][0]["text"] and self.buttonArray[0][2]["text"] == "X"):

            self.notificationLabel["text"] = "Player 1 wins!"
            self.gameOver = 1
            
        elif(self.buttonArray[0][0]["text"] == self.buttonArray[0][1]["text"] and self.buttonArray[0][0]["text"] == self.buttonArray[0][2]["text"] and self.buttonArray[0][0]["text"] == "O" or
            self.buttonArray[0][0]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[0][0]["text"] == self.buttonArray[2][2]["text"] and self.buttonArray[0][0]["text"] == "O" or
            self.buttonArray[0][0]["text"] == self.buttonArray[1][0]["text"] and self.buttonArray[0][0]["text"] == self.buttonArray[2][0]["text"] and self.buttonArray[0][0]["text"] == "O" or
            self.buttonArray[0][1]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[0][1]["text"] == self.buttonArray[2][1]["text"] and self.buttonArray[0][1]["text"] == "O" or
            self.buttonArray[0][2]["text"] == self.buttonArray[1][2]["text"] and self.buttonArray[0][2]["text"] == self.buttonArray[2][2]["text"] and self.buttonArray[0][2]["text"] == "O" or
            self.buttonArray[1][0]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[1][0]["text"] == self.buttonArray[1][2]["text"] and self.buttonArray[1][0]["text"] == "O" or
            self.buttonArray[2][0]["text"] == self.buttonArray[2][1]["text"] and self.buttonArray[2][0]["text"] == self.buttonArray[2][2]["text"] and self.buttonArray[2][0]["text"] == "O" or
            self.buttonArray[0][2]["text"] == self.buttonArray[1][1]["text"] and self.buttonArray[0][2]["text"] == self.buttonArray[2][0]["text"] and self.buttonArray[0][2]["text"] == "O"):

            self.notificationLabel["text"] = "Player 2 wins!"
            self.gameOver = 1
        if(self.gameOver != 0):
            self.disableButtons()

    def changeTurn(self):
        if(self.playerTurn == 1):
            self.playerTurn = 2
            self.notificationLabel["text"] = "Player 2's turn (O's turn)"
        elif(self.playerTurn == 2):
            self.playerTurn = 1
            self.notificationLabel["text"] = "Player 1's turn (X's turn)"

    def buttonsClicked(self, row, column):
        if(self.playerTurn == 1):
            self.buttonArray[row][column]["text"] = "X"
        elif(self.playerTurn == 2):
            self.buttonArray[row][column]["text"] = "O"
        self.buttonArray[row][column].configure(state = DISABLED)
        self.turnCount += 1
        self.changeTurn()
        self.checkForWin()
        
root = Tk()
root.title("Tic Tac Toe")
root.geometry("600x600")

app = Application(root)

root.mainloop()
