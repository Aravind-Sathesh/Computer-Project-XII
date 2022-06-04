# Computer Science Project
# Movie Theatre

from tkinter import *
from tkinter.messagebox import askyesno


# Setting values for some common colours:
window_size = '1500x570'
foreg = 'black'
backg = 'white'

# Creating output window and setting attributes:
window = Tk()
window.title('Home Screen')
window.geometry(window_size)
window.resizable(False, False)
window.config(bg='black')
film_var = StringVar()
rating = DoubleVar()


def closewindow():  # Function to close button when exit button is clicked
    window.destroy()



def thankyou():  # Function to be displayed when booking is done
    askyesno(title='Thankyou', message='Did you enjoy the booking experience?')
    print(rating.get())


def add_person():  # Adds a dictionary to a file
    with open('Films.txt', 'a+') as file:
        dict1 = {}
        dict1['Master'] = input_box.get()
        dict1['Film'] = film_var.get()
        dict1['Persons'] = number_box.get()
        file.write(f'{dict1}\n')


# Displaying labels and setting attributes
welcome_label = Label(window, fg='#336EFF',
                      width=30, height=2, text='Welcome to NCFE Cinemas', font=('Algerian', 30))
name_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                   width=20, height=1, text='Please enter your name', font=('Helvetica', 25))
number_people_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                            width=27, height=1, text='Please choose number of viewers', font=('Helvetica', 25))
film_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                   width=20, height=1, text='Please choose movie', font=('Helvetica', 25))
input_box = Entry(window, background='white',
                  foreground='black', width=19, font=('Helvetica', 25))
number_box = Entry(window, background='white',
                   foreground='black', width=19, font=('Helvetica', 25))

# Displaying buttons and setting attributes
film_button1 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film1', variable=film_var, value='Film1')
film_button2 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film2', variable=film_var, value='Film2')
film_button3 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film3', variable=film_var, value='Film3')
rating_bar = Scale(window, variable=rating, orient=HORIZONTAL, bd=3,
                   font=('Helvetica', 20), from_=0, to=10, length=400)
rate_button = Button(window, text='Rate us', command=thankyou,
                     width=10, height=1, font=('Helvetica', 15))
exit_button = Button(window, text='Exit', width=10, command=closewindow,
                     height=1, font=('Helvetica', 15))
register_button = Button(
    window, text='✅', font=('Helvetica', 15), command=add_person)


# Setting location of buttons, labels, etc. in x and y coordinates:
number_box.place(x=575, y=200)
name_label.place(x=30, y=150)
welcome_label.place(x=400, y=0)
number_people_label.place(x=497, y=150)
film_label.place(x=1090, y=150)
input_box.place(x=30, y=200)
film_button1.place(x=1200, y=200)
film_button2.place(x=1200, y=250)
film_button3.place(x=1200, y=300)
rating_bar.place(x=530, y=500)
rate_button.place(x=960, y=500)
exit_button.place(x=1375, y=525)
register_button.place(x=380, y=200)


# Required command to launch output window
window.mainloop()
