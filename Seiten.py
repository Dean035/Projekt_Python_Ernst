import math
from tkinter import *
from Datenbank import *
import matplotlib.pyplot as ppt
import numpy as np


Anmeldung = Tk()
Anmeldung.title("Anmeldung")

Anmeldung.geometry("400x400")
Anmeldung.resizable(width=0, height=0)


def inpAnmeldung():
    current_input = Benutzernameeingabe.get()
    current_input2 = Passworteingabe.get()
    print(current_input, current_input2)

    def OkButtonClick():
        Erroranm.destroy()

    if Prüfanm(current_input, current_input2):
        Mainwindow = Tk()
        Mainwindow.title("Mainwindow")
        Anmeldung.withdraw()
        Mainwindow.geometry("650x450")
        Mainwindow.resizable(width=0, height=0)
        Funktionen = StringVar(Mainwindow)
        Funktionen.set("Funktionen")
    else:
        Erroranm = Tk()
        Erroranm.title("Error")
        Erroranm.geometry("500x50")
        Erroranm.resizable(width=0, height=0)
        OkButton = Button(Erroranm, text="Ok", command=OkButtonClick)
        LabelFail = Label(Erroranm,
                          text="Dieser Account existiert nicht! Bitte versuchen sie es erneut")

        LabelFail.pack()
        OkButton.pack()


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
            fenster.title("Lineare-Funktion")
            fenster.geometry("800x600")
            fenster.resizable(width=0, height=0) #macht das die seite nicht vergrößert werden kann

           # butoon3 = Button(fenster, text="Zoom-in", )
           # butoon4 = Button(fenster, text="Zoom-out", )
            bisle = Entry(fenster, bd=5, width=12)  # wie weit y geht (bis) start = 0 (textboxen)
            lab1=Label(fenster,text="bis" )
            lab1.pack()
            lab1.place(x=7, y=435)

            vonle = Entry(fenster, bd=5, width=12)  # wie weit x geht (textboxen)
            lab2 = Label(fenster, text="von")
            lab2.pack()
            lab2.place(x=7, y=375)

            btexte = Entry(fenster, bd=5, width=12)  # yachsenabschnitt (textboxen)
            lab3 = Label(fenster, text="Y-Achsenabschnit")
            lab3.pack()
            lab3.place(x=7, y=315)

            mtexte = Entry(fenster, bd=5, width=12)  # steigung (textboxen)
            lab4 = Label(fenster, text="Steigung")
            lab4.pack()
            lab4.place(x=7, y=255)

            xbeschriftung = Entry(fenster, bd=5, width=12)  # name für xseite (textboxen)
            lab5 = Label(fenster, text="Name-X")
            lab5.pack()
            lab5.place(x=7, y=205)

            ybeschriftung = Entry(fenster, bd=5, width=12)  # name für yseite (textboxen)
            lab6 = Label(fenster, text="Name-Y")
            lab6.pack()
            lab6.place(x=7, y=145)

            def Rechnen():          #Formel für Lineare-Funktion
                ppt.title("Lineare-Funktion")
                ppt.ylabel(ybeschriftung.get())
                ppt.xlabel(xbeschriftung.get())
                vonl = vonle.get()
                bisl = bisle.get()
                btext = btexte.get()
                mtext = mtexte.get()
                vonl = float(vonl)
                btext = float(btext)
                mtext = float(mtext)
                bisl = float(bisl)

                aaa = ppt.gca()
                ppt.gca().set_aspect('equal')
                aaa.set_xticks(range(-10, 10, 1))
                aaa.set_yticks(range(-10, 10, 1))
                aaa.set_xlim([vonl, bisl])
                aaa.set_ylim([vonl, bisl])

                X =np.linspace(-10,10,100)
                Y = mtext * X + btext

                ppt.grid()
                ppt.plot(X, Y)
                ppt.show()

            def Beispill():
                x = np.linspace(-5, 5, 100)
                y = 4 * x + 2
                ppt.plot(x, y, '-r', label='y=4x+2')
                ppt.title('Der Graph von y=4x+2')
                ppt.xlabel('x')
                ppt.ylabel('y')
                ppt.grid()
                ppt.show()

            butoon1 = Button(fenster, text="Ausführen", command=Rechnen)#buttons
            butoon2 = Button(fenster, text="Beispiele", command=Beispill)


            vonle.pack(), bisle.pack(), btexte.pack(), mtexte.pack(), xbeschriftung.pack(), ybeschriftung.pack(),
            butoon2.pack(), butoon1.pack() #zeigt die scheiße an

            ## butoon3.place(x=100, y=555), butoon4.place(x=180, y=555)

            bisle.place(x=7, y=460), vonle.place(x=7, y=400), btexte.place(x=7, y=340), mtexte.place(x=7, y=280),
            xbeschriftung.place(x=7, y=230), ybeschriftung.place(x=7, y=170), butoon1.place(x=7, y=40),
            butoon2.place(x=7, y=555) #wo stehen die einzelen buttons usw

        elif Auswahl == "Quadratische-Funktion":
            Quadratisch = Tk()
            Quadratisch.title("Quadratische-Funktion")
            Quadratisch.geometry("400x400")
            Quadratisch.geometry("800x600")
            Quadratisch.resizable(width=0, height=0)

            def RechnungQuadr():
                ppt.title("Quadratischen-Funktion")
                ppt.ylabel(Eingabe6.get())
                ppt.xlabel(Eingabe7.get())
                a = Eingabe1.get()
                b = Eingabe2.get()
                c = Eingabe3.get()
                von = Eingabe4.get()
                bis = Eingabe5.get()
                aa = float(a)
                bb = float(b)
                cc = float(c)
                vv = float(von)
                bb = float(bis)


                x = np.linspace(vv, bb, 100)

                y = aa * x ** 2 + bb * x + cc

                bbb = bb / aa
                aaa = aa / aa
                ccc = cc / aa

                pq = -bbb/2 + math.sqrt((bbb/2)**2 - (ccc))
                pq2 = -bbb/2 - math.sqrt((bbb/2)**2 - (ccc))

                Ableitung1 = aa * 2 + bb

 
                yA = 0
                Zeile1 = yA - bb
                Zeile2 = aa / aa
                Zeile3 = yA / aa
                
                xA


                #if aa < 0:
                #    Ableitung1kl =

                xxx=[pq, pq2,]
                yyy=[0, 0]
                ppt.scatter(xxx, yyy, color="red")
                ppt.plot(x, y, '-r', label='y=')

                ppt.grid()
                ppt.show()

            def matplotbeispiel():
                x = np.linspace(-10, 10, 100)
                a = 5
                b = 3
                c = 4
                y = (a * x ** 2) + (b * x) + c
                ppt.plot(x, y, '-r', label='y=')
                ppt.title('Der Graph von y=4x+2')
                ppt.xlabel('x')
                ppt.ylabel('y')
                ppt.grid()
                ppt.show()

            '''def matplotbeispiel2():
                x = np.linspace(-10, 10, 100)
                a = 5
                PX = 3
                PY = 4
                SX = 1
                SY = 1
                y = a * (PX - SX) ** 2 + SY
                ppt.plot(x, y, '-r', label='y=')
                ppt.title('Der Graph von y=4x+2')
                ppt.xlabel('x')
                ppt.ylabel('y')
                ppt.grid()
                ppt.show()'''

            Normalform = Label(Quadratisch, text="Normalform:")
            Normalform.pack()
            Normalform.place(x=7, y=10)

            Labello1 = Label(Quadratisch, text="a")
            Labello1.pack()
            Labello1.place(x=7, y=25)

            Eingabe1 = Entry(Quadratisch, bd=5, width=12)
            Eingabe1.pack()
            Eingabe1.place(x=7, y=50)

            Labello2 = Label(Quadratisch, text="b")
            Labello2.pack()
            Labello2.place(x=7, y=75)

            Eingabe2 = Entry(Quadratisch, bd=5, width=12)
            Eingabe2.pack()
            Eingabe2.place(x=7, y=100)

            Labello3 = Label(Quadratisch, text="c")
            Labello3.pack()
            Labello3.place(x=7, y=125)

            Eingabe3 = Entry(Quadratisch, bd=5, width=12)
            Eingabe3.pack()
            Eingabe3.place(x=7, y=150)

            Labello4 = Label(Quadratisch, text="von")
            Labello4.pack()
            Labello4.place(x=7, y=175)

            Eingabe4 = Entry(Quadratisch, bd=5, width=12)
            Eingabe4.pack()
            Eingabe4.place(x=7, y=200)

            Labello4 = Label(Quadratisch, text="bis")
            Labello4.pack()
            Labello4.place(x=7, y=225)

            Eingabe5 = Entry(Quadratisch, bd=5, width=12)
            Eingabe5.pack()
            Eingabe5.place(x=7, y=250)

            Labello5 = Label(Quadratisch, text="Y-Name")
            Labello5.pack()
            Labello5.place(x=7, y=275)

            Eingabe6 = Entry(Quadratisch, bd=5, width=12)
            Eingabe6.pack()
            Eingabe6.place(x=7, y=300)

            Labello6 = Label(Quadratisch, text="X-Name")
            Labello6.pack()
            Labello6.place(x=7, y=325)

            Eingabe7 = Entry(Quadratisch, bd=5, width=12)
            Eingabe7.pack()
            Eingabe7.place(x=7, y=350)

            Button2 = Button(Quadratisch, text="Beispiel", command=matplotbeispiel)
            Button2.pack()
            Button2.place(x=7, y=450)

            Button1 = Button(Quadratisch, text="Ausführen", command=RechnungQuadr)
            Button1.pack()
            Button1.place(x=7, y=500)


            '''Scheitelpunktform = Label(Quadratisch, text="Scheitelpunktform:")
            Scheitelpunktform.pack()
            Scheitelpunktform.place(x=650, y=10)

            Labello_1 = Label(Quadratisch, text="a")
            Labello_1.pack()
            Labello_1.place(x=650, y=50)

            Eingabe_1 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_1.pack()
            Eingabe_1.place(x=650, y=75)

            Labello_2 = Label(Quadratisch, text="Y-Punkt")
            Labello_2.pack()
            Labello_2.place(x=650, y=100)

            Eingabe_2 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_2.pack()
            Eingabe_2.place(x=650, y=125)

            Labello_3 = Label(Quadratisch, text="X-Punkt")
            Labello_3.pack()
            Labello_3.place(x=650, y=150)

            Eingabe___2 = Entry(Quadratisch, bd=5, width=12)
            Eingabe___2.pack()
            Eingabe___2.place(x=650, y=175)

            Labello__2 = Label(Quadratisch, text="Y-SPunkt")
            Labello__2.pack()
            Labello__2.place(x=650, y=200)

            Eingabe__2 = Entry(Quadratisch, bd=5, width=12)
            Eingabe__2.pack()
            Eingabe__2.place(x=650, y=225)

            Labello__3 = Label(Quadratisch, text="X-SPunkt")
            Labello__3.pack()
            Labello__3.place(x=650, y=250)

            Eingabe_3 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_3.pack()
            Eingabe_3.place(x=650, y=275)

            Labello_4 = Label(Quadratisch, text="von")
            Labello_4.pack()
            Labello_4.place(x=650, y=300)

            Eingabe_4 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_4.pack()
            Eingabe_4.place(x=650, y=325)

            Labello__4 = Label(Quadratisch, text="bis")
            Labello__4.pack()
            Labello__4.place(x=650, y=350)

            Eingabe_5 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_5.pack()
            Eingabe_5.place(x=650, y=375)

            Labello_5 = Label(Quadratisch, text="Y-Name")
            Labello_5.pack()
            Labello_5.place(x=650, y=400)

            Eingabe_6 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_6.pack()
            Eingabe_6.place(x=650, y=425)

            Labello_6 = Label(Quadratisch, text="X-Name")
            Labello_6.pack()
            Labello_6.place(x=650, y=450)

            Eingabe_7 = Entry(Quadratisch, bd=5, width=12)
            Eingabe_7.pack()
            Eingabe_7.place(x=650, y=475)

            Button_2 = Button(Quadratisch, text="Beispiel", command=matplotbeispiel2)
            Button_2.pack()
            Button_2.place(x=650, y=500)

            Button_1 = Button(Quadratisch, text="Ausführen")
            Button_1.pack()
            Button_1.place(x=650, y=525)'''

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

    def logout():
        Mainwindow.destroy()
        Anmeldung.deiconify()


    logout = Button(Mainwindow, text="Abmelden", command=logout)
    logout.pack()
    logout.place(relx=0.9, rely=0.0)
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
                def OkButtonClick():
                    ErrorRgst.destroy()
                ErrorRgst = Tk()
                ErrorRgst.title("Error")
                ErrorRgst.geometry("500x50")
                ErrorRgst.resizable(width=0, height=0)
                OkButton = Button(ErrorRgst, text="Ok", command=OkButtonClick)
                LabelFail = Label(ErrorRgst,
                                  text="Dieser Benutzername existiert bereits! Bitte wählen Sie einen anderen!")

                LabelFail.pack()
                OkButton.pack()
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
