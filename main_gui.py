import tkinter as tk 
from tkinter import scrolledtext
#helpers
def centering (window,width,height) :
    screen_width = wordle_gui.winfo_screenwidth()
    screen_height = wordle_gui.winfo_screenheight()

    x_cord = int((screen_width / 2) - (width / 2))   #coordinate to center 
    y_cord = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{width}+{x_cord}+{y_cord}") #opens in center


#---------------
#main window
#---------------
wordle_gui = tk.Tk()
wordle_gui.title ("Wordle")
worlde_width = 1200
world_height = 1600 

#
centering(wordle_gui,worlde_width,world_height)





#grid 
n_rows = 6
n_cols = 5 
cells = []

#frame to hold the grid
grid_frame = tk.Frame(wordle_gui)
grid_frame.pack(expand=True,fill='both',pady=30,padx= 20) #fills the window in the y direction

#allowing grid cells to expand
for i in range (n_rows) :
    grid_frame.rowconfigure(i,weight=1)
for i in range(n_cols) :
    grid_frame.columnconfigure(i,weight=1)


for row in range(n_rows) :
    row_cells = []
    for col in range (n_cols) :
        label = tk.Label(\
            grid_frame, #the window the labels set on
            text = "", #for letters entered
            width= 16,
            height= 4,
            font= ("BROPELLA" , 18, "bold", "italic"), #black by default
            relief= "solid",    #a button look
            borderwidth= 0.5, 
            bg= "white",
        )
        label.grid(row=row,column = col,sticky='nsew', padx= 7 , pady=10, ipady=10 , ipadx=10)
        row_cells.append(label)                         #appending the row to the grid
    cells.append(row_cells)









wordle_gui.mainloop()

