# Computer Science Project
# Movie Theatre

from tkinter import *
import tkinter
from tkinter.messagebox import askyesno

# with open('Films.txt','a+') as file :
#     file.write('Movie List')

# Setting values for some universal values:
window_size = '1500x800'
foreg = 'black'
backg = 'white'

# Creating output window and setting attributes:
window = Tk()
window.title('Home Screen')
window.geometry(window_size)
window.resizable(False, False)
people_var = IntVar()
film_var = StringVar()
rating = DoubleVar()


def closewindow():  # Function to close button when exit button is clicked
    window.destroy()


def thankyou():  # Function to be displayed when booking is done
    askyesno(title='Thankyou', message='Did you enjoy the booking experience?')


def ask_number_people():
    window1 = Toplevel(window)
    window1.geometry('250x200')
    window1.resizable(False, False)
    label_ask = Button(window1, text='Please enter the number of people',
                       width=26, height=3, font=('Helvetica', 10))
    label_ask.place(x=15, y=0)
    askbox = Entry(window1, background='white',
                   foreground='black', width=14, font=('Helvetica', 25))
    askbox.place(x=0, y=100)


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
                  foreground='black', width=21, font=('Helvetica', 25))

# Displaying buttons and setting attributes
people_bar = Scale(window, variable=rating, orient=HORIZONTAL, bd=1,
                   font=('Helvetica', 20), from_=1, to=5, length=400, command=people_var)

# number_people_button_1 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
#     'ComicSans', '25'), text='1', variable=people_var, value=1)
# number_people_button_2 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
#     'ComicSans', '25'), text='2', variable=people_var, value=2)
# number_people_button_3 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
#     'ComicSans', '25'), text='3', variable=people_var, value=3)
# number_people_button_4 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
#     'ComicSans', '25'), text='4', variable=people_var, value=4)
# number_people_button_5 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
#     'ComicSans', '25'), text='5', variable=people_var, value=5)
# number_people_button_5plus = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
#     'ComicSans', '25'), text='5+', variable=people_var, value=6)
film_button1 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film1', variable=film_var, value='Film1')
film_button2 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film2', variable=film_var, value='Film2')
film_button3 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film3', variable=film_var, value='Film3')
film_button4 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film4', variable=film_var, value='Film4')
film_button5 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film5', variable=film_var, value='Film5')
film_button6 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film6', variable=film_var, value='Film6')
film_button7 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film7', variable=film_var, value='Film7')
film_button8 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film8', variable=film_var, value='Film8')
film_button9 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film9', variable=film_var, value='Film9')
film_button10 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film10', variable=film_var, value='Film10')
film_button11 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film11', variable=film_var, value='Film11')
film_button12 = Radiobutton(window, activebackground='white', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film12', variable=film_var, value='Film12')
# rating_bar = Scale(window, variable=rating, orient=HORIZONTAL, bd=3,
#                    font=('Helvetica', 20), from_=0, to=10, length=400)
# rate_button = Button(window, text='Rate us', command=thankyou,
#                      width=10, height=1, font=('Helvetica', 15))
exit_button = Button(window, text='Exit', width=10, command=closewindow,
                     height=1, font=('Helvetica', 15))
submit_button = Button(window, width=10,
                       text='Submit', font=('Helvetica', 16))

# Setting location of buttons, labels, etc. in x and y coordinates:
welcome_label.place(x=400, y=0)

name_label.place(x=580, y=125)
input_box.place(x=582, y=185)

number_people_label.place(x=515, y=275)
people_bar.place(x=572, y=325)

# number_people_button_1.place(x=500, y=300)
# number_people_button_2.place(x=500, y=350)
# number_people_button_3.place(x=500, y=400)
# number_people_button_4.place(x=500, y=450)
# number_people_button_5.place(x=500, y=500)
# number_people_button_5plus.place(x=500, y=550)

film_label.place(x=585, y=460)
film_button1.place(x=550, y=525)
film_button2.place(x=550, y=575)
film_button3.place(x=550, y=625)
film_button4.place(x=550, y=675)
film_button5.place(x=700, y=525)
film_button6.place(x=700, y=575)
film_button7.place(x=700, y=625)
film_button8.place(x=700, y=675)
film_button9.place(x=850, y=525)
film_button10.place(x=850, y=575)
film_button11.place(x=850, y=625)
film_button12.place(x=850, y=675)

# rating_bar.place(x=500, y=725)
# rate_button.place(x=910, y=755)

exit_button.place(x=1375, y=755)
submit_button.place(x=710, y=755)

# Required command to launch output window
window.mainloop()
