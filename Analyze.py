#return all habits (predefined and defined by the user)
def ReturnAllHabits():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3') # creating connection to database
        connection = sqliteConnection.cursor()

        command = """SELECT * FROM habit_db"""
        connection.execute(command)
        records = connection.fetchall()
        print("The habits are:  ", len(records)) # printing out wanted habits (in this case everything)
        print("\n")
        for row in records:
            print(row)

        sqliteConnection.commit()
        connection.close()

    except sqlite3.Error as error: # error handling in case there is some issues with the database
        print("Data could not be loaded", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close() # closing connection to the database


# return list of habits with the same periodicricity which is weekly
def ReturnWeeklyHabits():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        command = """SELECT * FROM habit_db WHERE Period = 'Weekly'""" # choosing which habits to print (in this case habits where the period is weekly
        conn.execute(command)
        records = conn.fetchall()
        print("The habits are:  ",  len(records))
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Data could not be loaded", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()



# return list of habits with the same periodicricity which is daily
def ReturnDailyHabits():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        command = """SELECT * FROM habit_db WHERE Period = 'Daily'""" # choosing which habits to print (in this case habits where the period is daily
        conn.execute(command)
        records = conn.fetchall()
        print("The habits are:  ", len(records))
        print("\n")
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Data could not be loaded", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


# return the longest streak of all defined habits
def LongStreakHabits():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        command = """SELECT Title, MAX(Max_Streak) FROM habit_db""" # choosing habits where the streak is the most
        conn.execute(command)
        records = conn.fetchall()

        for row in records:
            print(f"The longest run streak among all habits is : {row} ")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


# return the longest streak of all given habits
def LongStreakGiven():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        Action = True
        while Action:
            inputId = input("\nReturn the longest streak of a habit: (type in 1,2,3,...) : ")
            try:
                inpId = int(inputId)

                if inpId in range(lenrecords):
                    Action = False
                else:
                    print("\nyour input is incorrect.")
                    Action = True
            except ValueError:
                print("The ID is not valid.")
            else:
                break

        command = (f'''SELECT Name, MAX(Max_Streak) FROM habit_db WHERE Id = {inpId} ;''') # filtering habit with the id that the user chose
        conn.execute(command)
        records = conn.fetchall()
        for row in records:
            print(f"The longest run streak of given habits is : {row} ") # printing out chosen habits

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
