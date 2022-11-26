from tkinter import *
from tkinter import Button, Label
from cell import Cell
import settings
import utils

root = Tk()
root.configure(bg = "HotPink")
# creating sections for the game 
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
# header
top_frame = Frame(root,
                  bg = 'HotPink',
                  width = utils.width_pct(100),
                  height = utils.height_pct(25))
top_frame.place(x=0, y=0)

# side bar
left_frame = Frame(root,
                  bg = 'HotPink',
                  width = utils.width_pct(25),
                  height = utils.height_pct(75))
left_frame.place(x=0, y=utils.height_pct(25))
# main frame
center_frame = Frame(root,
                  bg = 'HotPink',
                  width = utils.width_pct(75),
                  height = utils.height_pct(75))
center_frame.place(x=utils.width_pct(25), y=utils.height_pct(25))

# creating buttons
for x in range(settings.GRID_WIDTH):
    for y in range(settings.GRID_HEIGHT):
        c = Cell(x,y)
        c.create_btn(center_frame)
        c.cell_btn.grid(column = x, row = y)
        
title = Label(top_frame, text = 'MINESWEEPER', bg = 'HotPink', fg = 'white', font=("", 150))
title.place(x=(settings.GRID_WIDTH/2) , y=0) 
        
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0, y=0)        
        
Cell.randomise_mines()

for c in Cell.all:
    print(c.is_mine )


root.mainloop()