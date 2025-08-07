import tkinter as tk 
from tkinter import scrolledtext
#-------------
#Default values 
#-------------
selected = 5 
prev = 5
grid_frame = None
cells = []

#-------------
#Helpers
#-------------
def centering (window,width,height) :
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cord = int((screen_width / 2) - (width / 2))   #coordinate to center 
    y_cord = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{width}+{x_cord}+{y_cord}") #opens in center

def setings_button () :
    #window
    settings_window = tk.Toplevel(wordle_gui) #at the top of our worlde window
    settings_window.title ("Settings") 
    settings_window.geometry("400x150")
    settings_window.configure(bg="#121213")
    settings_window.resizable(True, True)


    #word_lenggth_slider
    tk.Label(settings_window, text="Select word length" , font= ("Arial",12)).pack(pady= 10 , padx= 5)
    slider_frame = tk.Frame(settings_window) #on settings window
    slider_frame.pack()
    word_length = tk.IntVar(value=selected) #default is 5 
    slider = tk.Scale(settings_window,from_=3,to=6
                    ,orient="horizontal",variable=word_length,
                    showvalue= False, length= 250) #slides horizontally from 3 to 6
    slider.pack(side=tk.LEFT)

    floating_slider_value = tk.Label(slider_frame, text= 
                                     str(word_length.get()), #converts sliders current value to string
                                     font=("Arial", 12)) 
    floating_slider_value.pack(side=tk.LEFT,padx=20)

    def on_slider_change(val) :
        floating_slider_value.config(text=val) #updates
    
    slider.config(command = on_slider_change , bg="#121213") #whenever the slider is touched the function is activated

    #save button 
    def save_word_length() :
        global selected,prev
        selected = word_length.get() 
        if selected != prev  :      #reset only if the size was changed
            prev = selected
            settings_window.destroy() #shuts down settings window after saving
            build_grid(wordle_gui,True) #rebuilds
        else :
            settings_window.destroy()
    
    tk.Button(settings_window, text="Save" , command= save_word_length).pack(pady=10) 
    
    #Style
    tk.Label(
    settings_window,
    text="Select word length",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#121213"
    ).pack(pady=10)
    floating_slider_value = tk.Label(
    slider_frame,
    text=str(word_length.get()),
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#121213"
    )
    tk.Button(
    settings_window,
    text="Save",
    font=("Arial", 12, "bold"),
    bg="#538d4e",
    fg="white",
    relief="flat",
    command=save_word_length
    ).pack(pady=10)




def build_grid(window,rebuild_flag):
    global grid_frame, cells , selected

    n_rows = 6
    n_cols = selected if rebuild_flag else 5 #= 5 when rebuilding other wise 5 by default
    cells = []
    if rebuild_flag and grid_frame :
            grid_frame.destroy()#destory current frame

    #frame to hold the grid
    grid_frame = tk.Frame(window)
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

#---------------
#main window
#---------------
wordle_gui = tk.Tk()
wordle_gui.title ("Wordle")
worlde_width = 1200
world_height = 1600 

#centering
centering(wordle_gui,worlde_width,world_height)

#settings 
settings_btn = tk.Button(wordle_gui,text="⚙ Settings" ,
                        font=("Arial",12),command=setings_button,
                        bg="#538d43", fg="white" , relief="flat")
settings_btn.pack(pady=10) 

#building
build_grid(wordle_gui,False)

#Theme
wordle_gui.configure(bg="#121213")  # Dark gray background
grid_frame = tk.Frame (bg="#121213")  # inside build_grid











wordle_gui.mainloop()

