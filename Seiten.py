from tkinter import *
import Datenbank

Anmeldung = Tk()
Anmeldung.title("Anmeldung")

Anmeldung.geometry("400x400")
Anmeldung.resizable(width=0, height=0)

def Main():
    Mainwindow = Tk()
    Mainwindow. title("Mainwindow")
    Anmeldung.destroy()

def inpAnmeldung():
    current_input = Benutzernameeingabe.get()
    current_input2 = Passworteingabe.get()
    print(current_input, current_input2)

def register():
    Register = Tk()
    Register.title("Registration")
    Anmeldung.destroy()



    RgstBenutzername = Label(Register, text="Benutzername")
    RgstBenutzereingabe = Entry(Register, bd=5, width=40)
    RgstPasswort = Label(Register, text="Passwort")
    RgstPassworteingabe = Entry(Register, bd=5, width=40)
    RgstConfirm = Label(Register, text="Bestätigung des Passworts")
    RgstConfirmeingabe = Entry(Register, bd=5, width=40)
    RgstButton = Button(Register, text="Registrieren")

    RgstBenutzername.pack()
    RgstBenutzereingabe.pack()
    RgstPasswort.pack()
    RgstPassworteingabe.pack()
    RgstConfirm.pack()
    RgstConfirmeingabe.pack()
    RgstButton.pack()

Rgstlabel = Label(Anmeldung, text="Wenn Sie noch keinen Account besitzen Drücken sie bitte hier:")
Rgstbutton = Button(Anmeldung, text="Registration", command=register)
Benutzernamelabel = Label(Anmeldung, text="Benutzername")
Anmeldungsbutton = Button(Anmeldung, text="Anmelden", command=inpAnmeldung, Main)
Benutzernameeingabe = Entry(Anmeldung, bd=5, width= 40)
Passwortlabel = Label(Anmeldung, text="Passwort")
Passworteingabe = Entry(Anmeldung, bd=5, width= 40)





Benutzernamelabel.pack()
Benutzernameeingabe.pack()
Passwortlabel.pack()
Passworteingabe.pack()
Anmeldungsbutton.pack()
Rgstlabel.pack()
Rgstlabel.place(relx= 0.1, rely=0.8)
Rgstbutton.place(relx=0.4, rely=0.9)
Anmeldung.mainloop()

