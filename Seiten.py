import math
from tkinter import *

import numpy

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

                ax = plt.gca()  # krodinaten systeme
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                X = np.linspace(vonl,bisl, 100)
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
            Quadratisch.title("Quadratische-Funktion Ableitung1 =")
            Quadratisch.geometry("400x400")
            Quadratisch.geometry("800x600")
            Quadratisch.resizable(width=0, height=0)

            def RechnungQuadr():

                plt.title("Quadratischen-Funktion")
                plt.ylabel(Eingabe6.get())
                plt.xlabel(Eingabe7.get())
                a = Eingabe1.get()
                b = Eingabe2.get()
                c = Eingabe3.get()
                von = Eingabe4.get()
                bis = Eingabe5.get()
                aa = float(a)
                bb = float(b)
                cc = float(c)
                vonv = float(von)
                bisb = float(bis)

                ax = plt.gca()  # koordinatensystem
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(vonv, bisb, 100)
                y = aa * x ** 2 + bb * x + cc
                bbb = bb / aa  # Normalisierung
                aaa = aa / aa
                ccc = cc / aa

                Ergebnis1PQ = -bbb / 2
                Ergebnis2PQ = (bbb / 2) ** 2 - ccc
                pq1 = Ergebnis1PQ + math.sqrt(Ergebnis2PQ)
                pq2 = Ergebnis1PQ - math.sqrt(Ergebnis2PQ)

                PunktX = -bb / (2 * aa)   # Berechnung des Scheitelpunktes /Gleicung der Parabel
                PunktY = aa * PunktX ** 2 + bb * PunktX + cc  # Berechenet die Kordinaten des Scheitelpunktes

                xxx = [pq1, pq2]  # Nullstellen
                yyy = [0, 0]

                plt.scatter(xxx, yyy, color="red")
                plt.scatter( x=PunktX,y=PunktY, color="blue")
                plt.plot(x, y, '-r', label='y=')
                plt.grid()
                plt.show()

            def matplotbeispiel():

                ax = plt.gca()  # koordinatensystem
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(-5, 5, 100)
                a = 7
                b = 3
                c = -3

                y = (a * x ** 2) + (b * x) + c
                bbe = b / a  # Normalisierung
                aab = a / a
                ccb = c / a

                Punktx = -b / (2 * a)  # Berechnung des Scheitelpunktes /Gleicung der Parabel
                Punikty = a * Punktx ** 2 + b * Punktx + c  # Berechenet die Kordinaten des Scheitelpunktes

                pb1 = -bbe / 2 + math.sqrt((bbe / 2) ** 2 - (ccb))
                pb2 = -bbe / 2 - math.sqrt((bbe / 2) ** 2 - (ccb))
                xxb = [pb1, pb2]
                yyb = [0, 0]

                plt.scatter(xxb, yyb, color="red")
                plt.scatter(Punktx,Punikty, color="blue")
                plt.plot(x, y, '-r', label='y=')
                plt.title('Der Graph von y=4x+2')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid()
                plt.show()

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
                bisg = float(bisg)
                vong = float(vong)
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


                ax = plt.gca()  # krodinaten systeme
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x_Poly = np.linspace(vong,bisg,500) # erstellt ein array mit 100 glechmäsig verteielten x werten zwischen von und  bis

                if ng_ausgabe == 3:
                        y_poly = (ag_ausgabe * x_Poly ** 3) + (var2_ausgabe * x_Poly ** 2) + (var3_ausgabe * x_Poly ** 1) \
                            + (var4_Ausgabe * x_Poly ** 0)
                elif ng_ausgabe == 4:
                        y_poly  = (ag_ausgabe * x_Poly ** 4) + (var2_ausgabe * x_Poly ** 3) + (var3_ausgabe * x_Poly ** 2) \
                            (+ var4_Ausgabe * x_Poly ** 1) + (var5_Ausgabe * x_Poly ** 0)
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

                plt.plot(x_Poly,y_poly)  # stelt alles in matplot_lib dar
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

            def Rechnungtri():

                plt.title("Trigonometrische-Funktionen")
                plt.ylabel(TriEntry6.get())
                plt.xlabel(TriEntry7.get())
                at = TriEntry1.get()
                bt = TriEntry2.get()
                ct = TriEntry3.get()
                vont = TriEntry4.get()
                bist = TriEntry5.get()
                aat = float(at)
                bbt = float(bt)
                cct = float(ct)
                vvt = float(vont)
                bbit = float(bist)
                imtct = int(cct)
                imtbbt = int(bbt)


                k = 2

                ax = plt.gca()  # koordinatensystem
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(vvt, bbit, 1000)
                ysin = aat * np.sin(bbt * x + cct)
                ycos = aat * np.cos(bbt * x + cct)
                # ytan = aat * np.tan(bbt * x + cct)
                nullstelle_Sin = k * math.pi + imtct
                nullstelle_cos = imtbbt * ( k * math.pi + math.pi/2 + imtct)
                nullstelleny = 0



                plt.plot(x, ycos, color="blue")
                plt.plot(x, ysin, color="green")
                # plt.plot(x, ytan, color="purple")
                plt.scatter(x = nullstelle_Sin, y= nullstelleny , color= "green")
                plt.scatter(x = nullstelle_cos, y= nullstelleny , color= "blue")
                plt.grid()
                plt.show()

            def Beispieltri():

                plt.title('Der Graph von f(x) = 2 * sin(2x + 2) und f(x) = 2 * cos(2x + 2) ')
                ax = plt.gca()  # koordinatensystem
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(-10, 10, 100)
                sinn = 2 * np.sin(2 * x + 2)
                coss = 2 * np.cos(2 * x + 2)


                plt.plot(x, sinn, color="blue")
                plt.plot(x, coss, color="green")
                plt.grid()
                plt.show()

            TriLabel1 = Label(Trigonomisch, text="a")
            TriLabel1.pack()
            TriLabel1.place(x=7, y=25)

            TriEntry1 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry1.pack()
            TriEntry1.place(x=7, y=50)

            TriLabel2 = Label(Trigonomisch, text="b")
            TriLabel2.pack()
            TriLabel2.place(x=7, y=75)

            TriEntry2 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry2.pack()
            TriEntry2.place(x=7, y=100)

            TriLabel3 = Label(Trigonomisch, text="c")
            TriLabel3.pack()
            TriLabel3.place(x=7, y=125)

            TriEntry3 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry3.pack()
            TriEntry3.place(x=7, y=150)

            TriLabel4 = Label(Trigonomisch, text="von")
            TriLabel4.pack()
            TriLabel4.place(x=7, y=175)

            TriEntry4 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry4.pack()
            TriEntry4.place(x=7, y=200)

            TriLabel5 = Label(Trigonomisch, text="bis")
            TriLabel5.pack()
            TriLabel5.place(x=7, y=225)

            TriEntry5 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry5.pack()
            TriEntry5.place(x=7, y=250)

            TriLabel6 = Label(Trigonomisch, text="Y-Name")
            TriLabel6.pack()
            TriLabel6.place(x=7, y=275)

            TriEntry6 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry6.pack()
            TriEntry6.place(x=7, y=300)

            TriLabel7 = Label(Trigonomisch, text="X-Name")
            TriLabel7.pack()
            TriLabel7.place(x=7, y=325)

            TriEntry7 = Entry(Trigonomisch, bd=5, width=12)
            TriEntry7.pack()
            TriEntry7.place(x=7, y=350)

            Buttontri2 = Button(Trigonomisch, text="Beispiel", command=Beispieltri)
            Buttontri2.pack()
            Buttontri2.place(x=7, y=450)

            Buttontri1 = Button(Trigonomisch, text="Ausführen", command=Rechnungtri)
            Buttontri1.pack()
            Buttontri1.place(x=7, y=500)


        elif Auswahl == "Exponential-Funktionen":
            Exponential = Tk()
            Exponential.title("Exponential-Funktionen")
            Exponential.geometry("800x600")
            Exponential.resizable(width=0, height=0)

            bise = Entry(Exponential, bd=5, width=12)  # wie weit y geht (bis) start = 0 (textboxen)
            lab1 = Label(Exponential, text="bis")
            lab1.pack()
            lab1.place(x=7, y=435)
            bise.pack()
            bise.place(x=7, y=460)

            vone = Entry(Exponential, bd=5, width=12)  # wie weit x geht (textboxen)
            lab2 = Label(Exponential, text="von")
            lab2.pack()
            lab2.place(x=7, y=375)
            vone.pack()
            vone.place(x=7, y=400)

            Y_achse = Entry(Exponential, bd=5, width=12)  # yachsenabschnitt (textboxen)
            lab3 = Label(Exponential, text="Y-Achsenabschnit")
            lab3.pack()
            lab3.place(x=7, y=205)
            Y_achse.pack()
            Y_achse.place(x=7, y=230)

            m_steigung = Entry(Exponential, bd=5, width=12)  # steigung (textboxen)
            lab4 = Label(Exponential, text="Steigung")
            lab4.pack()
            lab4.place(x=7, y=255)
            m_steigung.pack()
            m_steigung.place(x=7, y=280)

            ctexte = Entry(Exponential, bd=5, width=12)  # steigung (textboxen)
            lab4 = Label(Exponential, text="c")
            lab4.pack()
            lab4.place(x=7, y=315)
            ctexte.pack()
            ctexte.place(x=7, y=340)

            x_name = Entry(Exponential, bd=5, width=12)  # name für xseite (textboxen)
            lab5 = Label(Exponential, text="Name-X")
            lab5.pack()
            lab5.place(x=7, y=85)
            x_name.pack()
            x_name.place(x=7, y=110)

            y_Name = Entry(Exponential, bd=5, width=12)  # name für yseite (textboxen)
            lab6 = Label(Exponential, text="Name-Y")
            lab6.pack()
            lab6.place(x=7, y=145)
            y_Name.pack()
            y_Name.place(x=7, y=170)

            def RechnenExpo():  # Formel für Exponential-Funktion
                plt.title("Exponential-Funktion")
                plt.ylabel(y_Name.get())
                plt.xlabel(x_name.get())
                vonx = vone.get()
                bisx = bise.get()
                ctext = ctexte.get()
                Steigung_m = m_steigung.get()
                Achse_Y = Y_achse.get()
                vonx = float(vonx)
                bisx = float(bisx)
                ctext = float(ctext)
                Steigung_m = float(Steigung_m)
                Achse_Y = float(Achse_Y)

                ax = plt.gca()  # krodinaten systeme
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                X = np.linspace(vonx, bisx, 100)
                Y = Steigung_m * (Achse_Y ** X) + ctext



                plt.grid()
                plt.plot(X, Y)
                plt.show()

            def Beispiel_Exponential():

                ax = plt.gca()  # krodinaten systeme
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                def BeispielEX(x):
                    return np.exp(x)
                wert_x = np.linspace(-5,5,100)
                plt.plot(wert_x, BeispielEX(wert_x))
                plt.title("Exponential Funktion")
                plt.grid()
                plt.show()

            buttonEx = Button(Exponential,text="Ausführen", command=RechnenExpo)
            buttonEx.pack()
            buttonEx.place(x=7,y=40)

            buttonBPE = Button(Exponential,text="Beispiel", command=Beispiel_Exponential)
            buttonBPE.pack()
            buttonBPE.place(x=7, y=555)

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

