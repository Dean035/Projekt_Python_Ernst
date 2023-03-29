from tkinter import *
from Datenbank import *
import matplotlib.pyplot as plt
import numpy as np

Anmeldung_fenster = Tk()
Anmeldung_fenster.title("Anmeldung")

Anmeldung_fenster.geometry("400x400")
Anmeldung_fenster.resizable(width=0, height=0)


def inpAnmeldung():
    current_input = Benutzernameeingabe.get()
    current_input2 = Passworteingabe.get()
    print(current_input, current_input2)

    def OkButtonClick():
        Erroranm.destroy()

    if Prüfanm(current_input, current_input2):
        Mainwindow = Tk()
        Mainwindow.title("Mainwindow")
        Anmeldung_fenster.withdraw()
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

    def show(selection):

        Auswahl = selection
        if Auswahl == "Lineare-Funktion":
            fenster = Tk()
            fenster.title("Lineare-Funktion")
            fenster.geometry("800x600")
            fenster.resizable(width=0, height=0)  # macht das die seite nicht vergrößert werden kann

            bisle = Entry(fenster, bd=5, width=12)  # wie weit y geht (bis) start = 0 (textboxen)
            lab1 = Label(fenster, text="bis")
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

            def Rechnen():  # Formel für Lineare-Funktion
                plt.title("Lineare-Funktion")
                plt.ylabel(ybeschriftung.get())
                plt.xlabel(xbeschriftung.get())
                vonl = vonle.get()
                bisl = bisle.get()
                btext = btexte.get()
                mtext = mtexte.get()
                vonl = float(vonl)
                btext = float(btext)
                mtext = float(mtext)
                bisl = float(bisl)

                aaa = plt.gca()
                plt.gca().set_aspect('equal')
                aaa.set_xticks(range(-10, 10, 1))
                aaa.set_yticks(range(-10, 10, 1))
                aaa.set_xlim([vonl, bisl])
                aaa.set_ylim([vonl, bisl])

                X = np.linspace(-10, 10, 100)
                Y = mtext * X + btext

                plt.grid()
                plt.plot(X, Y)
                plt.show()

            def Beispill():
                x = np.linspace(-5, 5, 100)
                y = 4 * x + 2
                plt.plot(x, y, '-r', label='y=4x+2')
                plt.title('Der Graph von y=4x+2')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid()
                plt.show()

            butoon1 = Button(fenster, text="Ausführen", command=Rechnen)  # buttons
            butoon2 = Button(fenster, text="Beispiele", command=Beispill)

            vonle.pack(), bisle.pack(), btexte.pack(), mtexte.pack(), xbeschriftung.pack(), ybeschriftung.pack(),
            butoon2.pack(), butoon1.pack()  # zeigt die scheiße an

            bisle.place(x=7, y=460), vonle.place(x=7, y=400), btexte.place(x=7, y=340), mtexte.place(x=7, y=280),
            xbeschriftung.place(x=7, y=230), ybeschriftung.place(x=7, y=170), butoon1.place(x=7, y=40),
            butoon2.place(x=7, y=555)  # wo stehen die einzelen buttons usw

        elif Auswahl == "Quadratische-Funktion":
            Quadratisch = Tk()
            Quadratisch.title("Quadratische-Funktion")
            Quadratisch.geometry("400x400")
            Quadratisch.resizable(width=0, height=0)



        elif Auswahl == "Ganzrationale-Funktionen":
            Ganzrational = Tk()
            Ganzrational.title("Ganzrationale-Funktionen")
            Ganzrational.geometry("800x600")
            Ganzrational.resizable(width=0, height=0)

            bisge = Entry(Ganzrational, bd=5, width=12)  # wie weit y geht (bis) start = 0 (textboxen)
            lab1 = Label(Ganzrational, text="bis")
            lab1.pack()
            lab1.place(x=7, y=435)

            vonge = Entry(Ganzrational, bd=5, width=12)  # wie weit x geht (textboxen)
            lab2 = Label(Ganzrational, text="von")
            lab2.pack()
            lab2.place(x=7, y=375)

            n_ausgabe = Entry(Ganzrational, bd=5, width=12)  # n (textboxen)
            lab3 = Label(Ganzrational, text="Grad")
            lab3.pack()
            lab3.place(x=7, y=255)

            a_ausgabe = Entry(Ganzrational, bd=5, width=12)  #var1 a (textboxen)
            lab4 = Label(Ganzrational, text="Variable1")
            lab4.pack()
            lab4.place(x=600, y=87)

            xbeschriftungg = Entry(Ganzrational, bd=5, width=12)  # name für xseite (textboxen)
            lab5 = Label(Ganzrational, text="Name-X")
            lab5.pack()
            lab5.place(x=7, y=205)

            ybeschriftungg = Entry(Ganzrational, bd=5, width=12)  # name für yseite (textboxen)
            lab6 = Label(Ganzrational, text="Name-Y")
            lab6.pack()
            lab6.place(x=7, y=145)

            n2_ausgabe = Entry(Ganzrational, bd=5, width=12)  # gibt var2 an  (textboxen)
            lab6 = Label(Ganzrational, text="variable4")
            lab6.pack()
            lab6.place(x=400, y=87)

            n3_ausgabe = Entry(Ganzrational, bd=5, width=12)  # gibt var3 an  (textboxen)
            lab6 = Label(Ganzrational, text="variable3")
            lab6.pack()
            lab6.place(x=300, y=87)

            n4_ausgabe = Entry(Ganzrational, bd=5, width=12)  # gibt var4 an  (textboxen)
            lab6 = Label(Ganzrational, text="variable2")
            lab6.pack()
            lab6.place(x=200, y=87)

            n5_ausgabe = Entry(Ganzrational, bd=5, width=12)  # gibt var4 an  (textboxen)
            lab6 = Label(Ganzrational, text="variable5")
            lab6.pack()
            lab6.place(x=500, y=87)


            def formel_berechnen():
                plt.title("Ganzrationale-Funktionen")
                plt.ylabel(ybeschriftungg.get())
                plt.xlabel(xbeschriftungg.get())
                bisg = bisge.get()
                vong = vonge.get()
                ag_ausgabe = a_ausgabe.get()
                ng_ausgabe = n_ausgabe.get()
                var2_ausgabe = n2_ausgabe.get()
                var2_ausgabe = float(var2_ausgabe)
                ng_ausgabe = float(ng_ausgabe)
                ag_ausgabe = float(ag_ausgabe)
                var3_ausgabe = n3_ausgabe.get()
                var3_ausgabe = float(var3_ausgabe)
                var4_Ausgabe = n4_ausgabe.get()
                var4_Ausgabe = float(var4_Ausgabe)
                var5_Ausgabe = n5_ausgabe.get()
                var5_Ausgabe = float(var5_Ausgabe)
                bisg = float(bisg)
                vong = float(vong)

                ax = plt.gca()  # krodinaten systeme
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(vong,bisg,500)  # erstellt ein array mit 100 glechmäsig verteielten x werten zwischen -10 und 10

                if ng_ausgabe == 3:
                        y = ag_ausgabe * x ** 3 + var2_ausgabe * x ** 2 + var3_ausgabe * x ** 1 \
                            + var4_Ausgabe
                elif ng_ausgabe == 4:
                        y = ag_ausgabe * x ** 4 + var2_ausgabe * x ** 3 + var3_ausgabe * x ** 2 \
                            + var4_Ausgabe * x ** 1 + var5_Ausgabe * x ** 0
                else:

                    def OkButtonClickG():
                        ErrorGrad.destroy()

                    ErrorGrad = Tk()
                    ErrorGrad.title("Error")
                    ErrorGrad.geometry("500x50")
                    ErrorGrad.resizable(width=0, height=0)
                    OkButton = Button(ErrorGrad, text="Ok", command=OkButtonClickG)
                    LabelFail = Label(ErrorGrad,text="Gebe bitte eine grad von 3 bis 4 ein")

                    LabelFail.pack()
                    OkButton.pack()

                plt.plot(x,y)  # stelt alles in matplot_lib dar
                plt.grid()
                plt.show()

            buton1 = Button(Ganzrational, text="Ausführen", command=formel_berechnen)  # buttons
            buton2 = Button(Ganzrational, text="Beispiele", )  # command=)

            vonge.pack(), bisge.pack(), n_ausgabe.pack(), a_ausgabe.pack(), xbeschriftungg.pack(), ybeschriftungg.pack(),
            buton2.pack(), buton1.pack(), n2_ausgabe.pack(),n3_ausgabe.pack(),n4_ausgabe.pack() # zeigt die scheiße an

            ybeschriftungg.place(x=7, y=170), xbeschriftungg.place(x=7, y=230),\
            a_ausgabe.place(x=600, y=110), n_ausgabe.place(x=7, y=280)
            vonge.place(x=7, y=400), bisge.place(x=7, y=460), buton1.place(x=7, y=40), buton2.place(x=7, y=555),\
            n2_ausgabe.place( x=200, y=110),n3_ausgabe.place( x=300, y=110),n4_ausgabe.place( x=400, y=110),\
            n5_ausgabe.place( x=500, y=110),




        elif Auswahl == "Trigonometrische-Funktionen":
            Trigonomisch = Tk()
            Trigonomisch.title("Trigonometrische-Funktionen")
            Trigonomisch.geometry("800x600")
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
        Anmeldung_fenster.deiconify()

    logout = Button(Mainwindow, text="Abmelden", command=logout)
    logout.pack()
    logout.place(relx=0.9, rely=0.0)
    drop.pack()
    drop.place(relx=0.0, rely=0.0)


def register():
    Register = Tk()
    Register.title("Registration")

    def registrierungs_input():
        RgstinpBenutzername = RgstBenutzereingabe.get()
        RgstinpPasswort = RgstPassworteingabe.get()
        RgstinpPasswortConfirm = RgstConfirmeingabe.get()

        if RgstinpPasswort == RgstinpPasswortConfirm and RgstinpBenutzername != "":
            if eingaben_ueberpruefen(RgstinpBenutzername):
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

    RgstButton = Button(Register, text="Registrieren", command=registrierungs_input)

    RgstBenutzername.pack()
    RgstBenutzereingabe.pack()
    RgstPasswort.pack()
    RgstPassworteingabe.pack()
    RgstConfirm.pack()
    RgstConfirmeingabe.pack()
    RgstButton.pack()


Rgstlabel = Label(Anmeldung_fenster, text="Wenn Sie noch keinen Account besitzen Drücken sie bitte hier:")
Rgstbutton = Button(Anmeldung_fenster, text="Registration", command=register)
Benutzernamelabel = Label(Anmeldung_fenster, text="Benutzername")
Anmeldungsbutton = Button(Anmeldung_fenster, text="Anmelden", command=inpAnmeldung)
Benutzernameeingabe = Entry(Anmeldung_fenster, bd=5, width=40)
Passwortlabel = Label(Anmeldung_fenster, text="Passwort")
Passworteingabe = Entry(Anmeldung_fenster, bd=5, width=40)

Benutzernamelabel.pack()
Benutzernameeingabe.pack()
Passwortlabel.pack()
Passworteingabe.pack()
Anmeldungsbutton.pack()
Rgstlabel.pack()
Rgstlabel.place(relx=0.1, rely=0.8)
Rgstbutton.place(relx=0.4, rely=0.9)
Anmeldung_fenster.mainloop()

