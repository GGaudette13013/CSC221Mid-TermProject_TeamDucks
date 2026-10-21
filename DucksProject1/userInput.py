'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userInput.py
Description:  
'''
from DucksProject1 import welcome_introduction

#  GET THE NUMBER OF DAYS IN WHICH THE USER CYCLES TASKS ANS FEEDS THE HIVE
def getUserDays():
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet1()

    userDays = int(input("                                  "))
    while userDays < 7 or userDays > 28:
        print("  o o                                                                    o o   ")
        print(" o   o          The number of days must be between 7 and 28.            o   o  ")
        print("  o o              E N T E R     D A Y S      B E L O W                  o o   ")
        
        userDays = int(input("                          "))

    return userDays



# GETS USER STARTER POPULATION
def getUserBeehiveStarterPopulation(days):
    welcome_introduction.display_instructions_userInput_DaysPopulationDispSet2(days)

    userPopulation = int(input("                                              "))

    while userPopulation < 1000 or userPopulation > 100000:
        print("  o o     The population is not in the range of permitted population.    o o   ")
        print(" o   o   Choose population ( average is between 20,000 and 80,000 )     o   o  ")
        print("  o o        E N T E R     P O P U L A T I O N      B E L O W            o o   ")
        
        userPopulation = int(input("                                      "))

    return userPopulation




