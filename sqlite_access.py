'''
sqlite_access_flabbyPird
@J_Klaus
'''

import sqlite3, sys




class Access():
    def __init__(self, db_name, cursor):
        self.db = db_name
        self.cu = cursor

    def connect(self.db):
        db = sqlite3.connect(self.db)
        cursor = db.cursor()
        return cursor, db


    def Input(table_name, iName, iCounter):
        try:
            connect(db)
            cursor.execute("INSERT into {0} Value {1}, {2}",format(table_name, iName, iCounter))
            db.commit()   
        except: 
            print("Fehler beim INSERT - Datensatz wurde nicht gespeichert !")
            print("Unexpected error:", sys.exc_info()[0])  
        finally:
            db.close()