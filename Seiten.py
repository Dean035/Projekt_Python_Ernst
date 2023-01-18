from tkinter import *
from Datenbank import NewAcc, Ausgabe

Anmeldung = Tk()
Anmeldung.title("Anmeldung")

Anmeldung.geometry("400x400")
Anmeldung.resizable(width=0, height=0)



def inpAnmeldung():
    current_input = Benutzernameeingabe.get()
    current_input2 = Passworteingabe.get()
    print(current_input, current_input2)
    Mainwindow = Tk()
    Mainwindow. title("Mainwindow")
    Anmeldung.destroy()
    Mainwindow.geometry("650x450")
    Mainwindow.resizable(width=0, height=0)
    Funktionen = StringVar(Mainwindow)
    Funktionen.set("Funktionen")

    def show(selection):
        Auswahl = selection
        if Auswahl == "Lineare-Funktion":
            Linear = Tk()
            Linear.title("Lineare-Funktion")
            Linear.geometry("600x600")
            Linear.resizable(width=0, height=0)
            butoon1 = Button(Linear,text= "Ausführen",)
            butoon2 = Button(Linear, text="Beispiele",)
            butoon3 = Button(Linear, text="Zoom-in",)
            butoon4 = Button(Linear, text="Zoom-out",)
            ytext = Entry(Linear, bd=5, width= 7)
            xtext = Entry(Linear, bd=5, width= 7)
            btext = Entry(Linear, bd=5, width= 7)
            mtext = Entry(Linear, bd=5, width= 7)
            xbeschriftung = Entry(Linear, bd=5, width= 7)
            ybeschriftung = Entry(Linear, bd=5, width= 7)

            ytext.pack(), xtext.pack(), btext.pack(), mtext.pack(), xbeschriftung.pack(), ybeschriftung.pack(),
            butoon4.pack(), butoon3.pack(), butoon2.pack(), butoon1.pack()

            ytext.place(relx= 2.1, rely=7.8), xtext.place(relx= 4.1, rely=6.8)


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


    drop = OptionMenu(Mainwindow, Funktionen,  "Lineare-Funktion" , "Quadratische-Funktion" ,
                      "Ganzrationale-Funktionen" ,"Trigonometrische-Funktionen" , "Exponential-Funktionen" ,
                      "Einstieg-Differenzialrechnung" , "Kurvendiskussion", "Integralrechnung", command=show)





    drop.pack()
    drop.place(relx=0.0, rely=0.0)

def register():
    Register = Tk()
    Register.title("Registration")
    #Anmeldung.destroy()

    def Rgstinp():
        RgstinpBenutzername = RgstBenutzereingabe.get()
        RgstinpPasswort = RgstPassworteingabe.get()
        RgstinpPasswortConfirm = RgstConfirmeingabe.get()

        if RgstinpPasswort == RgstinpPasswortConfirm:
            print(RgstinpBenutzername, RgstinpPasswort, RgstinpPasswortConfirm)
        else:
            print("Das Passwort und die Bestätigung des Passworts stimmen nicht überein")
        
        NewAcc(RgstBenutzereingabe.get(), RgstPassworteingabe.get())
        Ausgabe()
        
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

