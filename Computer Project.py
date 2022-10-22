# Computer Science Project
# Movie Theatre

# importing required modules
from tkinter import *
import tkinter
from tkinter.messagebox import askyesno, showerror
import csv

# Creating output window and setting attributes:
window = Tk()
window.title('Welcome')
window.geometry('600x340+450+235')
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
Movie_Font = ('Helvetica', 25)
gold = '#FFD700'
standard = '#00A1FF'
seat_font = ('Helvetica', 25)
color = '#00FF00'
seat_width = 4
seat_height = 2

# Setting background:
bg = tkinter.PhotoImage(file='Backdrop.png')
img = Label(window, i=bg)
img.place(x=-2, y=-2)


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


def screen1():  # Movie selection
    global screen1
    screen1 = Toplevel()
    screen1.title('Movie selection')
    screen1.geometry('1500x800+10+15')
    screen1.resizable(False, False)

    # Defining properties and values for labels
    heading = Label(screen1, width=25, height=1,
                    text='Digital Ticket Counter', font=('Algerian', 30))
    name_label = Label(screen1, width=20, height=1,
                       text='Please enter your name', font=seat_font)
    number_label = Label(screen1, width=25, height=1,
                         text='Please enter number of viewers', font=seat_font,)
    moviechoose_label = Label(
        screen1, width=20, height=1, text='Please choose movie:', font=seat_font)

    # Placing labels
    heading.place(x=440, y=0)
    name_label.place(x=80, y=175)
    number_label.place(x=30, y=425)
    moviechoose_label.place(x=835, y=75)

    # def PICTURE(filepath):  # Functions tp create radiobutton - Not working for now
    #     pic = PhotoImage(master=screen1, file=filepath)
    #     return pic

    # Function to define and place radiobuttons:
    def RADIOBUTTON(t, xloc, yloc, pichandle, activebg='white', activefg='#1E66DA', f=('ComicSans', '25'), var=film_var):
        global button
        button = Radiobutton(screen1, activebackground=activebg,
                             activeforeground=activefg, font=f, image=pichandle, variable=var, value=t)
        button.place(x=xloc, y=yloc)
    global thumbnail1, thumbnail2, thumbnail3, thumbnail4, thumbnail5, thumbnail6

    # Creating small size images from files:
    thumbnail1 = PhotoImage(master=screen1, file='1. BlackAdam (Small).png')
    thumbnail2 = PhotoImage(master=screen1, file='2. 777_Charlie (Small).png')
    thumbnail3 = PhotoImage(master=screen1, file='3. RRR (Small).png')
    thumbnail4 = PhotoImage(master=screen1, file='4. PS1 (Small).png')
    thumbnail5 = PhotoImage(master=screen1, file='5. Drishyam_2 (Small).png')
    thumbnail6 = PhotoImage(master=screen1, file='6. Vikram_Vedha (Small).png')

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
    input_box = Entry(screen1, background='white',
                      foreground='black', width=21, font=seat_font)
    input_box.place(x=82, y=235)

    people_bar = Scale(screen1, variable=people_var, orient=HORIZONTAL, bd=1, font=(
        'Helvetica', 20), from_=1, to=10, length=400)
    people_bar.place(x=72, y=475)

    exit_button = Button(screen1, text='Exit', width=10,
                         command=closewindow, height=1, font=('Helvetica', 15))
    exit_button.place(x=1375, y=755)

    proceed_button = Button(screen1, width=10, text='Proceed',
                            font=('Helvetica', 16), command=screen2)
    proceed_button.place(x=700, y=755)


def screen2():  # Movie details screen
    screen2 = Toplevel()
    screen2.title('Movie Details')
    screen2.geometry('1500x800+10+15')
    screen2.resizable(False, False)

    with open('Movies.csv', 'r') as f:
        CSVREADER = csv.reader(f)
        for i in CSVREADER:
            if i[1] == film_var.get():
                k = i
                break

        Heading = Label(screen2, activebackground='black', activeforeground='green',
                        width=26, height=3, font=('Algerian', 30), text='Seat selection')
        Heading.place(x=455, y=0)

        # To display details:
        Movie_Name, Language, Release_Date, Rating, Cast, Director = k
        Movie_Label = Label(master=screen2, text=Movie_Name,
                            font=Movie_Font, anchor=W)
        Language_Label = Label(
            master=screen2, text=Language, font=Movie_Font, anchor=W)
        Release_Label = Label(
            master=screen2, text=Release_Date, font=Movie_Font, anchor=W)
        Rating_Label = Label(master=screen2, text=Rating,
                             font=Movie_Font, anchor=W)
        Cast_Label = Label(master=screen2, text=Cast,
                           font=Movie_Font, anchor=W)
        Director_Label = Label(
            master=screen2, text=Director, font=Movie_Font, anchor=W)
        Cast_Heading = Label(master=screen2, text='Cast:',
                             font=Movie_Font, anchor=E)
        Director_Heading = Label(
            master=screen2, text='Director:', font=Movie_Font, anchor=E)
        Movie_Heading = Label(master=screen2, text='Movie:',
                              font=Movie_Font, anchor=E)
        Language_Heading = Label(
            master=screen2, text='Language:', font=Movie_Font, anchor=E)
        Release_Heading = Label(
            master=screen2, text='Release:', font=Movie_Font, anchor=E)
        Rating_Heading = Label(
            master=screen2, text='Rating:', font=Movie_Font, anchor=E)

        # Placement of details:
        Movie_Heading.place(x=100, y=200)
        Movie_Label.place(x=275, y=200)
        Language_Heading.place(x=100, y=275)
        Language_Label.place(x=275, y=275)
        Release_Heading.place(x=100, y=350)
        Release_Label.place(x=275, y=350)
        Rating_Heading.place(x=100, y=425)
        Rating_Label.place(x=275, y=425)
        Cast_Heading.place(x=100, y=500)
        Cast_Label.place(x=275, y=500)
        Director_Heading.place(x=100, y=575)
        Director_Label.place(x=275, y=575)

        # Submit and exit buttons:
        exit_button = Button(screen2, text='Exit', width=10,
                             command=closewindow, height=1, font=('Helvetica', 15))
        exit_button.place(x=1375, y=755)
        proceed_button = Button(screen2, width=10, text='Proceed', font=(
            'Helvetica', 16), command=screen3)
        proceed_button.place(x=700, y=755)
        back_button = Button(screen2, width=10, text='Back', font=(
            'Helvetica', 16), command=screen2.destroy)
        back_button.place(x=25, y=755)


def screen3():  # Seats allotment screen
    global screen3
    screen3 = Toplevel()
    screen3.title('Seat selection')
    screen3.geometry('1500x800+10+15')
    screen3.resizable(False, False)

    def check_seats():  # Function to emsure that the user only selects the number of seats entered in screen 1
        sums = 0
        for i in listm:
            sums += i.get()

        correct = people_var.get()
        if sums > correct:
            showerror('Message', f'Select only {correct} seats')
            screen3.destroy

    heading = Label(screen3, activebackground='black', activeforeground='green',
                    width=26, height=3, font=('Algerian', 30), text='Seat selection')
    heading.place(x=435, y=0)

    # Defining properties and values for seats
    global seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8, seat9, seat9, seat9, seat9, seat9, seat10, seat11, seat12, seat13, seat14, seat15, seat16, seat17, seat18, seat19, seat20, seat21, seat22, seat23, seat24, seat25, seat26, seat27, seat28, seat29, seat30, seat31, seat32, seat33, seat34, seat35, seat36, seat37, seat38, seat39
    seat1 = Checkbutton(screen3, activebackground=color,  bg=gold, font=seat_font, text='A1',
                        width=seat_width, height=seat_height, variable=seat_var1, onvalue=1, offvalue=0, command=check_seats)
    seat2 = Checkbutton(screen3, activebackground=color, bg=gold, font=seat_font, text='A2', width=seat_width,
                        height=seat_height, variable=seat_var2, onvalue=1, offvalue=0, command=check_seats)
    seat3 = Checkbutton(screen3, activebackground=color, bg=gold, font=seat_font, text='A3', width=seat_width,
                        height=seat_height, variable=seat_var3, onvalue=1, offvalue=0, command=check_seats)
    seat4 = Checkbutton(screen3, activebackground=color, bg=gold, font=seat_font, text='A4', width=seat_width,
                        height=seat_height, variable=seat_var4, onvalue=1, offvalue=0, command=check_seats)
    seat5 = Checkbutton(screen3, activebackground=color, bg=gold, font=seat_font, text='A5', width=seat_width,
                        height=seat_height, variable=seat_var5, onvalue=1, offvalue=0, command=check_seats)
    seat6 = Checkbutton(screen3, activebackground=color, bg=gold, font=seat_font, text='A6', width=seat_width,
                        height=seat_height, variable=seat_var6, onvalue=1, offvalue=0, command=check_seats)
    seat7 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='B1', width=seat_width,
                        height=seat_height, variable=seat_var7, onvalue=1, offvalue=0, command=check_seats)
    seat8 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='B2', width=seat_width,
                        height=seat_height, variable=seat_var8, onvalue=1, offvalue=0, command=check_seats)
    seat9 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='B3', width=seat_width,
                        height=seat_height, variable=seat_var9, onvalue=1, offvalue=0, command=check_seats)
    seat10 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='B4',
                         width=seat_width, height=seat_height, variable=seat_var10, onvalue=1, offvalue=0, command=check_seats)
    seat11 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='B5',
                         width=seat_width, height=seat_height, variable=seat_var11, onvalue=1, offvalue=0, command=check_seats)
    seat12 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='B6',
                         width=seat_width, height=seat_height, variable=seat_var12, onvalue=1, offvalue=0, command=check_seats)
    seat13 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='C1',
                         width=seat_width, height=seat_height, variable=seat_var13, onvalue=1, offvalue=0, command=check_seats)
    seat14 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='C2', width=seat_width,
                         height=seat_height, variable=seat_var14, onvalue=1, offvalue=0, command=check_seats)
    seat15 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='C3', width=seat_width,
                         height=seat_height, variable=seat_var15, onvalue=1, offvalue=0, command=check_seats)
    seat16 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='C4', width=seat_width,
                         height=seat_height, variable=seat_var16, onvalue=1, offvalue=0, command=check_seats)
    seat17 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='C5', width=seat_width,
                         height=seat_height, variable=seat_var17, onvalue=1, offvalue=0, command=check_seats)
    seat18 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='C6', width=seat_width,
                         height=seat_height, variable=seat_var18, onvalue=1, offvalue=0, command=check_seats)
    seat19 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='D1', width=seat_width,
                         height=seat_height, variable=seat_var19, onvalue=1, offvalue=0, command=check_seats)
    seat20 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='D2', width=seat_width,
                         height=seat_height, variable=seat_var20, onvalue=1, offvalue=0, command=check_seats)
    seat21 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='D3', width=seat_width,
                         height=seat_height, variable=seat_var21, onvalue=1, offvalue=0, command=check_seats)
    seat22 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='D4', width=seat_width,
                         height=seat_height, variable=seat_var22, onvalue=1, offvalue=0, command=check_seats)
    seat23 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='D5',
                         width=seat_width, height=seat_height, variable=seat_var23, onvalue=1, offvalue=0, command=check_seats)
    seat24 = Checkbutton(screen3, activebackground=color, bg=standard, font=seat_font, text='D6',
                         width=seat_width, height=seat_height, variable=seat_var24, onvalue=1, offvalue=0, command=check_seats)

    # Placing seats in specific locations
    global listm
    list_1 = [seat1, seat2, seat3, seat4, seat5, seat6]
    list_2 = [seat7, seat8, seat9, seat10, seat11, seat12]
    list_3 = [seat13, seat14, seat15, seat16, seat17, seat18]
    list_4 = [seat19, seat20, seat21, seat22, seat23, seat24]
    listm = (seat_var1, seat_var2, seat_var3, seat_var4, seat_var5, seat_var6, seat_var7, seat_var8, seat_var9, seat_var10, seat_var11, seat_var12, seat_var13, seat_var14, seat_var15, seat_var16, seat_var17, seat_var18, seat_var19, seat_var20,
             seat_var21, seat_var22, seat_var23)
    xlocation = 375
    ylocation = 150
    mega_list = [list_1, list_2, list_3, list_4]
    for i in mega_list:
        for j in i:
            j.place(x=xlocation, y=ylocation)
            xlocation += 125
        xlocation = 375
        ylocation += 100

    screen_this_way = Label(screen3, bg='#99f2ff', fg='black', width=115, height=1, text='↓↓↓ Screen this way ↓↓↓', font=(
        'ComicSans', 15), activeforeground='white', activebackground='black', anchor=CENTER)
    screen_this_way.place(x=120, y=700)

    # Submit and exit buttons:
    exit_button = Button(screen3, text='Exit', width=10,
                         command=closewindow, height=1, font=('Helvetica', 15))
    exit_button.place(x=1375, y=755)
    proceed_button = Button(screen3, width=10, text='Proceed', font=(
        'Helvetica', 16), command=screen4)
    proceed_button.place(x=700, y=755)
    back_button = Button(screen3, width=10, text='Back', font=(
        'Helvetica', 16), command=screen3.destroy)
    back_button.place(x=25, y=755)


def screen4():  # Confirming all details
    pass


start_button = Button(window, width=10, text='START',
                      font=('Helvetica', 16), command=screen1)
start_button.place(x=242, y=200)

# Required command to launch output window
window.mainloop()
