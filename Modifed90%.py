# Computer Science Project
# Movie Theatre

# importing required modules

from doctest import master
from email.mime import image
import imghdr
from tkinter import *
from tkinter.messagebox import askyesno, showerror
from PIL import ImageTk, Image
import csv
import os

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
Movie_Font = ('Helvetica', 30)
gold = '#FFD700'
blue = '#00A1FF'
gold_seat_color = '#FFD700'
normal_seat_color = '#00A1FF'
seat_font = ('Helvetica', 25)
color = '#00FF00'
seat_width = 10
seat_height = 3


def closewindow():  # Function to close button when exit button is clicked
    window.destroy()


def thankyou():  # Function to be displayed when booking is done
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


def check_seats():  # Function to emsure that the user only selects the number of seats entered in screen 1
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

    heading = Label(screen_2, activebackground='black', activeforeground='green',
                    width=26, height=3, font=seat_font, text='Select your seat')
    heading.place(x=455, y=0)
    global seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8, seat9, seat9, seat9, seat9, seat9, seat10, seat11, seat12, seat13, seat14, seat15, seat16, seat17, seat18, seat19, seat20, seat21, seat22, seat23, seat24, seat25, seat26, seat27, seat28, seat29, seat30, seat31, seat32, seat33, seat34, seat35, seat36, seat37, seat38, seat39
    seat1 = Checkbutton(screen_2, activebackground=color,  bg=gold_seat_color, font=seat_font, text='A1',
                        width=seat_width, height=seat_height, variable=seat_var1, onvalue=1, offvalue=0, command=check_seats)
    seat2 = Checkbutton(screen_2, activebackground=color, bg=gold_seat_color, font=seat_font, text='A2', width=seat_width,
                        height=seat_height, variable=seat_var2, onvalue=1, offvalue=0, command=check_seats)
    seat3 = Checkbutton(screen_2, activebackground=color, bg=gold_seat_color, font=seat_font, text='A3', width=seat_width,
                        height=seat_height, variable=seat_var3, onvalue=1, offvalue=0, command=check_seats)
    seat4 = Checkbutton(screen_2, activebackground=color, bg=gold_seat_color, font=seat_font, text='A4', width=seat_width,
                        height=seat_height, variable=seat_var4, onvalue=1, offvalue=0, command=check_seats)
    seat5 = Checkbutton(screen_2, activebackground=color, bg=gold_seat_color, font=seat_font, text='A5', width=seat_width,
                        height=seat_height, variable=seat_var5, onvalue=1, offvalue=0, command=check_seats)
    seat6 = Checkbutton(screen_2, activebackground=color, bg=gold_seat_color, font=seat_font, text='A6', width=seat_width,
                        height=seat_height, variable=seat_var6, onvalue=1, offvalue=0, command=check_seats)
    seat7 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='B1', width=seat_width,
                        height=seat_height, variable=seat_var7, onvalue=1, offvalue=0, command=check_seats)
    seat8 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='B2', width=seat_width,
                        height=seat_height, variable=seat_var8, onvalue=1, offvalue=0, command=check_seats)
    seat9 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='B3', width=seat_width,
                        height=seat_height, variable=seat_var9, onvalue=1, offvalue=0, command=check_seats)
    seat10 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='B4',
                         width=seat_width, height=seat_height, variable=seat_var10, onvalue=1, offvalue=0, command=check_seats)
    seat11 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='B5',
                         width=seat_width, height=seat_height, variable=seat_var11, onvalue=1, offvalue=0, command=check_seats)
    seat12 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='B6',
                         width=seat_width, height=seat_height, variable=seat_var12, onvalue=1, offvalue=0, command=check_seats)
    seat13 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='C1',
                         width=seat_width, height=seat_height, variable=seat_var13, onvalue=1, offvalue=0, command=check_seats)
    seat14 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='C2', width=seat_width,
                         height=seat_height, variable=seat_var14, onvalue=1, offvalue=0, command=check_seats)
    seat15 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='C3', width=seat_width,
                         height=seat_height, variable=seat_var15, onvalue=1, offvalue=0, command=check_seats)
    seat16 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='C4', width=seat_width,
                         height=seat_height, variable=seat_var16, onvalue=1, offvalue=0, command=check_seats)
    seat17 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='C5', width=seat_width,
                         height=seat_height, variable=seat_var17, onvalue=1, offvalue=0, command=check_seats)
    seat18 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='C6', width=seat_width,
                         height=seat_height, variable=seat_var18, onvalue=1, offvalue=0, command=check_seats)
    seat19 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='D1', width=seat_width,
                         height=seat_height, variable=seat_var19, onvalue=1, offvalue=0, command=check_seats)
    seat20 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='D2', width=seat_width,
                         height=seat_height, variable=seat_var20, onvalue=1, offvalue=0, command=check_seats)
    seat21 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='D3', width=seat_width,
                         height=seat_height, variable=seat_var21, onvalue=1, offvalue=0, command=check_seats)
    seat22 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='D4', width=seat_width,
                         height=seat_height, variable=seat_var22, onvalue=1, offvalue=0, command=check_seats)
    seat23 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='D5',
                         width=seat_width, height=seat_height, variable=seat_var23, onvalue=1, offvalue=0, command=check_seats)
    seat24 = Checkbutton(screen_2, activebackground=color, bg=normal_seat_color, font=seat_font, text='D6',
                         width=seat_width, height=seat_height, variable=seat_var24, onvalue=1, offvalue=0, command=check_seats)
    global listm
    list_1 = [seat1, seat2, seat3, seat4, seat5, seat6]
    list_2 = [seat7, seat8, seat9, seat10, seat11, seat12]
    list_3 = [seat13, seat14, seat15, seat16, seat17, seat18]
    list_4 = [seat19, seat20, seat21, seat22, seat23, seat24]
    listm = (seat_var1, seat_var2, seat_var3, seat_var4, seat_var5, seat_var6, seat_var7, seat_var8, seat_var9, seat_var10, seat_var11, seat_var12, seat_var13, seat_var14, seat_var15, seat_var16, seat_var17, seat_var18, seat_var19, seat_var20,
             seat_var21, seat_var22, seat_var23)
    xlocation = 17
    for i in list_1:
        i.place(x=xlocation, y=100)
        xlocation += 240
    xlocation = 17
    for j in list_2:
        j.place(x=xlocation, y=250)
        xlocation += 240
    xlocation = 17
    for k in list_3:
        k.place(x=xlocation, y=400)
        xlocation += 240
    xlocation = 17
    for l in list_4:
        l.place(x=xlocation, y=550)
        xlocation += 240

    screen_this_way = Label(screen_2, bg='black', fg='white', width=133, height=3, text='Screen this way', font=(
        'ComicSans', 15), activeforeground='white', activebackground='black', anchor=CENTER)
    screen_this_way.place(x=0, y=700)
    Submit_button = Button(
        screen_2, bg='#996633', activebackground='#00ff00', width=15, height=1, text='Submit', font=('Times New Roman', 25), command=Confirmation_Screen)
    Submit_button.place(x=25, y=17)


def Confirmation_Screen():
    screen3 = Toplevel()
    screen3.title('Confirmation Screen')
    screen3.geometry('1470x800')
    screen3.resizable(False, False)
    with open('Movies.csv', 'r') as f:
        CSVREADER = csv.reader(f)
        for i in CSVREADER:
            if i[1] == film_var.get():
                k = i
                break
        Movie_Name, Language, Release_Date, Rating = k
        Movie_Label = Label(master=screen3, text=Movie_Name,
                            font=Movie_Font, anchor=W)
        Language_Label = Label(
            master=screen3, text=Language, font=Movie_Font, anchor=W)
        Release_Label = Label(master=screen3, text=Release_Date,
                              font=Movie_Font, anchor=W)
        Rating_Label = Label(master=screen3, text=Rating,
                             font=Movie_Font, anchor=W)
        Movie_Heading = Label(master=screen3, text='Movie :',
                              font=Movie_Font, anchor=E)
        Language_Heading = Label(master=screen3, text='Language :',
                                 font=Movie_Font, anchor=E)
        Release_Heading = Label(master=screen3, text='Release :',
                                font=Movie_Font, anchor=E)
        Rating_Heading = Label(master=screen3, text='Rating :',
                               font=Movie_Font, anchor=E)
        Booking_details_Heading = Label(master=screen3, text='Booking Details',
                                        font=Movie_Font, bg='grey')
        Movie_Heading.place(x=100, y=200)
        Movie_Label.place(x=500, y=200)
        Language_Heading.place(x=100, y=300)
        Language_Label.place(x=500, y=300)
        Release_Heading.place(x=100, y=400)
        Release_Label.place(x=500, y=400)
        Rating_Heading.place(x=100, y=500)
        Rating_Label.place(x=500, y=500)
        Booking_details_Heading.place(x=590, y=0)


def RADIOBUTTON(t, xloc, yloc, pichandle, activebg='white', activefg='#1E66DA', f=('ComicSans', '25'), var=film_var):
    button = Radiobutton(window, activebackground=activebg,
                         activeforeground=activefg, font=f, image=pichandle, variable=var, value=t)
    button.place(x=xloc, y=yloc)


def LABEL(t, xloc, yloc, foreg='black', backg='white', w=20, h=1, f=seat_font):  # Functions tp create label
    label = Label(window, fg=foreg, bg=backg, activeforeground=foreg,
                  activebackground=backg, width=w, height=h, text=t, font=f)
    label.place(x=xloc, y=yloc)


def PICTURE(filepath):  # Functions tp create radiobutton - Not working for now
    pic = PhotoImage(master=window, file=filepath)
    return pic


# Displaying labels and setting attributes
LABEL('Welcome to NCFE Miniplex', 455, 0, w=25, f=('Algerian', 30))
LABEL('Please enter your name', 80, 175)
LABEL('Please enter number of viewers', 30, 425, w=25)
LABEL('Please choose movie', 835, 75)

thumbnail1 = PhotoImage(master=window, file='1. BlackAdam (Small).png')
thumbnail2 = PhotoImage(master=window, file='2. 777_Charlie (Small).png')
thumbnail3 = PhotoImage(master=window, file='3. RRR (Small).png')
thumbnail4 = PhotoImage(master=window, file='4. PS1 (Small).png')
thumbnail5 = PhotoImage(master=window, file='5. Drishyam_2 (Small).png')
thumbnail6 = PhotoImage(master=window, file='6. Vikram_Vedha (Small).png')

with open('Movies.csv', 'r') as f:  # Reading from movies.csv file
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
input_box = Entry(window, background='white',
                  foreground='black', width=21, font=seat_font)
input_box.place(x=82, y=235)

people_bar = Scale(window, variable=people_var, orient=HORIZONTAL, bd=1, font=(
    'Helvetica', 20), from_=1, to=10, length=400)
people_bar.place(x=72, y=475)

exit_button = Button(window, text='Exit', width=10,
                     command=closewindow, height=1, font=('Helvetica', 15))
exit_button.place(x=1375, y=755)

submit_button = Button(window, width=10, text='Proceed',
                       font=('Helvetica', 16), command=screen2)
submit_button.place(x=700, y=755)

# Required command to launch output window
window.mainloop()
