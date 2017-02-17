# Tim Bartos
# January 13th, 2017
# Final ;(

# Welcome to 2-Player Connect 4
# imports

from tkinter import *
import time
import sys

# giving the game **class**
    
class Gameboard(object):
    """now 30% compliant to PEP 8, with 100% more white space"""

    
    def __init__(self):
        # Lurking variables
        # (the board is rotated 90 degrees, look from the right side to understand)
        # The threes prevent python from erroring out when asked to interpret a value outside of the array.
        # Central 6 x 7 grid is only place data is truly stored.
        self.board = [[3,3,3,3,3,3,3,3,3,3,3,3],\
                      [3,3,3,3,3,3,3,3,3,3,3,3],\
                      [3,3,3,3,3,3,3,3,3,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,0,0,0,0,0,0,3,3,3],\
                      [3,3,3,3,3,3,3,3,3,3,3,3],\
                      [3,3,3,3,3,3,3,3,3,3,3,3],\
                      [3,3,3,3,3,3,3,3,3,3,3,3]]
        self.color = "yellow"
        # GUI Integration
        self.master = Tk()
        self.master.title("Connect 4! : Player " + self.color + " moves!")
        self.canvas = Canvas(self.master, width=700, height=700)
        self.canvas.bind("<Button-1>", self.click)
        self.label = Label(self.master, text = "Connect 4! : Player " + self.color + " moves!", font=("Helvetica", 16))
        self.label.pack()
        # Adding Grid
        for x in range(0, 8):
            self.canvas.create_line(100 * x, 100, 100 * x, 700)
        for y in range(0, 8):
            self.canvas.create_line(0, 100 * y, 700, 100 * y)
            
    # Utility Methods
    def exit(self):
        # Ending the window
        self.master.destroy()
        sys.exit()

        
    def restart(self):
        # Restarting the program
        self.master.destroy()
        self.__init__()
        self.finish()
    
    # Game Elements
    def add_circle(self, x, y, color):
        self.canvas.create_oval(x * 100 - 90, y * 100 + 10, x * 100 - 10,  y * 100 + 90, fill=color)

        
    def click(self, event):
        # Finding clicks on the board
        if ((event.y)//100) + 1 == 1:
            self.drop(((event.x)//100) + 1, self.color)
            
    def check_win(self, x, y):
        # This agonizing block of code is a modern artwork based on the concept of expectation of children in the information era.
        # It also is the condition for who wins, first with diagonals, then horizontals and verticals.
        if self.board[x][y] == self.board[x - 1][y - 1] == self.board[x - 2][y - 2] == self.board[x - 3][y - 3] or\
           self.board[x][y] == self.board[x - 1][y - 1] == self.board[x - 2][y - 2] == self.board[x + 1][y + 1] or\
           self.board[x][y] == self.board[x - 1][y - 1] == self.board[x + 1][y + 1] == self.board[x + 2][y + 2] or\
           self.board[x][y] == self.board[x + 1][y + 1] == self.board[x + 2][y + 2] == self.board[x + 3][y + 3] or\
           self.board[x][y] == self.board[x - 1][y + 1] == self.board[x - 2][y + 2] == self.board[x - 3][y + 3] or\
           self.board[x][y] == self.board[x - 1][y + 1] == self.board[x - 2][y + 2] == self.board[x + 1][y - 1] or\
           self.board[x][y] == self.board[x - 1][y + 1] == self.board[x + 1][y - 1] == self.board[x + 2][y - 2] or\
           self.board[x][y] == self.board[x + 1][y - 1] == self.board[x + 2][y - 2] == self.board[x + 3][y - 3] or\
           self.board[x][y] == self.board[x][y + 1] == self.board[x][y + 2] == self.board[x][y + 3] or\
           self.board[x][y] == self.board[x][y - 1] == self.board[x][y + 1] == self.board[x][y + 2] or\
           self.board[x][y] == self.board[x][y - 2] == self.board[x][y - 1] == self.board[x][y + 1] or\
           self.board[x][y] == self.board[x][y - 1] == self.board[x][y - 2] == self.board[x][y - 3] or\
           self.board[x][y] == self.board[x + 1][y] == self.board[x + 2][y] == self.board[x + 3][y] or\
           self.board[x][y] == self.board[x - 1][y] == self.board[x + 1][y] == self.board[x + 2][y] or\
           self.board[x][y] == self.board[x - 2][y] == self.board[x - 1][y] == self.board[x + 1][y] or\
           self.board[x][y] == self.board[x - 1][y] == self.board[x - 2][y] == self.board[x - 3][y]:
            # Here is where the agony ends and the popup for winning begins
            winner = Toplevel()
            winner.title("Player " + self.board[x][y] + " wins!")
            text = Message(winner, text = "Player " + self.board[x][y] + " is the winner!")
            text.pack()
            button1 = Button(winner, text="Restart", command=self.restart)
            button1.pack()
            button2 = Button(winner, text="Quit", command=self.exit)
            button2.pack()
           # In case nobody won (which is surprisingly hard in connect 4).
        dump = []
        for array in self.board:
            for value in array:
                dump.append(value)
                
        if 0 not in dump:
            winner = Toplevel()
            winner.title("Nobody wins!")
            text = Message(winner, text="Nobody is the winner. :(")
            text.pack()
            button1 = Button(winner, text="Restart?", command=self.restart)
            button1.pack()
            button2 = Button(winner, text="Quit", command=self.exit)
            button2.pack()
            
    
    def drop(self, column, player):
        # This program simulates the "drop" of a real plastic coin thing used in real connect-4.
        # However the animation part didn't work so I had to drop the only entertaining part of this program :(.
        x = column + 2
        if self.board[x][3] != 0:
            # This gives a "handy-dandy" reminder that you can't fill a column that's already full.
            popup = Toplevel()
            popup.title("Bad Move!")
            error = Message(popup, text="You may not add to a full column!")
            error.pack()
            button = Button(popup, text="Okay!", command=popup.destroy)
            button.pack()
            self.master.title("Connect 4!: Player " + self.color + " moves!")
        else:
            for y in range(0, 7):
                row = y + 2
                y = y + 3
                if self.board[x][y + 1] != 0:
                    self.board[x][y] = player
                    self.add_circle(column, row - 1, player)
                    if self.color == "yellow":
                        self.color = "red"
                    else:
                        self.color = "yellow"
                    self.master.title("Connect 4! : Player " + self.color + " moves!")
                    self.label['text'] = "Connect 4! : Player " + self.color + " moves!"
                    self.check_win(x, y)
                    break
                else:
                    pass
 
    def finish(self):
        # This just finishes and packs, nothing to see here.
        for row in range(1, 8):
            for column in range(1, 8):
                self.add_circle(row, column, "grey")
        self.canvas.pack()

# So it works on Github.
if __name__  ==  '__main__':
    game = Gameboard()
    game.finish()
