# Computer Science Project
# Movie Theatre

from tkinter import *
from tkinter.messagebox import askyesno

# Creating output window and setting attributes:
window = Tk()
window.title('Home Screen')
window.geometry('1500x800')
window.resizable(False, False)
people_var = IntVar()
film_var = StringVar()
rating = DoubleVar()
# img = PhotoImage(master=window, file='C:\\Users\\aramu\\OneDrive\\Desktop\\image.png')
# background = Label(window, image = img)
# backgrouand.place(x=0, y=0)

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

def screen2():
    pass

# Standard functions for button and label:
def RADIOBUTTON(t, xloc, yloc, pichandle, activebg = 'white', activefg = '#1E66DA', f=('ComicSans', '25'), var=film_var):
    button = Radiobutton(window, activebackground = activebg, activeforeground=activefg, font=f, image = pichandle, variable=var, value=t)
    button.place(x=xloc, y=yloc)
def LABEL(t, xloc, yloc, foreg = 'black', backg='white', w=20, h=1, f=('Helvetica', 25)):
    label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg, width=w, height=h, text=t, font=f)
    label.place(x=xloc, y=yloc)

def Picture(filepath):
    return PhotoImage(master=window, file=filepath) 

# Displaying labels and setting attributes
LABEL('Welcome to NCFE Miniplex', 455, 0, w = 25, f=('Algerian', 30))
LABEL('Please enter your name', 80, 175)
LABEL('Please enter number of viewers', 30, 425, w = 25)
LABEL('Please choose movie', 835, 75)

icon = PhotoImage(master=window, file='C://Sample.png')

# Displaying buttons and setting attributes
RADIOBUTTON('Film 1', 600, 150, pichandle=icon)
RADIOBUTTON('Film 2', 900, 150, pichandle=icon)
RADIOBUTTON('Film 3', 1200, 150, pichandle=icon)
RADIOBUTTON('Film 4', 600, 450, pichandle=icon)
RADIOBUTTON('Film 5', 900, 450, pichandle=icon)
RADIOBUTTON('Film 6', 1200, 450, pichandle=icon)


# Displaying other buttons and setting respective attributes
input_box = Entry(window, background='white',foreground='black', width=21, font=('Helvetica', 25))
input_box.place(x=82, y=235)

people_bar = Scale(window, variable=rating, orient=HORIZONTAL, bd=1, font=('Helvetica', 20), from_=1, to=10, length=400, command=people_var)
people_bar.place(x=72, y=475)

exit_button = Button(window, text='Exit', width=10, command=closewindow, height=1, font=('Helvetica', 15))
exit_button.place(x=1375, y=755)

submit_button = Button(window, width=10, text='Proceed', font=('Helvetica', 16), command=screen2)
submit_button.place(x=700, y=755)

# Required command to launch output window
window.mainloop()
