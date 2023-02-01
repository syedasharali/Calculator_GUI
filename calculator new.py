from tkinter import *

# Create the main window
root = Tk()
root.title('Calculator')
root.iconbitmap(r'calc.ico')
root.geometry('456x380')
root.resizable(0,0)

# Create a StringVar to store the current input
display_text = StringVar()

# Define functions for each button
def insert_digit(digit):
    """Inserts a digit into the display"""
    display.insert(END, digit)

def insert_zero():
    """Inserts zero"""
    if display_text.get()!='0':
        display.insert(END,0)
        
def insert_plus():
    flag=True
    if display_text.get()!='':
        for i in '+-x/':
            if display_text.get()[-1]==i:
                flag=False
        if flag==True:
            if display_text.get()[-1]=='-':
                display.delete(len(display_text.get())-1,len(display_text.get()))
            display.insert(END,'+')

def insert_minus():
    if display_text.get()!='':
        if display_text.get()[-1]!='-':
            if display_text.get()[-1]=='+':
                display.delete(len(display_text.get())-1,len(display_text.get()))
            display.insert(END,'-')
    else:
        display.insert(END,'-')

def insert_multiply():
    if display_text.get()!='':
        if display_text.get()[-1] in '+-x/e':
            display.delete(len(display_text.get())-1,len(display_text.get()))
        display.insert(END,'x')

def insert_divide():
    if display_text.get()!='':
        if display_text.get()[-1] in list('+-x/'):
            display.delete(len(display_text.get())-1,len(display_text.get()))
        display.insert(END,'/')

def insert_decimal():
    """Inserts a decimal point into the display"""
    if "." not in display_text.get():
        display.insert(END, ".")

def insert_exponent():
    """Inserts an exponent into the display"""
    try:
        expression = display_text.get()
        expression = expression.replace("x","*")
        eval(expression)
        if display_text.get()[-1] in '+-x/e':
            display.delete(len(display_text.get())-1,len(display_text.get()))
        display.insert(END, "e")
    except:
        pass


def calculate(evt):
    """Evaluates the expression in the display and shows the result"""
    expression = display_text.get()
    expression = expression.replace("x","*")
    result = eval(expression)
    display.delete(0, END)
    display.insert(0, result)

def clear():
    """Clears the last character from the display"""
    display.delete(len(display_text.get()) - 1, len(display_text.get()))

def clear_all():
    """Clears the entire display"""
    display.delete(0, END)

# Create the Entry widget for the display and place it at the top
display = Entry(root, textvariable=display_text, bd=2, font='Helvetica 30')
display.grid(columnspan=5, padx=5, pady=12, ipady=3)

# Create the button widgets and place them in a grid layout
button_list = [
    ("7", lambda: insert_digit(7)),
    ("8", lambda: insert_digit(8)),
    ("9", lambda: insert_digit(9)),
    ("/", insert_divide),
    ("AC", clear_all),
    ("4", lambda: insert_digit(4)),
    ("5", lambda: insert_digit(5)),
    ("6", lambda: insert_digit(6)),
    ("x", insert_multiply),
    ("C", clear),
    ("1", lambda: insert_digit(1)),
    ("2", lambda: insert_digit(2)),
    ("3", lambda: insert_digit(3)),
    ("+", insert_plus),
    ("-", insert_minus),
    ("0", insert_zero),
    (".", insert_decimal),
    ("e", insert_exponent),
    ("=", lambda: calculate(1))
]

for i, button in enumerate(button_list):
    button_text, button_command = button
    button = Button(root, text=button_text, font='Helvetica 20', command=button_command)
    if i <= 20:
        button['width']=3
    if i == 13:  # for the big plus button that spans rows 3 and 4
        button.grid(row=3, column=3, rowspan=2, ipadx=15, ipady=46, pady=1, padx=1, sticky='ew')
    elif i == 18: # for the equal button
        button.grid(row=4, column=4, ipadx=15, ipady=8, pady=1, padx=1, sticky='ew')
    else:
        button.grid(row=i // 5 + 1, column=i % 5, ipadx=15, ipady=8, pady=1, padx=1, sticky='ew')

display.focus_set()
root.bind('<Return>',calculate)


root.mainloop()
