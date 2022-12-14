def TableCreate():
    try:
        import sqlite3
        sqliteConnection = sqlite3.connect("habit_db.sqlite3")
        connection = sqliteConnection.cursor()

        command = """CREATE TABLE IF NOT EXISTS 'habit_db'(
            "Id" integer NOT NULL,
            "Title" text NOT NULL,
            "Period" text NOT NULL,
            "Born" integer,
            "Start_Date" integer NOT NULL,
            "Due_Date" integer,
            "Streak" integer,
            "Max_Streak" integer,
            "Break" integer,
            PRIMARY KEY("Id" AUTOINCREMENT)
        )"""

        connection.execute(command)

        sqliteConnection.commit()
        connection.close()

    except sqlite3.Error as error:
        print("Failed to read data.", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()


# Insert 5 predefined habits into the database
def predefinedhabits():
    import sqlite3

    sqliteConnection = sqlite3.connect('habit_db.sqlite3')
    conn = sqliteConnection.cursor()

    habits = [("Walk 9.000 steps", "Daily", "2022-01-01", "2022-01-02", "2022-01-03", 4, 7, 5),
              ("Do a Workout", "Weekly", "2022-03-20", "2022-03-31", "2022-04-04", 3, 4, 5),
              ("Eat Vegetables", "Daily", "2022-01-01", "2022-01-02", "2022-01-03", 1, 3, 4),
              ("Meet Friends", "Weekly",  "2022-01-01", "2022-01-02", "2022-01-03", 5, 3, 7),
              ("Read a book", "Daily", "2022-05-02", "2022-05-03", "2022-05-04", 4, 7, 3)
              ]

    conn.executemany(
        "INSERT OR REPLACE INTO habit_db ('Title','Period','Born','Start_Date','Due_Date','Streak','Max_Streak','Break') VALUES (?,?,?,?,?,?,?,?)",
        habits)

    sqliteConnection.commit()


