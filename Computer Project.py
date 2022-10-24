# Computer Science Project
# Movie Theatre

# importing required modules
from tkinter import *
from tkinter.messagebox import askyesno, showerror
import csv
from PIL import Image, ImageTk


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
gold = '#FFD700'
blue = '#00A1FF'
green = '#00FF00'
main_font = ('Helvetica', 25)
small_font = ('Helvetica', 20)
seat_width = 4
seat_height = 2

# Setting background:
bg = PhotoImage(file='Backdrop.png')
img = Label(window, i=bg)
img.place(x=-2, y=-2)


def closewindow():  # Function to close button when exit button is clicked
    window.destroy()


def thankyou():  # Function to be displayed when booking is done
    askyesno(title='Thankyou', message='Did you enjoy the booking experience?')


def PICTURE(filepath, x_size=170, y_size=240):  # Functions to create image objects
    image = Image.open(filepath)
    img = image.resize((x_size, y_size))
    screen1.img = img
    return ImageTk.PhotoImage(img)


def screen_1():  # Movie selectionw
    global screen1
    screen1 = Toplevel()
    screen1.title('Movie selection')
    screen1.geometry('1500x800+10+15')
    screen1.resizable(False, False)

    # Defining properties and values for labels
    heading = Label(screen1, width=25, height=1,
                    text='Digital Ticket Counter', font=('Algerian', 30))
    name_label = Label(screen1, width=20, height=1,
                       text='Please enter your name', font=main_font)
    number_label = Label(screen1, width=25, height=1,
                         text='Please enter number of viewers', font=main_font,)
    moviechoose_label = Label(
        screen1, width=20, height=1, text='Please choose movie:', font=main_font)

    # Placing labels
    heading.place(x=440, y=0)
    name_label.place(x=80, y=175)
    number_label.place(x=30, y=425)
    moviechoose_label.place(x=835, y=75)

    with open('Movies.csv', 'r') as f:  # Reading from movies.csv file
        csv_reader = csv.reader(f)
        movies_list = []
        for i in csv_reader:
            movies_list.append(i)

    # Function to define and place radiobuttons:
    def RADIOBUTTON(t, xloc, yloc, pichandle, activebg='white', activefg='#1E66DA', f=('ComicSans', '25'), var=film_var):
        global button
        button = Radiobutton(screen1, activebackground=activebg,
                             activeforeground=activefg, font=f, image=pichandle, variable=var, value=t)
        button.place(x=xloc, y=yloc)
    global poster1, poster2, poster3, poster4, poster5, poster6

    # Creating small size images from files:
    poster1 = PICTURE('Black Adam.png')
    poster2 = PICTURE('777 Charlie.png')
    poster3 = PICTURE('RRR.png')
    poster4 = PICTURE('Ponniyin Selvan 1.png')
    poster5 = PICTURE('Bheeshma Parvam.png')
    poster6 = PICTURE('Vikram Vedha.png')

    RADIOBUTTON(movies_list[1][0], 600, 150, poster1)
    RADIOBUTTON(movies_list[2][0], 900, 150, poster2)
    RADIOBUTTON(movies_list[3][0], 1200, 150, poster3)
    RADIOBUTTON(movies_list[4][0], 600, 450, poster4)
    RADIOBUTTON(movies_list[5][0], 900, 450, poster5)
    RADIOBUTTON(movies_list[6][0], 1200, 450, poster6)

    # Displaying other buttons and setting respective attributes
    global input_box

    input_box = Entry(screen1, background='white',
                      foreground='black', width=21, font=main_font)
    input_box.place(x=82, y=235)

    people_bar = Scale(screen1, variable=people_var, orient=HORIZONTAL, bd=1, font=(
        'Helvetica', 20), from_=1, to=10, length=400)
    people_bar.place(x=72, y=475)

    exit_button = Button(screen1, text='Exit', width=10,
                         command=closewindow, height=1, font=('Helvetica', 15))
    exit_button.place(x=1375, y=755)

    proceed_button = Button(screen1, width=10, text='Proceed',
                            font=('Helvetica', 16), command=screen_2)
    proceed_button.place(x=700, y=755)


def screen_2():  # Movie details screen
    screen2 = Toplevel()
    screen2.title('Movie Details')
    screen2.geometry('1500x800+10+15')
    screen2.resizable(False, False)

    with open('Movies.csv', 'r') as f:
        CSVREADER = csv.reader(f)
        for i in CSVREADER:
            if i[0] == film_var.get():
                k = i
                break

        Heading = Label(screen2, activebackground='black', activeforeground='green',
                        width=26, height=3, font=('Algerian', 30), text='Movie Details')
        Heading.place(x=420, y=0)

        # To display details:
        global Time
        Movie_Name, Language, Release_Date, Runtime_h, Runtime_m, Time, Cast, Director, Rating = k
        Runtime_text = Runtime_h, 'hours,', Runtime_m, 'minutes'
        Movie_Label = Label(master=screen2, text=Movie_Name,
                            font=small_font, anchor=W)
        Language_Label = Label(
            master=screen2, text=Language, font=small_font, anchor=W)
        Release_Label = Label(
            master=screen2, text=Release_Date, font=small_font, anchor=W)
        Runtime_Label = Label(
            master=screen2, text=Runtime_text, font=small_font, anchor=W)
        Time_Label = Label(master=screen2, text=Time,
                           font=small_font, anchor=W)
        Cast_Label = Label(master=screen2, text=Cast,
                           font=small_font, anchor=W)
        Director_Label = Label(
            master=screen2, text=Director, font=small_font, anchor=W)
        Rating_Label = Label(master=screen2, text=Rating,
                             font=small_font, anchor=W)
        Movie_Heading = Label(master=screen2, text='Movie:',
                              font=small_font, anchor=E)
        Language_Heading = Label(
            master=screen2, text='Language:', font=small_font, anchor=E)
        Release_Heading = Label(
            master=screen2, text='Release:', font=small_font, anchor=E)
        Runtime_Heading = Label(
            master=screen2, text='Run time:', font=small_font, anchor=E)
        Time_Heading = Label(
            master=screen2, text='Time:', font=small_font, anchor=E)
        Cast_Heading = Label(master=screen2, text='Cast:',
                             font=small_font, anchor=E)
        Director_Heading = Label(
            master=screen2, text='Director:', font=small_font, anchor=E)
        Rating_Heading = Label(
            master=screen2, text='Rating:', font=small_font, anchor=E)

        # Placement of details:
        Movie_Heading.place(x=100, y=200)
        Movie_Label.place(x=275, y=200)
        Language_Heading.place(x=100, y=250)
        Language_Label.place(x=275, y=250)
        Release_Heading.place(x=100, y=300)
        Release_Label.place(x=275, y=300)
        Runtime_Heading.place(x=100, y=350)
        Runtime_Label.place(x=275, y=350)
        Time_Heading.place(x=100, y=400)
        Time_Label.place(x=275, y=400)
        Cast_Heading.place(x=100, y=450)
        Cast_Label.place(x=275, y=450)
        Director_Heading.place(x=100, y=500)
        Director_Label.place(x=275, y=500)
        Rating_Heading.place(x=100, y=550)
        Rating_Label.place(x=275, y=550)

        Movie_Name = str(Movie_Name+'.png')
        poster = PICTURE(Movie_Name, x_size=375, y_size=550)
        imglabel = Label(screen2, image=poster, borderwidth=3, relief='solid')
        imglabel.image = poster
        imglabel.place(x=1050, y=125)

        # Submit and exit buttons:
        exit_button = Button(screen2, text='Exit', width=10,
                             command=closewindow, height=1, font=('Helvetica', 15))
        exit_button.place(x=1375, y=755)
        proceed_button = Button(screen2, width=10, text='Proceed', font=(
            'Helvetica', 16), command=screen_3)
        proceed_button.place(x=700, y=755)
        back_button = Button(screen2, width=10, text='Back', font=(
            'Helvetica', 16), command=screen2.destroy)
        back_button.place(x=25, y=755)


def screen_3():  # Seats selection screen
    global screen3
    global listm
    global listn
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
    seat1 = Checkbutton(screen3, activebackground=green,  bg=gold, font=main_font, text='A1',
                        width=seat_width, height=seat_height, variable=seat_var1, onvalue=1, offvalue=0, command=check_seats)
    seat2 = Checkbutton(screen3, activebackground=green, bg=gold, font=main_font, text='A2', width=seat_width,
                        height=seat_height, variable=seat_var2, onvalue=1, offvalue=0, command=check_seats)
    seat3 = Checkbutton(screen3, activebackground=green, bg=gold, font=main_font, text='A3', width=seat_width,
                        height=seat_height, variable=seat_var3, onvalue=1, offvalue=0, command=check_seats)
    seat4 = Checkbutton(screen3, activebackground=green, bg=gold, font=main_font, text='A4', width=seat_width,
                        height=seat_height, variable=seat_var4, onvalue=1, offvalue=0, command=check_seats)
    seat5 = Checkbutton(screen3, activebackground=green, bg=gold, font=main_font, text='A5', width=seat_width,
                        height=seat_height, variable=seat_var5, onvalue=1, offvalue=0, command=check_seats)
    seat6 = Checkbutton(screen3, activebackground=green, bg=gold, font=main_font, text='A6', width=seat_width,
                        height=seat_height, variable=seat_var6, onvalue=1, offvalue=0, command=check_seats)
    seat7 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='B1', width=seat_width,
                        height=seat_height, variable=seat_var7, onvalue=1, offvalue=0, command=check_seats)
    seat8 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='B2', width=seat_width,
                        height=seat_height, variable=seat_var8, onvalue=1, offvalue=0, command=check_seats)
    seat9 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='B3', width=seat_width,
                        height=seat_height, variable=seat_var9, onvalue=1, offvalue=0, command=check_seats)
    seat10 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='B4',
                         width=seat_width, height=seat_height, variable=seat_var10, onvalue=1, offvalue=0, command=check_seats)
    seat11 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='B5',
                         width=seat_width, height=seat_height, variable=seat_var11, onvalue=1, offvalue=0, command=check_seats)
    seat12 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='B6',
                         width=seat_width, height=seat_height, variable=seat_var12, onvalue=1, offvalue=0, command=check_seats)
    seat13 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='C1',
                         width=seat_width, height=seat_height, variable=seat_var13, onvalue=1, offvalue=0, command=check_seats)
    seat14 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='C2', width=seat_width,
                         height=seat_height, variable=seat_var14, onvalue=1, offvalue=0, command=check_seats)
    seat15 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='C3', width=seat_width,
                         height=seat_height, variable=seat_var15, onvalue=1, offvalue=0, command=check_seats)
    seat16 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='C4', width=seat_width,
                         height=seat_height, variable=seat_var16, onvalue=1, offvalue=0, command=check_seats)
    seat17 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='C5', width=seat_width,
                         height=seat_height, variable=seat_var17, onvalue=1, offvalue=0, command=check_seats)
    seat18 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='C6', width=seat_width,
                         height=seat_height, variable=seat_var18, onvalue=1, offvalue=0, command=check_seats)
    seat19 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='D1', width=seat_width,
                         height=seat_height, variable=seat_var19, onvalue=1, offvalue=0, command=check_seats)
    seat20 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='D2', width=seat_width,
                         height=seat_height, variable=seat_var20, onvalue=1, offvalue=0, command=check_seats)
    seat21 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='D3', width=seat_width,
                         height=seat_height, variable=seat_var21, onvalue=1, offvalue=0, command=check_seats)
    seat22 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='D4', width=seat_width,
                         height=seat_height, variable=seat_var22, onvalue=1, offvalue=0, command=check_seats)
    seat23 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='D5',
                         width=seat_width, height=seat_height, variable=seat_var23, onvalue=1, offvalue=0, command=check_seats)
    seat24 = Checkbutton(screen3, activebackground=green, bg=blue, font=main_font, text='D6',
                         width=seat_width, height=seat_height, variable=seat_var24, onvalue=1, offvalue=0, command=check_seats)

    # Placing seats in specific locations
    global listm
    list_1 = [seat1, seat2, seat3, seat4, seat5, seat6]
    list_2 = [seat7, seat8, seat9, seat10, seat11, seat12]
    list_3 = [seat13, seat14, seat15, seat16, seat17, seat18]
    list_4 = [seat19, seat20, seat21, seat22, seat23, seat24]
    listm = (seat_var1, seat_var2, seat_var3, seat_var4, seat_var5, seat_var6, seat_var7, seat_var8, seat_var9, seat_var10, seat_var11, seat_var12, seat_var13, seat_var14, seat_var15, seat_var16, seat_var17, seat_var18, seat_var19, seat_var20,
             seat_var21, seat_var22, seat_var23, seat_var24)
    listn = list_1 + list_2 + list_3 + list_4

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
        'Helvetica', 16), command=screen_4)
    proceed_button.place(x=700, y=755)
    back_button = Button(screen3, width=10, text='Back', font=(
        'Helvetica', 16), command=screen3.destroy)
    back_button.place(x=25, y=755)


def screen_4():  # Confirming all details
    for i in range(len(listm)):
        if listm[i].get() == 1:
            listn[i].configure(state=DISABLED)

    global screen4
    screen4 = Toplevel()
    screen4.title('Ticket details')
    screen4.geometry('1500x800+10+15')
    screen4.resizable(False, False)

    Heading = Label(screen4, activebackground='black', activeforeground='green',
                    width=26, height=3, font=('Algerian', 30), text='Booking Confirmed')
    Heading.place(x=450, y=0)

    username = input_box.get()
    movie_user = Label(master=screen4, text='User Name: '+username,
                       font=small_font)
    movie_user.place(x=100, y=200)

    userchoice = film_var.get()
    movie_Name = Label(master=screen4, text='Movie name: '+userchoice,
                       font=small_font)
    movie_Name.place(x=100, y=275)
    movie_theater = Label(master=screen4, text='Theatre: '+'NCFE Miniplex',
                          font=small_font)
    movie_theater.place(x=100, y=350)

    movie_timing = Label(master=screen4, text='Time: '+Time,
                         font=small_font)
    movie_timing.place(x=100, y=425)

    seatno = people_var.get()
    movie_noofseats = Label(master=screen4, text='Number of tickets: '+str(seatno),
                            font=small_font)
    movie_noofseats.place(x=100, y=500)

    confirmation_dialog = Label(master=screen4, text='Congratulations! Your booking has been completed successfully',
                                font=('Copperplate Gothic Light', 25))
    confirmation_dialog.place(x=100, y=600)

    # Submit and exit buttons:
    exit_button = Button(screen4, text='Exit', width=10,
                         command=closewindow, height=1, font=('Helvetica', 15))
    exit_button.place(x=1375, y=755)

    back_button = Button(screen4, width=10, text='Back', font=(
        'Helvetica', 16), command=screen4.destroy)
    back_button.place(x=25, y=755)


start_button = Button(window, width=10, text='START',
                      font=('Helvetica', 16), command=screen_1)
start_button.place(x=242, y=200)

# Required command to launch output window
window.mainloop()
