import sqlite3
import os
#from Seiten import register



def createdb():
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()

    Tabelle = """CREATE TABLE anmeldung("benutzername TEXT","passwort TEXT");"""
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




