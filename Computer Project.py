# Computer Science Project
# Movie Theatre
from tkinter import *
# with open('Films.txt','a+') as file :
#     file.write('Movie List')
foreg = 'black'
backg = 'white'

window = Tk()
window.attributes('-fullscreen', True)
window.title('Home Screen')
window.resizable(False, False)
people_var = IntVar()
film_var = StringVar()
rating = DoubleVar()


def review():
    pass


welcome_label = Label(window, fg='#336EFF', activebackground='#33FFB2', activeforeground='#336EFF',
                      width=30, height=2, text='Welcome to NCFE Cinemas', font=('Algerian', 30))
name_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                   width=20, height=2, text='Please enter your name', font=('Arial', 25))
number_people_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                            width=25, height=2, text='Please choose number of viewers', font=('Arial', 25))
film_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                   width=20, height=2, text='Please choose movie', font=('Arial', 25))
input_box = Entry(window, background='white',
                  śśforeground='black', width=21, font=('Arial', 25))


number_people_button_1 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='1', variable=people_var, value=1)
number_people_button_2 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='2', variable=people_var, value=2)
number_people_button_3 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='3', variable=people_var, value=3)
number_people_button_4 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='4', variable=people_var, value=4)
number_people_button_5 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='5', variable=people_var, value=5)
number_people_button_5plus = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='5+', variable=people_var, value=6)
film_button1 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film1', variable=film_var, value='Film1')
film_button2 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film2', variable=film_var, value='Film2')
film_button3 = Radiobutton(window, activebackground='#D71B1B', activeforeground='#1E66DA', font=(
    'ComicSans', '25'), text='Film3', variable=film_var, value='Film3')
rating_bar = Scale(window, variable=rating, orient=HORIZONTAL,
                   font=('Arial', 25), from_=0, to=10, length=400)
rate_button = Button(window, text='Rate us', command=review,
                     width=30, height=4, font=('Arial', 10))


name_label.place(x=30, y=150)
welcome_label.place(x=450, y=0)
number_people_label.place(x=500, y=150)
film_label.place(x=1050, y=150)
input_box.place(x=30, y=250)
number_people_button_1.place(x=600, y=300)
number_people_button_2.place(x=600, y=350)
number_people_button_3.place(x=600, y=400)
number_people_button_4.place(x=600, y=450)
number_people_button_5.place(x=600, y=500)
number_people_button_5plus.place(x=600, y=550)
film_button1.place(x=1100, y=300)
film_button2.place(x=1100, y=350)
film_button3.place(x=1100, y=400)
rating_bar.place(y=700, x=500)
rate_button.place(x=910, y=700)

window.mainloop()
