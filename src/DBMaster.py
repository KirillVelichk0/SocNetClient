import sqlite3
import pathlib
from pathlib import Path
class DatabaseMaster:
    def __init__(self):
        base_dir = Path(__file__).parent.parent.resolve()
        self.__cur_path = base_dir.joinpath('lite', 'db')
        connection = sqlite3.connect(self.__cur_path)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS TokenStore
          (id INTEGER PRIMARY KEY, jwt TEXT)''')
        cursor.close()
        connection.close()
        #Потом добавятся еще методы

    def __GetConnection(self):
        connection = sqlite3.connect(self.__cur_path)
        return connection

    def GetJWT(self):
        with self.__GetConnection() as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM TokenStore
            WHERER id = 0''')
            result = cursor.fetchone()
            cursor.close()
            if result is None:
                return None
            return {"id": result[0], "jwt": result[1]}
        
    def UpdateJWT(self, jwt):
        with self.__GetConnection() as connection:
            cursor = connection.cursor()
            row = self.GetJWT()
            if row is None:
                new_row = (0, jwt)
                cursor.execute(''' INSERT into TokenStore (id, jwt) 
                 VALUES (?, ?) ''', new_row)
            else:
                cursor.execute(''' UPDATE TokenStore
                 SET jwt = ? WHERE id = 0''', jwt)
            cursor.close()

    def DeleteJWT(self):
        with self.__GetConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM TokenStore where id = 0")
            cursor.close()



master = DatabaseMaster()