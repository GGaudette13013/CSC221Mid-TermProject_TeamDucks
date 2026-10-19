'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userInput.py
Description:  
'''
from DucksProject1 import welcome_introduction

#  GET THE NUMBER OF DAYS IN WHICH THE USER CYCLES TASKS ANS FEEDS THE HIVE
def getUserDays():
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet1()

    userDays = int(input("Enter number of days (7-28): "))
    while userDays < 7 or userDays > 28:
        print("The number of days must be between 7 and 28.")
        userDays = int(input("Enter number of days (7-28): "))

    return userDays



# GETS USER STARTER POPULATION
def getUserBeehiveStarterPopulation(days):
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet2(days)

    userPopulation = int(input("Enter starting bee population (1000-100000): "))

    while userPopulation < 1000 or userPopulation > 100000:
        print("Population must be between 1000 and 100000.")
        userPopulation = int(input("Enter starting bee population (1000-100000): "))

    return userPopulation