import sqlite3

def printMenu():
    print(f"Please select an option to filter by: ") 
    print(f"1 - Maximum Cost")
    print(f"2 - Price Range")
    print(f"3 - Starts with _")
    print(f"4 - Contains _")
    print(f"Type 'exit' to quit")

def getBooksByPrice(price):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from books where price < ?"""
        cursor.execute(sql_select_query, (price,))
        records = cursor.fetchall()
        print(f"\n{len(records)} Books under {price}:")
        for row in records:
            print(f"{row[1]} | PRICE: {row[2]}")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def getBooksByRange(min, max):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from books where price > ? and price < ?"""
        cursor.execute(sql_select_query, (min, max))
        records = cursor.fetchall()
        print(f"\n{len(records)} Books between {min} - {max}:")
        for row in records:
            print(f"{row[1]} | PRICE: {row[2]}")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def getBooksByFirst_(letter):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from books where title like ?"""
        cursor.execute(sql_select_query, (letter + "%",))
        records = cursor.fetchall()
        print(f"\n{len(records)} Books beginning with '{letter}':")
        for row in records:
            print(f"{row[1]} | PRICE: {row[2]}")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def getBooksByContains(content):
    try:
        sqliteConnection = sqlite3.connect('books.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from books where title like ?"""
        cursor.execute(sql_select_query, ("%" + content + "%",))
        records = cursor.fetchall()
        print(f"\n{len(records)} Books containing '{content}':")
        for row in records:
            print(f"{row[1]} | PRICE: {row[2]}")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

if __name__ == "__main__":

    printMenu()
    while True:
        usrInput = str((input()))
        if usrInput.lower() == 'exit':
            break
            
        elif usrInput == '1':
            price = float(input('Maximum Cost: '))
            getBooksByPrice(price)
            print(f"\n") 
            printMenu()
        elif usrInput == '2':
            min = float(input('Minimum Cost: '))
            max = float(input('Maximum Cost: '))
            getBooksByRange(min, max)
            print(f"\n") 
            printMenu()
        elif usrInput == '3':
            letter = input('Starts with: ')
            getBooksByFirst_(letter)
            print(f"\n") 
            printMenu()
        elif usrInput == '4':
            Content = input('Contains: ')
            getBooksByContains(Content)
            print(f"\n") 
            printMenu()
        else:
            print("\nERROR Invalid option")
            printMenu()

