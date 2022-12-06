def checkOffHabit():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        connection = sqliteConnection.cursor()
        records = connection.fetchall()
        lenrecords = len(records)

        td = datetime.today().date() # td = today
        timedlt = timedelta(days=-1)
        yesterd = td + timedlt
        tmorrow = td + timedelta(days=1)

        while True:
            inputID = input("Type in the ID of the Habit that you want to mark as done: ")
            try:
                inpID = int(inputID)
            except ValueError:
                print("It´s not the correct ID. Please, type in an ID from the list.")
            else:
                break

        # Add Streak+1
        connection.execute(
            "UPDATE habit_db SET Streak = Streak+? WHERE Start_Date <=? AND Id = ? AND Due_Date > ?",
            (1, td, inpID, yesterd))


        action = (f"""UPDATE habit_db SET (Max_Streak) = (Streak) WHERE (Max_Streak)<(Streak) AND Id = {inpID};""")
        connection.execute(action)
        sqliteConnection.commit()

        # replacing the old due date with a new due date
        connection.execute("UPDATE habit_db SET (Start_Date)=(Due_Date) WHERE Id = ? AND Start_Date<? AND Due_Date > ?",
                     (inpID, tmorrow, yesterd))

        newStartingDate = datetime.today().date()

        # daily period habits -> updating due date (day)
        timeDay = timedelta(days=1)
        newDueDay = newStartingDate + timeDay
        connection.execute(
            'UPDATE habit_db SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Daily" AND Id = ? AND Due_Date > ?',
            (newDueDay, inpID, yesterd))

        # weekly period habits -> updating due date (week)
        timeWeek = timedelta(days=7)
        newDueWeek = newStartingDate + timeWeek
        connection.execute(
            'UPDATE habit_db SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Weekly" AND Id = ? AND Due_Date > ?',
            (newDueWeek, inpID, yesterd))

        sqliteConnection.commit()

    finally:
        if sqliteConnection:
            sqliteConnection.close()