from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
root.title("TicTacToe")

Label(root, text="Tic Tac Toe", font=("ariel", 30)).pack()
current_chr = "X"
play_area = Frame(root, width=300, height=300, bg="white")
status_label = Label(root, text="X Turn", font=("ariel", 20))
status_label.pack(fill=X)

x_point = []
o_point = []

XO_points = []


class XOpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg="snow", fg="black")
            self.value = current_chr
            if current_chr == "X":
                x_point.append(self)
                current_chr = "O"
                status_label.configure(text="O Turn")
            elif current_chr == "O":
                o_point.append(self)
                current_chr = "X"
                status_label.configure(text="X Turn")

        check_win()

    def reset(self):
        self.button.configure(text="", bg="white")
        self.value = None


for x in range(1, 4):
    for y in range(1, 4):
        XOpoint(x, y)


class winningpossibility:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def check(self, for_char):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False

        if for_char == "X":
            for point in x_point:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_char == "O":
            for point in o_point:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True

        return all([p1_satisfied, p2_satisfied, p3_satisfied])


winning_possibility = [
    winningpossibility(0, 0, 0, 1, 0, 2),
    winningpossibility(1, 0, 1, 1, 1, 2),
    winningpossibility(2, 0, 2, 1, 2, 2),
    winningpossibility(0, 0, 1, 0, 2, 0),
    winningpossibility(0, 1, 1, 1, 2, 1),
    winningpossibility(0, 2, 1, 2, 2, 2),
    winningpossibility(0, 0, 1, 1, 2, 2),
    winningpossibility(2, 0, 1, 1, 0, 2),
]


def check_win():
    for possibility in winning_possibility:
        if possibility.check("X"):
            messagebox.showinfo("Result", "X won!")
        elif possibility.check("O"):
            messagebox.showinfo("Result", "O won!!")
        elif len(x_point) + len(o_point) == 9:
            messagebox.showinfo("Result", "Draw!")

            return


def reset_game(self):
    self.button.configure(text="", bg="lightgrey")
    if self.value == "X":
        x_point.remove(self)
    elif self.value == "O":
        o_point.remove(self)

    self.value = None


def play_again():
    global current_chr
    current_chr = "X"
    for point in XO_points:
        point.button.configure(state=NORMAL)
        point.reset()
    status_label.configure(text="X turn")
    # play_again_button.pack_forget()


play_again_button = Button(root, text="Play Again", command=play_again).pack()
"""def disable_game():
    for point in XO_points:
        point.button.configure(state = DISABLED)
    play_again_button.pack()"""

play_area.pack(padx=10, pady=10)


root.mainloop()
