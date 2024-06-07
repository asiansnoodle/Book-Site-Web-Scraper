import sqlite3
import pandas as pd

def createDatabase():
    connection = sqlite3.connect("books.db")   # create the database books.db
    cur = connection.cursor()  # create a cursor so we can interact with the database
    # execute sql command to create table 
    cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, price REAL NOT NULL)')
    connection.commit() # save changes to table 
    connection.close()  # close connection

def insertToDataBase(df):
    connection = sqlite3.connect("books.db")    # connect to database
    # write the dataframe to sql table
    df.to_sql("books", connection, if_exists='append', index=False)
    connection.close()  # close connection to db

if __name__ == "__main__":
    df = pd.read_csv('books.csv')
    
    createDatabase()
    insertToDataBase(df)

    print("Data successfully scraped and stored in 'books.db' database.")