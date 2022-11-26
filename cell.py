from tkinter import *
from tkinter import Button, Label
import settings
import random


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label = None
    
    def __init__(self, x, y, is_mine = False):
        self.is_open = False
        self.is_mine_candidate = False
        self.is_mine = is_mine 
        self.cell_btn = None
        self.x = x
        self.y = y
        
        # append the object to Cell.all list
        Cell.all.append(self)
        
    def create_btn(self, location):
        btn = Button(location,
                      height= 2,
                      width= 2)
        btn.bind('<Button-1>', self.single_click)
        btn.bind('<Double-Button-1>', self.double_click)
        self.cell_btn = btn
    
    @staticmethod    
    def create_cell_count_label(location):
        lbl = Label(location,
                    text = f'CELLS LEFT: \n{Cell.cell_count }', 
                    width = 12,
                    height = 4 , 
                    bg = 'HotPink',
                    fg = 'white',
                    font = ("", 50))
        Cell.cell_count_label = lbl
        
        
    # reveal number
    def single_click(self, event):
        print('single')
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_mines == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
                    if cell.surrounded_mines == 0:
                        for cell2 in cell.surrounded_cells:
                            cell2.show_cell()
                            if cell2.surrounded_mines == 0:
                                for cell3 in cell2.surrounded_cells:
                                    cell3.show_cell()
            self.show_cell()
        
    def show_mine(self):
        # show player lost
        self.cell_btn.configure(text = '💣')
    
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property
    def surrounded_cells(self):
        cells = []
        for x in range(self.x-1, self.x+2):
            for y in range(self.y-1, self.y+2):
                if x>=0 and x<settings.GRID_WIDTH and y>=0 and y<settings.GRID_HEIGHT and not (self.x==x and self.y==y):
                    cells.append(self.get_cell_by_axis(x,y))
        return  cells
    
    @property
    def surrounded_mines(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count+=1
        return count

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count-=1
            self.cell_btn.configure(text = str(self.surrounded_mines))
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text = f'CELLS LEFT: \n{Cell.cell_count}')
            self.is_open == True
        # cell is open
        
            
    # for mines
    def double_click(self, event):
        print('double')
        if not self.is_mine_candidate:
            self.cell_btn.configure(text = '🚩')
            self.is_mine_candidate = True
        else:
            self.cell_btn.configure(text = '')
            self.is_mine_candidate = False
            
        
    @staticmethod
    def randomise_mines():
        mine_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in mine_cells:
            cell.is_mine = True
    
    def __repr__(self):
        return f'cell: ({self.x},{self.y})' 