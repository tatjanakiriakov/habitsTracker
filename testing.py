# a few functionalities will be tested
# 1. returning all habits
# 2. definition of new habits by the user
# 3. analysis: returning longest streak of habits
# 4. checking off a habit as done

import pytest
import time
import datetime
from datetime import timedelta
import sqlite3

# connecting to the database
sqliteConnection = sqlite3.connect('habit_db.sqlite3')
conn = sqliteConnection.cursor()

# 1. testing returning all habits
def return_all_test():
     ReturnAllHabits()
     habits = conn.execute('SELECT * FROM habit_db')
     assert list(habits.fetchall()) == [("Walk 9.000 steps", "Daily", "2022-01-01", "2022-01-02", "2022-01-03", 4, 7, 5),
              ("Do a Workout", "Weekly", "2022-03-20", "2022-03-31", "2022-04-04", 3, 4, 5),
              ("Eat Vegetables", "Daily", "2022-01-01", "2022-01-02", "2022-01-03", 1, 3, 4),
              ("Meet Friends", "Weekly",  "2022-01-01", "2022-01-02", "2022-01-03", 5, 3, 7),
              ("Read a book", "Daily", "2022-05-02", "2022-05-03", "2022-05-04", 4, 7, 3)
              ]


# 2. testing defining new habits
def create_new_test():
    habits = {
        "title": "Dancing",
        "input period": "Weekly"
    }


# 3. testing analysis: returning longest streak of habits
def longest_streak_test():
    LongStreakHabits()
    habits = conn.execute('SELECT Title, MAX(Max_Streak) FROM habit_db')
    assert list(habit_list.fetchall()) == [("Meet Friends", 7)]

