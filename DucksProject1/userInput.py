'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userInput.py
Description:  
'''
#  GET THE NUMBER OF DAYS IN WHICH THE USER CYCLES TASKS ANS FEEDS THE HIVE
def getUserDays():
    print("The time to prepare is nigh!! You must choose a time frame to prepare.")
    userDays = int(input("How many days do you have to prepare before winter hits?"))
    while userDays < 7 or userDays > 28:
        print("The time frame must be between a week and a month span.")
        userDays = int(input("How many days do you have to prepare before winter hits?"))
        
    return userDays
