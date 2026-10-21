'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userInput.py
Description:  
'''
from DucksProject1 import welcome_introduction

#  GET THE NUMBER OF DAYS IN WHICH THE USER CYCLES TASKS ANS FEEDS THE HIVE
def getUserDays():
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet1()

    userDays = int(input("Enter number of days (7-28):               "))
    while userDays < 7 or userDays > 28:
        print("  o o                                                                    o o   ")
        print(" o   o          The number of days must be between 7 and 28.            o   o  ")
        print("  o o              E N T E R     D A Y S      B E L O W                  o o   ")
        
        userDays = int(input("Enter number of days (7-28): "))

    return userDays



# GETS USER STARTER POPULATION
def getUserBeehiveStarterPopulation(days):
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet2(days)

    userPopulation = int(input("Enter starting bee population (1000-100000):               "))

    while userPopulation < 1000 or userPopulation > 100000:
        print("  o o     The population is not in the range of permitted population.    o o   ")
        print(" o   o   Choose population ( average is between 20,000 and 80,000 )     o   o  ")
        print("  o o        E N T E R     P O P U L A T I O N      B E L O W            o o   ")
        
        userPopulation = int(input("Enter starting bee population (1000-100000):               "))

    return userPopulation

# Gets the number of bees sent foraging
def getUserForagingBees(totalPopulation):

    foragingBees = int(input("How many bees would you like to send foraging? "))

    while foragingBees < 0 or foragingBees > totalPopulation:
        print("Invalid number of bees.")
        print("You have", totalPopulation, "bees available.")

        foragingBees = int(input("Enter number of bees to forage: "))

    return foragingBees


