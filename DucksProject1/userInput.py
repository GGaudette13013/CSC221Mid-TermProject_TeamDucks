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



# GETS USER STARTER POPULATION
def getUserBeehiveStarterPopulation(days):
    
    
    
    print("The hive has only", days, "left before the snow starts falling.")
    print("You must decide what the beehive starter population is before we start preparing. ")
    
    userPopulation = int(input("What is the beehive population (i.e. 50000)? "))
    
    while userPopulation < 1000 or userPopulation > 100000:
        print("The population is not in the range of permitted population. Choose another population")
        print("The average population is 20,000 to 80,000 bees. ")
        userPopulation = int(input("What is the beehive population (i.e. 50000)? "))
        
    return userPopulation

