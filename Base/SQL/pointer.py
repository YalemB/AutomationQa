import mysql.connector


class DB:
    def __init__(self, db):
        self.db = db
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yalem1994",
            port="3306",
            database=self.db
        )


    def ser(self,qury):
        connaction = self.mydb.cursor()
        connaction.execute(qury)
        return connaction.fetchall()

    def up(self,qury):
        updat = self.mydb.cursor()
        updat.execute(qury)
        return self.mydb.commit()




















