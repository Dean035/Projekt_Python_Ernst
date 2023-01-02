from tkinter import *
import Datenbank

Anmeldung = Tk()
Anmeldung.title("Anmeldung")

def Main():
    Mainwindow = Tk()
    Mainwindow. title("Mainwindow")
    Anmeldung.destroy()

Benutzernamelabel = Label(Anmeldung, text="Benutzername")
Anmeldungsbutton = Button(Anmeldung, text="Anmelden", command=Main)
Benutzernameeingabe = Entry(Anmeldung, bd=5, width= 40)
Passwortlabel = Label(Anmeldung, text="Passwort")
Passworteingabe = Entry(Anmeldung, bd=5, width= 40)




Benutzernamelabel.pack()
Benutzernameeingabe.pack()
Passwortlabel.pack()
Passworteingabe.pack()
Anmeldungsbutton.pack()

Anmeldung.mainloop()

