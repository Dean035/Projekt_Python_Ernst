import sqlite3
import os
from Seiten import register




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

def NewAcc():
    connection = sqlite3.connect("Datenbank.db")
    cursor = connection.cursor()
    register()
    NewBenutzername = register.RgstinpBenutzername
    NewPasswort = register.RgstinpPasswort
    update = f"UPDATE INTO anmeldung VALUES('{NewBenutzername}', '{NewPasswort}');"
    cursor.execute(update)
    connection.commit()
    connection.close()


if os.path.exists("Datenbank.db"):
    print("Datenbank existiert bereits")
else:
    createdb()


