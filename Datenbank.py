import sqlite3, os

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
    print("test")


if os.path.exists("Datenbank.db"):
    print("Datenbank existiert bereits")
else:
    createdb()


