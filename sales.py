from users import *
from dbsetup import *
from tkinter import *
import tkinter.messagebox


def newSales():
    #create window object
    new = Tk()
    new.title("New")
    new.geometry("500x400+350+180")
    new.lift()

    #define labels
    lab = Label(new,text="      ")
    lab.grid(row=0, column=0,columnspan=5)
    lab1 = Label(new, text="Item name: ")
    lab1.grid(row=1,column=0)

    lab2 = Label(new, text="Item price: ₦")
    lab2.grid(row=2,column=0)

    lab3 = Label(new, text="Quantity: ")
    lab3.grid(row=1,column=3)

    lab4 = Label(new, text="Item type: ")
    lab4.grid(row=2,column=3)

    #define Entries
    global name, price, quan, itemT
    name = StringVar()
    ent1 = Entry(new, textvariable=name)
    name.set("Blue Biro")
    ent1.grid(row=1,column=1)

    price = IntVar()
    ent2 = Entry(new, textvariable=price)
    price.set("30")
    ent2.grid(row=2, column=1)

    quan = IntVar()
    ent3 = Entry(new, textvariable=quan)
    quan.set("1")
    ent3.grid(row=1,column=4)

    itemT = StringVar()
    ent4 = Entry(new, textvariable=itemT)
    itemT.set("Stationary")
    ent4.grid(row=2, column=4)

        #define button

    lab = Label(new, text="      ")
    lab.grid(row=3, column=0, columnspan=5)
    but = Button(new, text="Add to Sale",command=addTo)
    but.grid(row=4, column=2,rowspan=2)

        #define sales list

    global itn, itp, itq, itt, tp

    itn = Listbox(new)
    itp = Listbox(new)
    itq = Listbox(new)
    itt = Listbox(new)
    tp = Listbox(new, width=12)
    itn.place(x=0,y=150)
    itp.place(x=80, y=150)
    itq.place(x=160, y=150)
    itt.place(x=240, y=150)
    tp.place(x=320, y=150)


    btn = Button(new, text="Record Sale", command=recordSale)
    btn.place(x=420, y=150)

    new.mainloop()


def addTo():
    itn1 = name.get()
    itp1 = price.get()
    itq1 = quan.get()
    itt1 = itemT.get()
    if itn1 and itp1 and itq1 and itt1:
        itn.insert(END, itn1)
        aitn.append(itn1)
        itp.insert(END, itp1)
        aitp.append(itp1)
        itq.insert(END, itq1)
        aitq.append(itq1)
        itt.insert(END, itt1)
        aitT.append(itt1)
        tp1 = itp1 * itq1
        atp.append(tp1)
        tp.insert(END, tp1)
        price.set("0")
        quan.set("0")
    elif itp1 == 0 or itq1 == 0 or itn1 =="":
        tkinter.messagebox.showerror('Error', 'Fill in all fields before adding to sale')
    else:
        tkinter.messagebox.showerror('Error', 'Fill in all fields before adding to sale')

def recordSale():
    total = 0
    for pr in atp:
        total = total + pr

    stotal = str(total)
    tkinter.messagebox.showinfo('Total', 'Total Amount = '+stotal+' ')


class mainwindow:
    def screen():
        #create windows
        window = Tk()
        window.title("Sales Manager")
        window.geometry('800x600+100+0')

        #define menu
        menu = Menu(window)
        window.config(menu=menu)

        #define filemenu
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label='New', command=newSales)
        # subMenu.add_command(label="About", command='')
        subMenu.add_separator()
        subMenu.add_command(label='Exit', command=window.destroy)

        #define editmenu
        helpMenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpMenu)
        helpMenu.add_command(label='Help', command='')
        helpMenu.add_command(label='About', command='')

        #left frame
        left = Frame(window, height='700', width='250', bg='lightgrey')

        left.grid(rowspan=1, column=0)

        #top-right frame
        top_right = Frame(window, height='300', width='548', bg='yellow')

        top_right.place(x=250, y=0)

        #bottom-right frame
        bottom_right = Frame(window, height='298', width='548', bg='blue')

        bottom_right.place(x=251, y=302)

        window.mainloop()

h=mainwindow.screen()