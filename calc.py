# run export LC_ALL=C to avoid locale errors
import tkinter as tk
import ttkbootstrap as ttk


# Setup
window = ttk.Window(themename='vapor')
window.title('app')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry('250x300')
window.resizable(False, False)

# widgets


# main menu 
main_menu = ttk.Menu(window)

file_menu = ttk.Menu(main_menu)
file_menu.add_command(label='quit', command= lambda: window.quit())

edit_menu = ttk.Menu(main_menu)
edit_menu.add_command(label='Copy', command= lambda: print('copy'))
edit_menu.add_command(label='Paste', command= lambda: print('paste'))

help_menu = ttk.Menu(main_menu)
help_menu.add_command(label='Support', command=lambda: print("Support me"))
help_menu.add_command(label="See more projects", command= lambda: print("See more projects"))



main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
window['menu'] = main_menu

# frames
frame1 = ttk.Frame(window, border=5, relief='solid', height=25)
frame2 = ttk.Frame(window)



# variables
entry_var = tk.IntVar(value=0)

# Frame 1
entry = ttk.Label(frame1, textvariable=entry_var, text='0', borderwidth=5, font=('Arial', 15), foreground='white')
frame1.pack(side='top', fill='x', pady=20, padx=10), entry.pack(side='right')

# frame 2 grid layout
for i in range(5):
    frame2.rowconfigure(i, weight=1)
    frame2.columnconfigure(i, weight=1)

percent_btn = ttk.Button(frame2, text='%', bootstyle="outline",command= lambda:print("%"))
divide_btn = ttk.Button(frame2, text='/', bootstyle="outline", command= lambda:print("/"))
multiply_btn = ttk.Button(frame2, text='X', bootstyle="outline",command= lambda: print("X"))
minus_btn = ttk.Button(frame2, text="-", bootstyle="outline", command= lambda:print("-"))
frame2.pack(fill='both', padx=10, pady=20)

seven_btn = ttk.Button(frame2, text='7', bootstyle="outline", command= lambda: print('7'))
eight_btn = ttk.Button(frame2, text='8', bootstyle="outline", command= lambda: print('8'))
nine_btn = ttk.Button(frame2, text='9', bootstyle="outline", command= lambda: print('9'))
plus_btn = ttk.Button(frame2, text='+', bootstyle="outline", command= lambda: print('+'))

four_btn = ttk.Button(frame2, text='4', bootstyle="outline", command= lambda: print('4'))
five_btn = ttk.Button(frame2, text='5', bootstyle="outline", command= lambda: print('5'))
six_btn = ttk.Button(frame2, text='6', bootstyle="outline", command= lambda: print('6'))

one_btn = ttk.Button(frame2, text='1', bootstyle="outline", command= lambda: print('1'))
two_btn = ttk.Button(frame2, text='2', bootstyle="outline", command= lambda: print('2'))
three_btn = ttk.Button(frame2, text='3', bootstyle="outline", command= lambda: print('3'))
equals_btn = ttk.Button(frame2, text='=', bootstyle="outline", command= lambda: print('='))

zero_btn = ttk.Button(frame2, text='0', bootstyle="outline", command= lambda: print('0'))
point_btn = ttk.Button(frame2, text='.', bootstyle="outline", command= lambda: print('.'))

clear_button = ttk.Button(frame2, text='C', bootstyle="outline", command= lambda: print("clear"))
all_clear_button = ttk.Button(frame2, text='AC', bootstyle="outline", command= lambda: print("All clear"))



# grid

# row 0
percent_btn.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
divide_btn.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
multiply_btn.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
minus_btn.grid(row=0, column=3, sticky='nsew', padx=5, pady=5)

# row 1
seven_btn.grid(row=1, column=0, padx=5, sticky='nsew', pady=5)
eight_btn.grid(row=1, column=1, padx=5, sticky='nsew', pady=5)
nine_btn.grid(row=1, column=2, padx=5, sticky='nsew', pady=5)
plus_btn.grid(row=1, column=3, padx=5, sticky='nsew', rowspan=2, pady=5)

# row 2
four_btn.grid(row=2, column=0, padx=5, sticky='nsew', pady=5)
five_btn.grid(row=2, column=1, padx=5, sticky='nsew', pady=5)
six_btn.grid(row=2, column=2, padx=5, sticky='nsew', pady=5)
equals_btn.grid(row=3, column=3, padx=5, sticky='nsew', rowspan=2, pady=5)

# row 3
zero_btn.grid(row=3, column=0, padx=5, sticky='nsew', pady=5, columnspan=2)
point_btn.grid(row=3, column=2, padx=5, sticky='nsew', pady=5)

# column 5
clear_button.grid(row=0, column=4, padx=7.5, sticky='nsew', pady=5)
all_clear_button.grid(row=1, column=4, padx=7.5, sticky='nsew', pady=5, rowspan=3)


# Security event
window.bind('<Escape>', lambda event: window.quit())
# Run
window.mainloop()