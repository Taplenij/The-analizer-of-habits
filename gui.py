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
    win.resizable(False, False)

    frequency = ttk.Label(win, text='Set the analysis frequency:\n'
                                    'THE RESULTS ACCURACY WILL DIFFER!',
                          background='darkgray', font=('Arial', 14))
    frequency.place(x=1, y=1)
    # Create a combobox
    times = [f'{i} min' for i in range(5, 31, 5)]
    times_var = StringVar(value=times[0])
    set_freq = ttk.Combobox(win, textvariable=times_var, values=times, font=('Arial', 10))
    set_freq.place(x=1, y=50)
    # I was too lazy to draw a line, so I just made a black canvas
    canvas1 = Canvas(win, bg='black', highlightthickness=0, width=1, height=500)
    canvas1.place(x=400, y=0)
    # Format type label
    print_type = ttk.Label(win, text='Choose the format type output:',
                           background='darkgray', font=('Arial', 14))
    print_type.place(x=410, y=0)

    enabled = StringVar()
    # Create checkbutton(table, plot, table and plot)
    table_check = ttk.Checkbutton(win, text='Table', variable=enabled, width=7, onvalue='table')
    table_check.place(x=410, y=30)
    plot_check = ttk.Checkbutton(win, text='Plot', variable=enabled,  width=7, onvalue='plot')
    plot_check.place(x=410, y=60)
    table_plot_check = ttk.Checkbutton(win, text='Table and Plot', onvalue='table_plot')
    table_plot_check.place(x=410, y=90)
    # Notifications checkbutton
    notifications = StringVar(value='yes')

    not_lab = ttk.Label(win, text='Receive notifications',
                        background='darkgray', font=('Arial', 14))
    not_lab.place(x=1, y=300)
    rec_not = ttk.Checkbutton(win, variable=notifications, onvalue='yes', offvalue='no')
    rec_not.place(x=190, y=305)


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
