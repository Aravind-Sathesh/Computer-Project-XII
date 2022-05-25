# Computer Science Project
# Movie Theatre
from tkinter import *
from turtle import width
# with open('Films.txt','a+') as file :
#     file.write('Movie List')
window_size = '1500x1000'
foreg = 'black'
backg = 'white'

window = Tk()
window.title('Home Screen')
window.geometry(window_size)
window.resizable(False, False)


name_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg,
                   activebackground=backg, width=20, height=2, text='Name', font=('Arial', 25))
welcome_label = Label(window, bg='#33FFB2', fg='#336EFF', activebackground='#33FFB2', activeforeground='#336EFF',
                      width=30, height=2, text='Welcome to NCFE Cinemas', font=('American Typewriter', 25))
number_people_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                            width=25, height=2, text='Please choose number of people', font=('Arial', 25))
film_label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg,
                   width=20, height=2, text='Please Choose film', font=('Arial', 25))
menu1 = StringVar()
menu1.set("Please choose the number of persons for the movie")
drop1 = OptionMenu(window, menu1, '1', '2', '3', '4',
                   '5', '6', '7', '8', '9', '10')
menu2 = StringVar()
menu2.set('Please choose movie')
drop2 = OptionMenu(window, menu2, 'Film1', 'Film2', 'Film3')


name_label.place(x=30, y=150)
welcome_label.place(x=450, y=0)
number_people_label.place(x=500, y=150)
film_label.place(x=1050, y=150)
drop1.place(x=560, y=250)
drop2.place(x=1170, y=250)
window.mainloop()
