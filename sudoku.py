"""
project discription: The aim is to create a sudoku game that has basic functions
    
author: Qiqi Su
"""

""" Import statements """
import tkinter as tk
from PIL import ImageTk, Image
from create_sudoku import create_sudoku
from sudoku_solver import valid, solve
from time import sleep

class Sudoku(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        # create title and icon
        self.master.title("Sudoku")
        icon = tk.PhotoImage(file = "llama.png")
        self.master.iconphoto(False, icon)

        # create canvas
        self.canvas = tk.Canvas(self, bg="white", width=440, height=600)
        self.canvas.pack(fill="both", expand=True)

        
    
    def create_front(self):
        # create background
        # photo should be in the same file
        openbg = Image.open("green_red_bg.png")
        self.bg = ImageTk.PhotoImage(openbg.resize((440, 600)))
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        # create front title
        self.frontmsg = self.canvas.create_text(225, 200, text="Sudoku",
                   font=("Helvetica", 50), fill = "white")

        # create start button
        self.start_btn = tk.Button(root, text="Start", font=("Helvetica", 30),
                      width=20, fg="white", bg="coral1", command=self.start)
        self.start_btn_window = self.canvas.create_window(225, 350, width=200,
                                                          window=self.start_btn)


    def bind_entry(self, event):
        userinput = event.widget.get()
        if userinput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            event.widget.delete(0, tk.END)

    def clear(self):
        self.sol_btn["state"] = tk.NORMAL
        self.check_btn["state"] = tk.NORMAL
        self.canvas.delete(self.endmsg)
        for l in self.entries:
            l[2].delete(0, tk.END)

    def check(self):
        numdict = self.numdiction()
        for l in self.entries:
            try:
                value = numdict[l[2].get()]
            except KeyError:
                errormsg = self.canvas.create_text(225, 20, text="Finish before check",
                   font=("Helvetica", 30), fill = "red")
                self.canvas.after(500, self.canvas.delete, errormsg)
                return
            x = l[0]
            y = l[1]
            if valid(value, x, y, self.sudoku):
                self.sudoku[x][y]=value
            else:
                msg = "Hint: number at position"+str(x)+","+str(y)+" is wrong"
                errormsg = self.canvas.create_text(225, 20, text=msg,
                   font=("Helvetica", 20), fill = "red")
                self.canvas.after(1000, self.canvas.delete, errormsg)
                return
        self.endmsg = self.canvas.create_text(225, 20, text="Congratulation!! You got it!!",
                                font=("Helvetica", 20), fill = "green2")
        self.sol_btn["state"] = tk.DISABLED
        self.check_btn["state"] = tk.DISABLED
        self.clear_btn["text"] = "Try Again"
        self.canvas.delete(self.clear_btn_window)
        self.clear_btn_window = self.canvas.create_window(350, 450, width=150,
                                                          window=self.clear_btn)
        return

    def sol(self):
        if solve(self.sudoku):
            for l in self.entries:
                entry = l[2]
                entry.delete(0, tk.END)
                entry.insert(0, self.sudoku[l[0]][l[1]])
        else:
            msg = "Something went wrong"
            errormsg = self.canvas.create_text(225, 20, text=msg,
                                               font=("Helvetica", 20), fill = "red")
            self.canvas.after(1000, self.canvas.delete, errormsg)
        return
    
    def start(self):
        # delete previous stuffs
        self.canvas.delete(self.frontmsg)
        self.start_btn.destroy()

        # make a board
        opencv = Image.open("canvas.png")
        self.cv = ImageTk.PhotoImage(opencv)
        self.canvas.create_image(39, 39, image=self.cv, anchor="nw")

        self.draw_table()

        # generate a sudoku
        self.sudoku = create_sudoku()
        self.entries = []
        self.print_puzzle()

        """
        # print frame of the sudoku
        openfr = Image.open("frame.png")
        self.fr = ImageTk.PhotoImage(openfr)
        self.canvas.create_image(39, 39, image=self.fr, anchor="nw")
        """
        # restrict the user input on entries
        for l in self.entries:
            entry = l[2]
            entry.bind("<Leave>", self.bind_entry)

        # create an exit button
        self.exit_btn = tk.Button(root, text="Quit", font=("Helvetica", 20),
                                  fg="white", bg="coral1", command=self.master.destroy)
        self.exit_btn_window = self.canvas.create_window(350, 540, width=80,
                                                          window=self.exit_btn)

        # create a clear button
        self.clear_btn = tk.Button(root, text="Clear", font=("Helvetica", 20),
                                  fg="white", bg="coral1", command=self.clear)
        self.clear_btn_window = self.canvas.create_window(350, 450, width=80,
                                                          window=self.clear_btn)

        # create a check button
        self.check_btn = tk.Button(root, text="Check", font=("Helvetica", 30),
                                  fg="white", bg="coral1", command=self.check)
        self.check_btn_window = self.canvas.create_window(150, 455, width=150,
                                                          window=self.check_btn)
        
        # create a show solution button
        self.sol_btn = tk.Button(root, text="Show solution", font=("Helvetica", 20),
                                  fg="white", bg="coral1", command=self.sol)
        self.sol_btn_window = self.canvas.create_window(150, 540, width=200,
                                                          window=self.sol_btn)


    # helper functions for start
    def draw_table(self):
        for i in range(1, 11):
            coord1 = 40, i*40, 400, i*40
            self.canvas.create_line(coord1, fill = "gray10")
            coord2 = i*40, 40, i*40, 400
            self.canvas.create_line(coord2, fill = "gray10")
            
    def print_puzzle(self):
        for i in range(9):
            for j in range(9):
                num = self.sudoku[i][j]
                if num == 0:
                    e = tk.Entry(self, font=("Helvetica", 30), width=40)
                    e["bd"], e["justify"] = 1, 'center'
                    self.entries.append([i, j, e])
                    coord = 41+i*40, 41+j*40
                    self.canvas.create_window(coord, anchor="nw", window=e,
                                              height=39, width=39)
                else:
                    coord = 49+i*40, 40+j*40
                    self.canvas.create_text(coord, anchor="nw", text=str(num),
                                            font=("Helvetica", 30))
    def numdiction(self):
        d = {}
        for i in range(1, 10):
            d[str(i)] = i
        return d



""" main """
root = tk.Tk()
sudoku = Sudoku(master = root)
sudoku.create_front()
sudoku.mainloop()
