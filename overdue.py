def Overdue():
    import sqlite3
    from datetime import datetime, timedelta

    sqliteConnection = sqlite3.connect("habit_db.sqlite3") # create connection to the database
    connection = sqliteConnection.cursor()

    timed = timedelta(days=-1) # timed = timedelta
    yesterd = datetime.today().date() + timed #yesterd = yesterday

    newStartingDate = datetime.today().date()

    timeDay = timedelta(days=1)
    newDueDay = newStartingDate + timeDay

    timeWeek = timedelta(days=7)
    newduedateweek = newStartingDate + timeWeek
    newBreak = 1

    # add Break if it´s overdue
    connection.execute('UPDATE habit_db SET Break = Break+? WHERE Break=(Break) AND Due_Date <= ?', (newBreak, yesterd))

    # Reset Streak to zero if user fails to check off habit in the given period
    connection.execute('UPDATE habit_db SET Streak=? WHERE Streak=(Streak) AND Due_Date <= ?', (0, yesterd))

    # replacing starting date with today´s date
    connection.execute('UPDATE habit_db SET Start_Date=? WHERE Start_Date=(Start_Date) AND Due_Date <= ?',  (newStartingDate, yesterd))

    # replacing daily period´s due date with new date today
    connection.execute('UPDATE habit_db SET Due_Date=? WHERE Due_Date=(Due_Date) AND Period=("Daily") AND Due_Date <= ?',
                 (newDueDay, yesterd))
    # Replacing weekly period´s due date with new date for the week
    connection.execute('UPDATE habit_db SET Due_Date=? WHERE Streak=(Streak) AND Period=("Weekly") AND Due_Date <= ?',(newduedateweek, yesterd))

    sqliteConnection.commit()
