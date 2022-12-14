class Habits():

    def __init__(self):
        print("Welcome to your Habit Tracker!")

def main_page():

    myHabits = Habits()

    # creating an empty table
    import predefined
    predefined.TableCreate()


    # 1. Option: start with 5 predefined habits in the list or with an empty list
    NewOrPredef = True
    while NewOrPredef == True:
        predefHabits = input("\nDo you want to use predefined habits? Yes/No :  ")
        #creating 5 predefined habits
        if predefHabits == 'Yes':
            import predefined
            predefined.predefinedhabits()
            print("Now 5 different predefined habits are part of your tasks that you need to check off regularly. Go to Analyze habits to have a look at them!")
            NewOrPredef = False
        #start without predefined habits in the list
        elif predefHabits == 'No':
            break
        else:
            print("\nYour input is invalid")
            NewOrPredef = True




    #Menu with 5 different choices for the user
    choice = ""
    while choice.lower() != "x":

        print("\nEnter 1 to define a new habit")
        print("_________________________________")
        print("Enter 2 to check off a habit ")
        print("_________________________________")
        print("Enter 3 to delete a habit")
        print("_________________________________")
        print("Enter 4 to analyse your habits")
        print("_________________________________")
        print("Enter x to exit the program")


        choice = input("\nChoose a number to proceed:  ")

        # reset if the user fails to check off his habit
        import overdue
        overdue.Overdue()


        # first Option: creating new habits
        if choice == "1":
            import habits
            habits.newHabits()


        # second Option: check off a habit
        elif choice == "2":
            import analyze
            analyze.ReturnAllHabits() # returning all habits for user to choose which one to check
            # checking off task by user
            import checkoff
            checkoff.checkOffHabit()
            print("Your chosen habit has been marked as done")


        # third Option: deleting habits
        elif choice == "3":
            deleteOrExit = ""
            while deleteOrExit != "exit":
                deleteOrExit = input("\nPlease, type in 1 to delete a habit or [exit] to go back to the main menu: ")
                if deleteOrExit == "1":
                    import analyze
                    analyze.ReturnAllHabits() # all the habits are displayed
                    import delete
                    delete.deletehabits() # user can choose a habit and delete it


        # forth Option: analyzing habits
        elif choice == "4":
            AnalyzeMenu = ""
            while AnalyzeMenu != "exit":

                print("\nType in 1 to return all habits")
                print("_____________________________________________________________")
                print("Type in 2 to return all daily habits")
                print("_____________________________________________________________")
                print("Type in 3 to return all weekly habits")
                print("_____________________________________________________________")
                print("Type in 4 to return longest run streak of all defined habits")
                print("_____________________________________________________________")
                print("Type in 5 to return longest run streak for a given habit")
                print("_____________________________________________________________")
                print("Type in [exit] to go to the main menu")
                print("_____________________________________________________________")

                AnalyzeMenu = input("\nPlease, type in your choice: ")

                # first analyze option: returning all habits
                if AnalyzeMenu == "1":
                    import analyze
                    analyze.ReturnAllHabits()

                # second analyze option: returning all daily habits
                elif AnalyzeMenu == "2":
                    import analyze
                    analyze.ReturnDailyHabits()

                # third analyze option: returning all weekly habits
                elif AnalyzeMenu == "3":
                    import analyze
                    analyze.ReturnWeeklyHabits()

                # forth analyze option: returning longest run streak of all habits
                elif AnalyzeMenu == "4":
                    import analyze
                    analyze.LongStreakHabits()

                # fifth analyze option: returning longest run streak for a given habit
                elif AnalyzeMenu == "5":
                    import analyze
                    analyze.LongStreakGiven()

                # sixth option: go to the main menu
                elif AnalyzeMenu == "exit":
                    print("You are going to the main menu")


        elif str(choice.lower()) == "x":
            print("\nBye!\n")
            print("_____________")

        else:
            print("\nYour choice is not one of the given options\n")

main_page()
