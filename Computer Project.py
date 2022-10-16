# Computer Science Project
# Movie Theatre

#importing required modules
from turtle import Screen
from tkinter import *
from tkinter.messagebox import askyesno, showerror
from cgitb import text
import csv

# Creating output window and setting attributes:
window = Tk()
window.title('Home Screen')
window.geometry('1500x800')
window.resizable(False, False)
people_var = IntVar()
film_var = StringVar()
rating = DoubleVar()
seat_var1 = IntVar()
seat_var2 = IntVar()
seat_var3 = IntVar()
seat_var4 = IntVar()
seat_var5 = IntVar()
seat_var6 = IntVar()
seat_var7 = IntVar()
seat_var8 = IntVar()
seat_var9 = IntVar()
seat_var10 = IntVar()
seat_var11 = IntVar()
seat_var12 = IntVar()
seat_var13 = IntVar()
seat_var14 = IntVar()
seat_var15 = IntVar()
seat_var16 = IntVar()
seat_var17 = IntVar()
seat_var18 = IntVar()
seat_var19 = IntVar()
seat_var20 = IntVar()
seat_var21 = IntVar()
seat_var22 = IntVar()
seat_var23 = IntVar()
seat_var24 = IntVar()
seat_var25 = IntVar()
seat_var26 = IntVar()
seat_var27 = IntVar()
seat_var28 = IntVar()
seat_var29 = IntVar()
seat_var30 = IntVar()
seat_var31 = IntVar()
seat_var32 = IntVar()
seat_var33 = IntVar()
seat_var34 = IntVar()
seat_var35 = IntVar()
seat_var36 = IntVar()
seat_var37 = IntVar()
seat_var38 = IntVar()
seat_var39 = IntVar()
gold = '#FFD700'
blue = '#00A1FF'
seat_font = ('Helvetica', 25)
color = '#00FF00'
seat_width = 5
seat_height = 3


def closewindow():  # Function to close button when exit button is clicked
    window.destroy()

def thankyou(): # Function to be displayed when booking is done
    askyesno(title='Thankyou', message='Did you enjoy the booking experience?')

# def add_person():  # Adds a dictionary to a file
#     with open('Films.csv', 'a+') as file:
#         dict1 = {}
#         dict1['Name'] = input_box.get()
#         dict1['Movie'] = film_var.get()
#         dict1['Persons'] = people_var.get()
#         file.write(f'{dict1}\n')

def ask_number_people():  # Function to take input of number of people the ticket is being booked for
    window1 = Toplevel(window)
    window1.geometry('250x200')
    window1.resizable(False, False)
    label_ask = Button(window1, text='Please enter the number of people',
                       width=26, height=3, font=('Helvetica', 10))
    label_ask.place(x=15, y=0)
    askbox = Entry(window1, background='white',
                   foreground='black', width=14, font=seat_font)
    askbox.place(x=0, y=100)

def check_seats(): # Function to emsure that the user only selects the number of seats entered in screen 1
    sums = 0
    for i in listm:
        sums += i.get()
    correct = people_var.get()
    if sums > correct:
        showerror('Message', f'Select only {correct} seats')

def screen2():  # Seats allotment screen
    global screen_2
    screen_2 = Toplevel()
    screen_2.title('Booking Screen')
    screen_2.geometry('1470x800')
    screen_2.resizable(False, False)

    heading = Label(screen_2, activebackground='black', activeforeground='green', width=26, height=3, font=seat_font, text='Select your seat')
    heading.place(x=455, y=0)
    global seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8, seat9, seat9, seat9, seat9, seat9, seat10, seat11, seat12, seat13, seat14, seat15, seat16, seat17, seat18, seat19, seat20, seat21, seat22, seat23, seat24, seat25, seat26, seat27, seat28, seat29, seat30, seat31, seat32, seat33, seat34, seat35, seat36, seat37, seat38, seat39
    seat1 = Checkbutton(screen_2, activebackground=color,  bg=gold, font=seat_font, text='A1', width=seat_width, height=seat_height, variable=seat_var1, onvalue=1, offvalue=0, command=check_seats)
    seat2 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A2', width=seat_width, height=seat_height, variable=seat_var2, onvalue=1, offvalue=0, command=check_seats)
    seat3 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A3', width=seat_width, height=seat_height, variable=seat_var3, onvalue=1, offvalue=0, command=check_seats)
    seat4 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A4', width=seat_width, height=seat_height, variable=seat_var4, onvalue=1, offvalue=0, command=check_seats)
    seat5 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A5', width=seat_width, height=seat_height, variable=seat_var5, onvalue=1, offvalue=0, command=check_seats)
    seat6 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A6', width=seat_width, height=seat_height, variable=seat_var6, onvalue=1, offvalue=0, command=check_seats)
    seat7 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A7', width=seat_width, height=seat_height, variable=seat_var7, onvalue=1, offvalue=0, command=check_seats)
    seat8 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A8', width=seat_width, height=seat_height, variable=seat_var8, onvalue=1, offvalue=0, command=check_seats)
    seat9 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A9', width=seat_width, height=seat_height, variable=seat_var9, onvalue=1, offvalue=0, command=check_seats)
    seat10 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A10', width=seat_width, height=seat_height, variable=seat_var10, onvalue=1, offvalue=0, command=check_seats)
    seat11 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A11', width=seat_width, height=seat_height, variable=seat_var11, onvalue=1, offvalue=0, command=check_seats)
    seat12 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A12', width=seat_width, height=seat_height, variable=seat_var12, onvalue=1, offvalue=0, command=check_seats)
    seat13 = Checkbutton(screen_2, activebackground=color, bg=gold, font=seat_font, text='A13', width=seat_width, height=seat_height, variable=seat_var13, onvalue=1, offvalue=0, command=check_seats)
    seat14 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B1', width=seat_width, height=seat_height, variable=seat_var14, onvalue=1, offvalue=0, command=check_seats)
    seat15 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B2', width=seat_width, height=seat_height, variable=seat_var15, onvalue=1, offvalue=0, command=check_seats)
    seat16 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B3', width=seat_width, height=seat_height, variable=seat_var16, onvalue=1, offvalue=0, command=check_seats)
    seat17 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B4', width=seat_width, height=seat_height, variable=seat_var17, onvalue=1, offvalue=0, command=check_seats)
    seat18 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B5', width=seat_width, height=seat_height, variable=seat_var18, onvalue=1, offvalue=0, command=check_seats)
    seat19 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B6', width=seat_width, height=seat_height, variable=seat_var19, onvalue=1, offvalue=0, command=check_seats)
    seat20 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B7', width=seat_width, height=seat_height, variable=seat_var20, onvalue=1, offvalue=0, command=check_seats)
    seat21 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B8', width=seat_width, height=seat_height, variable=seat_var21, onvalue=1, offvalue=0, command=check_seats)
    seat22 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B9', width=seat_width, height=seat_height, variable=seat_var22, onvalue=1, offvalue=0, command=check_seats)
    seat23 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B10', width=seat_width, height=seat_height, variable=seat_var23, onvalue=1, offvalue=0, command=check_seats)
    seat24 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B11', width=seat_width, height=seat_height, variable=seat_var24, onvalue=1, offvalue=0, command=check_seats)
    seat25 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B12', width=seat_width, height=seat_height, variable=seat_var25, onvalue=1, offvalue=0, command=check_seats)
    seat26 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='B13', width=seat_width, height=seat_height, variable=seat_var26, onvalue=1, offvalue=0, command=check_seats)
    seat27 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C1', width=seat_width, height=seat_height, variable=seat_var27, onvalue=1, offvalue=0, command=check_seats)
    seat28 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C2', width=seat_width, height=seat_height, variable=seat_var28, onvalue=1, offvalue=0, command=check_seats)
    seat29 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C3', width=seat_width, height=seat_height, variable=seat_var29, onvalue=1, offvalue=0, command=check_seats)
    seat30 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C4', width=seat_width, height=seat_height, variable=seat_var30, onvalue=1, offvalue=0, command=check_seats)
    seat31 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C5', width=seat_width, height=seat_height, variable=seat_var31, onvalue=1, offvalue=0, command=check_seats)
    seat32 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C6', width=seat_width, height=seat_height, variable=seat_var32, onvalue=1, offvalue=0, command=check_seats)
    seat33 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C7', width=seat_width, height=seat_height, variable=seat_var33, onvalue=1, offvalue=0, command=check_seats)
    seat34 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C8', width=seat_width, height=seat_height, variable=seat_var34, onvalue=1, offvalue=0, command=check_seats)
    seat35 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C9', width=seat_width, height=seat_height, variable=seat_var35, onvalue=1, offvalue=0, command=check_seats)
    seat36 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C10', width=seat_width, height=seat_height, variable=seat_var36, onvalue=1, offvalue=0, command=check_seats)
    seat37 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C11', width=seat_width, height=seat_height, variable=seat_var37, onvalue=1, offvalue=0, command=check_seats)
    seat38 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C12', width=seat_width, height=seat_height, variable=seat_var38, onvalue=1, offvalue=0, command=check_seats)
    seat39 = Checkbutton(screen_2, activebackground=color, bg=blue, font=seat_font, text='C13', width=seat_width, height=seat_height, variable=seat_var39, onvalue=1, offvalue=0, command=check_seats)
    global listm
    list1 = [seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8, seat9, seat10, seat11, seat12, seat13]
    list2 = [seat14, seat15, seat16, seat17, seat18, seat19, seat20, seat21, seat22, seat23, seat24, seat25, seat26]
    list3 = [seat27, seat28, seat29, seat30, seat31, seat32, seat33, seat34, seat35, seat36, seat37, seat38, seat39]
    listm = (seat_var1, seat_var2, seat_var3, seat_var4, seat_var5, seat_var6, seat_var7, seat_var8, seat_var9, seat_var10, seat_var11, seat_var12, seat_var13, seat_var14, seat_var15, seat_var16, seat_var17, seat_var18, seat_var19, seat_var20, seat_var21, seat_var22, seat_var23, seat_var24, seat_var25, seat_var26, seat_var27, seat_var28, seat_var29, seat_var30, seat_var31, seat_var32, seat_var33, seat_var34, seat_var35, seat_var36, seat_var37, seat_var38, seat_var39)
    xlocation = 10
    for i in list1:
        i.place(x=xlocation, y=200)
        xlocation += 110
    xlocation = 10
    for j in list2:
        j.place(x=xlocation, y=350)
        xlocation += 110
    xlocation = 10
    for k in list3:
        k.place(x=xlocation, y=500)
        xlocation += 110

    screen_this_way = Label(screen_2, bg='black', fg='white', width=133, height=3, text='Screen this way', font=('ComicSans', 15), activeforeground='white', activebackground='black', anchor=CENTER)
    projector = Label(screen_2, bg='grey', fg='white', width=34, height=3, text='Projector', font=('ComicSans', 15), activeforeground='white', activebackground='grey', anchor=CENTER)
    screen_this_way.place(x=0, y=700)
    projector.place(x=515, y=100)

def RADIOBUTTON(t, xloc, yloc, pichandle, activebg = 'white', activefg = '#1E66DA', f=('ComicSans', '25'), var=film_var): # Functions tp create radiobutton
    button = Radiobutton(window, activebackground = activebg, activeforeground=activefg, font=f, image = pichandle, variable=var, value=t)
    button.place(x=xloc, y=yloc)

def LABEL(t, xloc, yloc, foreg = 'black', backg='white', w=20, h=1, f=seat_font): # Functions tp create label
    label = Label(window, fg=foreg, bg=backg, activeforeground=foreg, activebackground=backg, width=w, height=h, text=t, font=f)
    label.place(x=xloc, y=yloc)

def PICTURE(filepath): # Functions tp create radiobutton - Not working for now
    pic = PhotoImage(master=window, file=filepath)
    return pic

# Displaying labels and setting attributes
LABEL('Welcome to NCFE Miniplex', 455, 0, w = 25, f=('Algerian', 30))
LABEL('Please enter your name', 80, 175)
LABEL('Please enter number of viewers', 30, 425, w = 25)
LABEL('Please choose movie', 835, 75)

thumbnail1 = PhotoImage(master=window, file='1. BlackAdam (Small).png',)
thumbnail2 = PhotoImage(master=window, file='2. 777_Charlie (Small).png')
thumbnail3 = PhotoImage(master=window, file='3. RRR (Small).png')
thumbnail4 = PhotoImage(master=window, file='4. PS1 (Small).png')
thumbnail5 = PhotoImage(master=window, file='5. Drishyam_2 (Small).png')
thumbnail6 = PhotoImage(master=window, file='6. Vikram_Vedha (Small).png')

with open ('Movies.csv', 'r') as f: # Reading from movies.csv file
    csv_reader = csv.reader(f)
    movies_list = []
    for i in csv_reader:
        movies_list.append(i)

RADIOBUTTON(movies_list[1][1], 600, 150, thumbnail1)
RADIOBUTTON(movies_list[2][1], 900, 150, thumbnail2)
RADIOBUTTON(movies_list[3][1], 1200, 150, thumbnail3)
RADIOBUTTON(movies_list[4][1], 600, 450, thumbnail4)
RADIOBUTTON(movies_list[5][1], 900, 450, thumbnail5)
RADIOBUTTON(movies_list[6][1], 1200, 450, thumbnail6)

# Displaying other buttons and setting respective attributes
input_box = Entry(window, background='white',foreground='black', width=21, font=seat_font)
input_box.place(x=82, y=235)

people_bar = Scale(window, variable=people_var, orient=HORIZONTAL, bd=1, font=('Helvetica', 20), from_=1, to=10, length=400)
people_bar.place(x=72, y=475)

exit_button = Button(window, text='Exit', width=10, command=closewindow, height=1, font=('Helvetica', 15))
exit_button.place(x=1375, y=755)

submit_button = Button(window, width=10, text='Proceed', font=('Helvetica', 16), command=screen2)
submit_button.place(x=700, y=755)

# Required command to launch output window
window.mainloop()
