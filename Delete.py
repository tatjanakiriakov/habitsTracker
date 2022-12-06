def deletehabits():
    try:
        import sqlite3
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        while True:
            inputDelete = input("\nDELETE Habit's ID number : ") # input lets user choose the ID of the habit that they want to remove from the list
            try:
                inpDelete = int(inputDelete) # converting the user´s input into an integer
            except ValueError:
                print("It's not a valid Id.")
            else:
                break

        # deleting by user chosen ID
        command = (f'''DELETE FROM habit_db WHERE Id = {inpDelete} AND Id IS NOT NULL;''')
        conn.execute(command)

        command = (f'''UPDATE habit_db SET ('Id') = (Id)-1  WHERE Id > {inpDelete} ;''') # sorting IDs after the chose one was removed
        conn.execute(command)
        sqliteConnection.commit()
        conn.close()

        print("Habit was successfully removed from the list!")

    except sqlite3.Error as error:
        print("Failed to read data", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
