'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userInput.py
Description:  
'''
from DucksProject1 import welcome_introduction

#  GET THE NUMBER OF DAYS IN WHICH THE USER CYCLES TASKS ANS FEEDS THE HIVE
def getUserDays():
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet1()

    userDays = input("Enter number of days (7-28): ")

    while not userDays.isdigit() or int(userDays) < 7 or int(userDays) > 28:
        print("The number of days must be between 7 and 28.")
        userDays = input("Enter number of days (7-28): ")

    return int(userDays)



# GETS USER STARTER POPULATION
def getUserBeehiveStarterPopulation(days):
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet2(days)

    userPopulation = input("Enter starting bee population (1000-100000): ")

    while not userPopulation.isdigit() or int(userPopulation) < 1000 or int(userPopulation) > 100000:
        print("Population must be between 1000 and 100000.")
        userPopulation = input("Enter starting bee population (1000-100000): ")

    return int(userPopulation)