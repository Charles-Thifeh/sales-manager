from tkinter import *
import tkinter.messagebox

global atp, aitn, aitp, aitq, aitT
atp = []
aitn = []
aitp = []
aitq = []
aitT = []

class user:
    def login():
        #create window object
        window = Tk()
        window.title("Login")
        window.geometry("300x200+100+100")

        #define labels
        lab1 = Label(window, text="UserID")
        lab1.place(x=50,y=50)

        lab2 = Label(window, text="Password")
        lab2.place(x=50, y=90)

        #define Entries
        userID = StringVar()
        ent1 = Entry(window, textvariable=userID)
        userID.set("userID")
        ent1.place(x=120,y=50)

        password = StringVar()
        ent1 = Entry(window, textvariable=password, show='*')
        password.set("******")
        ent1.place(x=120, y=90)

        #define button
        log = Button(window, text='Login', command='')
        log.place(x=150, y=120)

        window.mainloop()

dd = user.login()
# dd = user.newSales()
