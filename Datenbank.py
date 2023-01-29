import sqlite3
import os
#from Seiten import register



def createdb():
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()

    Tabelle = f"""CREATE TABLE anmeldung(
                benutzername TEXT,
                passwort TEXT
            );"""
    cursor.execute(Tabelle)
    connection.commit()

    Benutzer = "admin"
    Passwort = "admin"
    insert = f"INSERT INTO anmeldung VALUES('{Benutzer}', '{Passwort}');"
    cursor.execute(insert)
    connection.commit()
    connection.close()

def NewAcc(name, passwort):
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()
    InsertNewAcc = f"INSERT INTO anmeldung VALUES('{name}', '{passwort}');"
    cursor.execute(InsertNewAcc)
    connection.commit()
    connection.close()

def Prüfanm(name, passwort):
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()
    statement = f"""SELECT benutzername
                    FROM anmeldung
                    WHERE benutzername ='{name}' AND passwort= '{passwort}'"""
    cursor.execute(statement)
    k = cursor.fetchone()
    if not k:
        print("Login Failed")
    else:
        print("Login Successful")
def PrüfungRgst(Benutzer):
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()

    sql = f"""SELECT benutzername 
          FROM anmeldung 
          WHERE benutzername = '{Benutzer}';"""

    PrüfRgst = cursor.execute(sql).fetchall()
    if PrüfRgst == "NULL":
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
