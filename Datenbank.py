import sqlite3
import os



def createdb(): #Erstellung der Datenbank
    connection = sqlite3.connect("Datenbank.db") #connection zu sqlite3 und Datenbank.db Datei wird erstellt
    cursor = connection.cursor() #connection wird mit cursor verbunden

    #Datenbank anmeldung wird erstellt mit spalten benutzername und passwort
    Tabelle = f"""CREATE TABLE anmeldung(
                benutzername TEXT,
                passwort TEXT
            );"""
    cursor.execute(Tabelle) #Erstellung wird ausgeführt
    connection.commit() #und committed

    Benutzer = "admin" #in Variable Benutzer wird admin reingelegt
    Passwort = "admin" #in Variable Passwort wird admin reingelegt
    insert = f"INSERT INTO anmeldung VALUES('{Benutzer}', '{Passwort}');" #Variablen Benutzername und Passwort wird in Datenbank anmeldung in Spalten Benutzername und Passwort gelegt
    cursor.execute(insert) #Das reinlegen wird ausgeführt
    connection.commit() #und committed
    connection.close() #connection wird geschlossen

def NewAcc(name, passwort): #funktion wird angelegt mit variablen name und passwort
    connection = sqlite3.connect("Datenbank.db") #connection zu sqlite3 und Datenbank.db Datei wird erstellt
    cursor = connection.cursor()#connection wird mit cursor verbunden
    InsertNewAcc = f"INSERT INTO anmeldung VALUES('{name}', '{passwort}');" #Der Inhalt der Variablen name und passwort wird in die datenbank anmeldung gelegt
    cursor.execute(InsertNewAcc) #Das reinlegen wird ausgeführt
    connection.commit() #und committed
    connection.close()#connection wird geschlossen

def Prüfanm(name, passwort):
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()
    #Abfrage in der Spalte benutzername von der Tabelle anmeldung wo benutzername ist inhalt von variable name und passwort inhalt von variable passwort (eingabe in textfeld von Seiten,oy)
    statement = f"""SELECT benutzername
                    FROM anmeldung
                    WHERE benutzername ='{name}' AND passwort= '{passwort}'"""
    cursor.execute(statement) #wird ausgeführt
    k = cursor.fetchone() #In die Variable k wird hineingepackt ob einer der Abfrage gerecht wurde
    #Wenn nicht gerecht wurde mache False wenn gerecht wurde mache True
    if not k:
        return False
    else:
        return True
def PrüfungRgst(Benutzer):
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()
    #sql abfrage in spalte benutzername, tabelle anmeldung, wo benutzername der inhalt von Benutzer ist
    sql = f"""SELECT benutzername 
          FROM anmeldung 
          WHERE benutzername = '{Benutzer}';"""
    #in PrüfRgst wird die Abfrage ausgeführt und guckt ob 1 Ergebnis gebracht wurde und wenn er gebracht wurde ist False und wenn keiner gebracht wurde ist true
    PrüfRgst = cursor.execute(sql).fetchone()
    if PrüfRgst:
        return False
    else:
        return True

def Ausgabe():
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()

    sql = "SELECT * FROM anmeldung"
    ausgabe = cursor.execute(sql).fetchall()
    print(ausgabe)
    connection.commit()
    connection.close()

if os.path.exists("Datenbank.db"):
    print("Datenbank existiert bereits")
else:
    createdb()
