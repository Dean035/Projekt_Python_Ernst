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
        fenster = Tk()
        fenster.geometry("600x600")
        fenster.resizable(width=0, height=0)
        fenster.title(Auswahl)

        if Auswahl ==  "Lineare-Funktion":
            butoon1 = Button(fenster, text="Ausführen", )
            butoon2 = Button(fenster, text="Beispiele", )
            butoon3 = Button(fenster, text="Zoom-in", )
            butoon4 = Button(fenster, text="Zoom-out", )
            ytext = Entry(fenster, bd=5, width=7)
            xtext = Entry(fenster, bd=5, width=7)
            btext = Entry(fenster, bd=5, width=7)
            mtext = Entry(fenster, bd=5, width=7)
            xbeschriftung = Entry(fenster, bd=5, width=7)
            ybeschriftung = Entry(fenster, bd=5, width=7)

            ytext.pack(), xtext.pack(), btext.pack(), mtext.pack(), xbeschriftung.pack(), ybeschriftung.pack(),
            butoon4.pack(), butoon3.pack(), butoon2.pack(), butoon1.pack()

            ytext.place(x=7, y=235)

        elif Auswahl ==  "Quadratische-Funktion":
            pass
        
        
        elif Auswahl ==  "Ganzrationale-Funktionen":



        elif Auswahl == "Trigonometrische-Funktionen":



        elif Auswahl == "Exponential-Funktionen":



        elif Auswahl == "Einstieg-Differenzialrechnung":



        elif Auswahl == "Kurvendiskussion":
          
       
                       
        elif Auswahl == "Integralrechnung":

            




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
            NewAcc(RgstBenutzereingabe.get(), RgstPassworteingabe.get())
            Ausgabe()
            Register.destroy()
        else:
            print("Das Passwort und die Bestätigung des Passworts stimmen nicht überein")
            RegisterFail = Tk()
            RegisterFail.title("Error")
            RegisterFail.geometry("500x50")
            RegisterFail.resizable(width=0, height=0)

            def OkButtonClick():
                RegisterFail.destroy()

            OkButton = Button(RegisterFail, text="Ok", command=OkButtonClick)
            LabelFail = Label(RegisterFail, text="Das Passwort und die Bestätigung des Passwortes stimmen nicht überein!")

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


