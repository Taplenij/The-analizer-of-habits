import webbrowser
from tkinter import *
from tkinter import ttk
import webbrowser as wb


def open_link(event):
    wb.open_new_tab('t.me/lupachosbot')

# Function to open new window


def setting_win():
    win = Tk()
    win.title('Settings')
    win.geometry('800x500')
    win.config(bg='darkgray')
    frequency = ttk.Label(win, text='Set the analize frequency\n'
                                    'THE RESULTS ACCURACY WILL DIFFER!',
                          background='darkgray', font=('Arial', 12))
    frequency.pack(anchor=NW)
    times = [f'{i} min' for i in range(5, 31, 5)]
    times_var = StringVar(value=times[0])
    set_freq = ttk.Combobox(win, textvariable=times_var,values=times, font=('Arial', 10))
    set_freq.pack(anchor=NW, pady=40)


# Create the main window
root = Tk()
root.title('Analyzer of habits')
root.geometry('800x500')
root.config(bg='darkgray')

# Title
program_name = ttk.Label(text='Analyzer of habits', background='darkgray', font=('Arial', 30))
program_name.pack()

# Pointer to link
pointer = ttk.Label(text='Send a message to Telegram bot\n'
                         '  to get the observations results',
                    background='darkgray', font=('Arial', 16))
pointer.pack(anchor=CENTER, expand=True)

# Telegram link
tg_link = ttk.Label(text='t.me/lupachosbot', background='black',
                    foreground='white', font=('Arial', 18),
                    relief='groove')
tg_link.pack()
tg_link.bind('<Button-1>', open_link)

# Settings button
settings = ttk.Button(text='Settings', command=setting_win)
settings.pack(anchor=SE, expand=True)


root.mainloop()
