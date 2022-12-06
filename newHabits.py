def newHabits():
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        lenrecords = len(records)

        Action = True
        while Action:
            newOrExit = input("\nDo you want to create a new habit? Yes/No: ") # needed to give user the chance to go back to the main menu

            if newOrExit == "Yes":
                userTitle = input("\nWhat is the name of your new habit?: ")
                print(userTitle)

                created = datetime.today().date() # gives the date when the habit was created
                print(f"This habit was created on: : {created}")

                lenrecords = lenrecords + 1

                userPeriod = input("\nShould the period be daily or weekly? daily/weekly : ")

                # Setting the period to Daily
                periodChoice = True
                while periodChoice:
                    if userPeriod == "daily":
                        inp_Period = "Daily"
                        print(f"Period: {userPeriod}")
                        due = created + timedelta(days=1)
                        print(f"Due Date: {due}")
                        periodChoice = False


                    # Setting the period to Weekly
                    elif userPeriod == "weekly":
                        userPeriod = "Weekly"
                        print(f"Habit Period : {userPeriod}")

                        due = created + timedelta(days=7)
                        print(f"Due Date: {due}")
                        periodChoice = False

                #inserting new data into database
                habits = [
                    (lenrecords, userTitle, userPeriod, created, due, 0, 0, 0)
                ]

                conn.executemany("INSERT OR REPLACE INTO habit_db VALUES(?,?,?,?,?,?,?,?,?)", habits)
                sqliteConnection.commit()

            elif newOrExit == "No":
                conn.close()
                Action = False


    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()