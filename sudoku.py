"""
project discription: The aim is to create a sudoku game that has basic functions
    
author: Qiqi Su
"""

""" Import statements """
import tkinter as tk
from PIL import ImageTk, Image


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
        self.canvas = tk.Canvas(self, bg="white", width=440, height=500)
        self.canvas.pack(fill="both", expand=True)

        
    
    def create_front(self):
        # create background
        # photo should be in the same file
        openbg = Image.open("green_red_bg.png")
        bg = ImageTk.PhotoImage(openbg.resize((440, 500)))
        self.canvas.create_image(0, 0, image=bg, anchor="nw")

        # create front title
        self.frontmsg = self.canvas.create_text(225, 200, text="Sudoku",
                   font=("Helvetica", 50), fill = "white")

        # create start button
        """
        self.start_btn = tk.Button(root, text="Start", font=("Helvetica", 30),
                      width=20, fg="white", bg="coral1", command=self.start)
        self.start_btn_window = self.canvas.create_window(225, 400, width=200, window=start_btn)
        
        """
    def start(self):
        return
    
    def draw_table(self):
        for i in range(1, 11):
            coord1 = 40, i*40, 400, i*40
            self.canvas.create_line(coord1, fill = "gray10")
            coord2 = i*40, 40, i*40, 400
            self.canvas.create_line(coord2, fill = "gray10")

    
        


""" main """
root = tk.Tk()
sudoku = Sudoku(master = root)
sudoku.create_front()
sudoku.mainloop()
