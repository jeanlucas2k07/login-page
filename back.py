from tkinter import messagebox
import sqlite3 as sq
import os

class DataBase():
    def __init__(self, db_directory="database", db_name="data.db"):
        self.db_directory = db_directory
        self.db_name = db_name
        self.db_path = os.path.join(self.db_directory, self.db_name)
        os.makedirs(self.db_directory, exist_ok=True)
        print(f"Database will be created/in: {self.db_path}")

    def con_db(self):
        try:
            conn = sq.connect(self.db_path)
            print(f"Connection successful: {self.db_path}")
            return conn
        except sq.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def CreateDataBase(self):
        conn = self.con_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS data (
                        email TEXT NOT NULL, 
                        password TEXT NOT NULL
                    )
                ''')
                conn.commit()
                print('The table was created successfully')
            except sq.Error as e:
                print(f"Error creating table: {e}")
            finally:
                conn.close()

    def Cad(self, email, password):
        conn = self.con_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO data (email, password) VALUES (?, ?)", (email, password))
                conn.commit()
                messagebox.showinfo(title='register', message=f'Record entered: {email}, {password}')
            except sq.Error as e:
                messagebox.showerror('ERROR!', f"Error when entering data: {e}")
            finally:
                conn.close()