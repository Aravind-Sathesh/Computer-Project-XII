# Computer Science Project
# Movie Theatre

from tkinter import *
from tkinter.messagebox import askyesno

foreg = 'black'
backg = 'white'

# Creating output window and setting attributes:
window = Tk()
window.title('Home Screen')
window.geometry('1500x800')
window.resizable(False, False)
people_var = IntVar()
film_var = StringVar()
rating = DoubleVar()

def closewindow():  # Function to close button when exit button is clicked
    window.destroy()

def thankyou():  # Function to be displayed when booking is done
    askyesno(title='Thankyou', message='Did you enjoy the booking experience?')

def add_person():  # Adds a dictionary to a file
    with open('Films.csv', 'a+') as file:
        dict1 = {}
        dict1['Master'] = input_box.get()
        dict1['Film'] = film_var.get()
        dict1['Persons'] = people_var.get()
        file.write(f'{dict1}\n')

def ask_number_people():  # Function to take input of number of people the ticket is being booked for
    window1 = Toplevel(window)
    window1.geometry('250x200')
    window1.resizable(False, False)
    label_ask = Button(window1, text='Please enter the number of people',
                       width=26, height=3, font=('Helvetica', 10))
    label_ask.place(x=15, y=0)
    askbox = Entry(window1, background='white',
                   foreground='black', width=14, font=('Helvetica', 25))
    askbox.place(x=0, y=100)


# Standard functions for button and label:
def RADIOBUTTON(t, xloc, yloc, activebg = 'white', activefg = '#1E66DA', f=('ComicSans', '25'), var=film_var):
    button = Radiobutton(window, activebackground = activebg, activeforeground=activefg, font=f, text=t, variable=var, value=t)
    button.place(x=xloc, y=yloc)
def LABEL(t, xloc, yloc, foreg = 'black', backg='white', w=20, h=1, f=('Helvetica', 25)):
    label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg, width=w, height=h, text=t, font=f)
    label.place(x=xloc, y=yloc)

# Displaying labels and setting attributes
LABEL('Welcome to NCFE Miniplex', 400, 0, foreg='#336EFF')
LABEL('Please enter your name', 580, 125)
LABEL('Please choose number of viewers', 515, 275, w = 27)
LABEL('Please choose movie', 585, 460)

# Displaying buttons and setting attributes
RADIOBUTTON('Film 1', 550, 525)
RADIOBUTTON('Film 2', 550, 575)
RADIOBUTTON('Film 3', 550, 625)
RADIOBUTTON('Film 4', 550, 675)
RADIOBUTTON('Film 5', 700, 525)
RADIOBUTTON('Film 6', 700, 575)
RADIOBUTTON('Film 7', 700, 625)
RADIOBUTTON('Film 8', 700, 675)
RADIOBUTTON('Film 9', 850, 525)
RADIOBUTTON('Film 10', 850, 575)
RADIOBUTTON('Film 11', 850, 625)
RADIOBUTTON('Film 12', 850, 675)

# Displaying other buttons and setting respective attributes
input_box = Entry(window, background='white',foreground='black', width=21, font=('Helvetica', 25))
input_box.place(x=582, y=185)

people_bar = Scale(window, variable=rating, orient=HORIZONTAL, bd=1, font=('Helvetica', 20), from_=1, to=10, length=400, command=people_var)
people_bar.place(x=572, y=325)

exit_button = Button(window, text='Exit', width=10, command=closewindow, height=1, font=('Helvetica', 15))
exit_button.place(x=1375, y=755)

submit_button = Button(window, width=10, text='Submit', font=('Helvetica', 16), command=screen2)
submit_button.place(x=710, y=755)

# Required command to launch output window
window.mainloop()
