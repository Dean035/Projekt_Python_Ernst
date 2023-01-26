from tkinter import *
from Datenbank import *
import matplotlib.pyplot as ppt

Anmeldung = Tk()
Anmeldung.title("Anmeldung")

Anmeldung.geometry("400x400")
Anmeldung.resizable(width=0, height=0)


def inpAnmeldung():
    current_input = Benutzernameeingabe.get()
    current_input2 = Passworteingabe.get()
    print(current_input, current_input2)
    #Prüfanm(current_input, current_input2)
    Mainwindow = Tk()
    Mainwindow.title("Mainwindow")
    Anmeldung.destroy()
    Mainwindow.geometry("650x450")
    Mainwindow.resizable(width=0, height=0)
    Funktionen = StringVar(Mainwindow)
    Funktionen.set("Funktionen")

    def lingraf():
        ppt.ylabel('numbers')
        ppt.plot([1, 2, 3, 4])
        #dd_x = [1, 6, 9, 7, 90]

        #dd_y = [3, 5, 7, 89, 90]

        #ppt.plot([dd_x], [dd_y])
        ppt.show()

    def show(selection):

        Auswahl = selection
        if Auswahl == "Lineare-Funktion":
            fenster = Tk()
            fenster.geometry("800x600")
            fenster.resizable(width=0, height=0)
            butoon1 = Button(fenster, text="Ausführen", command=lingraf())
            butoon2 = Button(fenster, text="Beispiele", )
            butoon3 = Button(fenster, text="Zoom-in", )
            butoon4 = Button(fenster, text="Zoom-out", )
            ytext = Entry(fenster, bd=5, width=12)
            xtext = Entry(fenster, bd=5, width=12)
            btext = Entry(fenster, bd=5, width=12)
            mtext = Entry(fenster, bd=5, width=12)
            xbeschriftung = Entry(fenster, bd=5, width=12)
            ybeschriftung = Entry(fenster, bd=5, width=12)

            ytext.pack(), xtext.pack(), btext.pack(), mtext.pack(), xbeschriftung.pack(), ybeschriftung.pack(),
            butoon4.pack(), butoon3.pack(), butoon2.pack(), butoon1.pack(),

            ytext.place(x=7, y=340), xtext.place(x=7, y=300), btext.place(x=7, y=260), mtext.place(x=7, y=220),
            xbeschriftung.place(x=7, y=180), ybeschriftung.place(x=7, y=140), butoon1.place(x=7, y=40),
            butoon2.place(x=7, y=555), butoon3.place(x=100, y=555), butoon4.place(x=180, y=555)

            ytext.pack(), xtext.pack(), btext.pack(), mtext.pack(), xbeschriftung.pack(), ybeschriftung.pack(),
            butoon4.pack(), butoon3.pack(), butoon2.pack(), butoon1.pack()

            ytext.place(relx=2.1, rely=7.8), xtext.place(relx=4.1, rely=6.8)


        elif Auswahl == "Quadratische-Funktion":
            Quadratisch = Tk()
            Quadratisch.title("Quadratische-Funktion")
            Quadratisch.geometry("400x400")
            Quadratisch.resizable(width=0, height=0)
        elif Auswahl == "Ganzrationale-Funktionen":
            Ganzrational = Tk()
            Ganzrational.title("Ganzrationale-Funktionen")
            Ganzrational.geometry("400x400")
            Ganzrational.resizable(width=0, height=0)
        elif Auswahl == "Trigonometrische-Funktionen":
            Trigonomisch = Tk()
            Trigonomisch.title("Trigonometrische-Funktionen")
            Trigonomisch.geometry("400x400")
            Trigonomisch.resizable(width=0, height=0)
        elif Auswahl == "Exponential-Funktionen":
            Exponential = Tk()
            Exponential.title("Exponential-Funktionen")
            Exponential.geometry("400x400")
            Exponential.resizable(width=0, height=0)
        elif Auswahl == "Einstieg-Differenzialrechnung":
            Differenzial = Tk()
            Differenzial.title("Einstieg-Differenzialrechnung")
            Differenzial.geometry("400x400")
            Differenzial.resizable(width=0, height=0)
        elif Auswahl == "Kurvendiskussion":
            Kurven = Tk()
            Kurven.title("Kurvendiskussion")
            Kurven.geometry("400x400")
            Kurven.resizable(width=0, height=0)
        elif Auswahl == "Integralrechnung":
            Integral = Tk()
            Integral.title("Integralrechnung")
            Integral.geometry("400x400")
            Integral.resizable(width=0, height=0)

    drop = OptionMenu(Mainwindow, Funktionen, "Lineare-Funktion", "Quadratische-Funktion",
                      "Ganzrationale-Funktionen", "Trigonometrische-Funktionen", "Exponential-Funktionen",
                      "Einstieg-Differenzialrechnung", "Kurvendiskussion", "Integralrechnung", command=show)

    drop.pack()
    drop.place(relx=0.0, rely=0.0)


def register():
    Register = Tk()
    Register.title("Registration")

    # Anmeldung.destroy()

    def Rgstinp():
        RgstinpBenutzername = RgstBenutzereingabe.get()
        RgstinpPasswort = RgstPassworteingabe.get()
        RgstinpPasswortConfirm = RgstConfirmeingabe.get()

        if RgstinpPasswort == RgstinpPasswortConfirm and RgstinpBenutzername != "":
            if PrüfungRgst(RgstinpBenutzername):
                print(RgstinpBenutzername, RgstinpPasswort, RgstinpPasswortConfirm)
                NewAcc(RgstBenutzereingabe.get(), RgstPassworteingabe.get())
                Ausgabe()
                Register.destroy()
            else:
                Error123 = Tk()
        else:
            print("Das Passwort und die Bestätigung des Passworts stimmen nicht überein")
            RegisterFail = Tk()
            RegisterFail.title("Error")
            RegisterFail.geometry("500x50")
            RegisterFail.resizable(width=0, height=0)

            def OkButtonClick():
                RegisterFail.destroy()

            OkButton = Button(RegisterFail, text="Ok", command=OkButtonClick)
            LabelFail = Label(RegisterFail,
                              text="Das Passwort und die Bestätigung des Passwortes stimmen nicht überein!")

            LabelFail.pack()
            OkButton.pack()

    RgstBenutzername = Label(Register, text="Benutzername")
    RgstBenutzereingabe = Entry(Register, bd=5, width=40)
    RgstPasswort = Label(Register, text="Passwort")
    RgstPassworteingabe = Entry(Register, bd=5, width=40)
    RgstConfirm = Label(Register, text="Bestätigung des Passworts")
    RgstConfirmeingabe = Entry(Register, bd=5, width=40)

    RgstButton = Button(Register, text="Registrieren", command=Rgstinp)

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
Anmeldungsbutton = Button(Anmeldung, text="Anmelden", command=inpAnmeldung)
Benutzernameeingabe = Entry(Anmeldung, bd=5, width=40)
Passwortlabel = Label(Anmeldung, text="Passwort")
Passworteingabe = Entry(Anmeldung, bd=5, width=40)

Benutzernamelabel.pack()
Benutzernameeingabe.pack()
Passwortlabel.pack()
Passworteingabe.pack()
Anmeldungsbutton.pack()
Rgstlabel.pack()
Rgstlabel.place(relx=0.1, rely=0.8)
Rgstbutton.place(relx=0.4, rely=0.9)
Anmeldung.mainloop()
