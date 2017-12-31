from os import path
import sqlite3

class DatabaseIO:

    def __init__(self):
        self.filename = "database/disqusbrownie.db"
        self.db = sqlite3.connect(self.filename)
        self.cursor = self.db.cursor()
        self.initializeDatabase()

    def initializeDatabase(self):
        '''
        Check for existence of the necessary tables, creating them if necessary
        '''
        self.cursor.execute("SELECT name FROM sqlite_master where type='table'")
        if not len(self.cursor.fetchall()):
            self.cursor.execute("CREATE TABLE apiData (filterName TEXT, apiInfo TEXT)")
            self.db.commit()

    def queryDatabase(self, filterName):
        fetchAPIDataCommand = "SELECT * FROM apiData where filterName=?"
        fetchAPIDataValue = (filterName,)
        self.cursor.execute(fetchAPIDataCommand, fetchAPIDataValue)
        content = self.cursor.fetchone()
        if content == () or content = None:
            return None
        else:
            return content[1]        

    def writeToDatabase(self, filterName, apiInfo):
        insertAPIDataCommand = "INSERT INTO apiData VALUES (?, ?)"
        insertAPIDataValue = (filterName, apiInfo)
        self.cursor.execute(insertAPIDataCommand, insertAPIDataValue)
        self.db.commit()
