# run export LC_ALL=C to avoid locale errors on linux
import tkinter as tk
import ttkbootstrap as ttk
import pyperclip
import webbrowser

url = 'https://github.com/SlackOps01'
# Setup
window = ttk.Window(themename='vapor')
window.title('app')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry('250x350+1366+0')
window.resizable(False, False)

operators = ['+', '*', "/", "%", '-']
# functions

def updateLabel(val):
    if val in operators:
        operator(val)
        pass
    elif val == "=":
        calculate(var1, operation)
        pass
    elif val == '\r':
        calculate(var1, operation)
        pass
    elif val == '.':
        insertDecimal()
    try:
        val = int(val)
        if entry_var.get() == '0':
            entry_var.set(val)
        else:
            string = f"{entry_var.get()}{val}"
            entry_var.set(string)
    except:
        pass


def backSpace():
    # Check to make sure there's no non 0 entry
    if len(entry_var.get()) == 1:
        entry_var.set('0')
        pass
    else:
        entry_var.set((entry_var.get()[:-1]))


def insertDecimal():
    entry_var.set(f"{entry_var.get()}.")
    

def clearEntry():
    entry_var.set(0)


def clearAll():
    # Clearing var1, and var2
    global var1, var2
    entry_var.set(0)
    var1 = 0
    var2 = 0


var1=0
var2 = 0


operation = ''


def operator(operator):
    # Handles pressing an operator button
    global operation, var1
    var1 = float(entry_var.get())
    entry_var.set('0')
    operation = operator


def calculate(var1, operation):
    var2 = float(entry_var.get())

    # do nothing if no operation is set
    try:
        answer = eval(f"{var1}{operation}{var2}")
        entry_var.set(round(answer, 3))
    except:
        pass


def pasteValue():
    global entry_var

    # preventing non numeric entries 
    try:
        entry_var.set(float(pyperclip.paste()))
    except:
        pass


# widgets

# main menu 
main_menu = ttk.Menu(window)

file_menu = ttk.Menu(main_menu)
file_menu.add_command(label='Quit', command= lambda: window.quit())

edit_menu = ttk.Menu(main_menu)
edit_menu.add_command(label='Copy', command= lambda: pyperclip.copy(entry_var.get()))
edit_menu.add_command(label='Paste', command= pasteValue)

help_menu = ttk.Menu(main_menu)
help_menu.add_command(label='Support', command=lambda: webbrowser.open(url))
help_menu.add_command(label="See more projects", command= lambda: webbrowser.open(url))



main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
window['menu'] = main_menu

# frames
frame1 = ttk.Frame(window, border=5, relief='solid', height=25)
frame2 = ttk.Frame(window)


# variables
entry_var = tk.StringVar(value='0')

# Frame 1
entry = ttk.Label(frame1, textvariable=entry_var, text='0', borderwidth=5, font=('Arial', 15), foreground='white')
frame1.pack(side='top', fill='x', pady=20, padx=10), entry.pack(side='right')

# frame 2 grid layout
for i in range(5):
    frame2.rowconfigure(i, weight=1)
    frame2.columnconfigure(i, weight=1)


# Creating all buttons
percent_btn = ttk.Button(frame2, text='%', bootstyle="outline", command= lambda: operator('%'))
divide_btn = ttk.Button(frame2, text='/', bootstyle="outline", command= lambda: operator('/'))
multiply_btn = ttk.Button(frame2, text='X', bootstyle="outline", command= lambda: operator('*'))
minus_btn = ttk.Button(frame2, text="-", bootstyle="outline", command= lambda: operator('-'))
frame2.pack(fill='both', padx=10, pady=20)

seven_btn = ttk.Button(frame2, text='7', bootstyle="outline", command= lambda: updateLabel(7))
eight_btn = ttk.Button(frame2, text='8', bootstyle="outline", command= lambda: updateLabel(8))
nine_btn = ttk.Button(frame2, text='9', bootstyle="outline", command= lambda: updateLabel(9))
plus_btn = ttk.Button(frame2, text='+', bootstyle="outline", command= lambda: operator('+'))

four_btn = ttk.Button(frame2, text='4', bootstyle="outline", command= lambda: updateLabel(4))
five_btn = ttk.Button(frame2, text='5', bootstyle="outline", command= lambda: updateLabel(5))
six_btn = ttk.Button(frame2, text='6', bootstyle="outline", command= lambda: updateLabel(6))

one_btn = ttk.Button(frame2, text='1', bootstyle="outline", command= lambda: updateLabel(1))
two_btn = ttk.Button(frame2, text='2', bootstyle="outline", command= lambda: updateLabel(2))
three_btn = ttk.Button(frame2, text='3', bootstyle="outline", command= lambda: updateLabel(3))
equals_btn = ttk.Button(frame2, text='=', bootstyle="outline", command= lambda: calculate(var1, operation))

zero_btn = ttk.Button(frame2, text='0', bootstyle="outline", command= lambda: updateLabel(0))
point_btn = ttk.Button(frame2, text='.', bootstyle="outline", command= lambda: insertDecimal())

clear_button = ttk.Button(frame2, text='C', bootstyle="outline", command= lambda: clearEntry())
all_clear_button = ttk.Button(frame2, text='AC', bootstyle="outline", command= lambda: clearAll())



# grid

# row 0
percent_btn.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
divide_btn.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
multiply_btn.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
minus_btn.grid(row=0, column=3, sticky='nsew', padx=5, pady=5)

# row 1, plus is in both row 1 & 2
seven_btn.grid(row=1, column=0, padx=5, sticky='nsew', pady=5)
eight_btn.grid(row=1, column=1, padx=5, sticky='nsew', pady=5)
nine_btn.grid(row=1, column=2, padx=5, sticky='nsew', pady=5)
plus_btn.grid(row=1, column=3, padx=5, sticky='nsew', rowspan=2, pady=5)

# row 2, equals in both row 3 and 4
four_btn.grid(row=2, column=0, padx=5, sticky='nsew', pady=5)
five_btn.grid(row=2, column=1, padx=5, sticky='nsew', pady=5)
six_btn.grid(row=2, column=2, padx=5, sticky='nsew', pady=5)
equals_btn.grid(row=3, column=3, padx=5, sticky='nsew', rowspan=2, pady=5)

# row 3
one_btn.grid(row=3, column=0, padx=5, sticky='nsew', pady=5)
two_btn.grid(row=3, column=1, padx=5, sticky='nsew', pady=5)
three_btn.grid(row=3, column=2, padx=5, sticky='nsew', pady=5)

# row 4
zero_btn.grid(row=4, column=0, padx=5, sticky='nsew', pady=5, columnspan=2)
point_btn.grid(row=4, column=2, padx=5, sticky='nsew', pady=5)

# column 5
clear_button.grid(row=0, column=4, padx=7.5, sticky='nsew', pady=5)
all_clear_button.grid(row=1, column=4, padx=7.5, sticky='nsew', pady=5, rowspan=4)


# Security event
window.bind('<Escape>', lambda event: window.quit())
window.bind('<KeyPress>', lambda event: updateLabel(event.char))
window.bind('<BackSpace>', lambda event: backSpace())
# Run
window.mainloop()