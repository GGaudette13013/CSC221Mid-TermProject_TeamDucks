'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userTaskExecution.py
Description:  
'''
from DucksProject1 import welcome_introduction
from DucksProject1 import userInput
from DucksProject1 import hivePopulations


def getUserTask():
    
    print("  o o  ")
    print(" o   o ")
    print("  o o   o o  o o  o o  o o  o o  o o  o o")
    print(" o   o     E N T E R         T A S K     o")
    userTask = input(" o o                                ")
    
    return userTask
    
    
    




def getUserTaskValidation(taskChoice):
    
    while taskChoice != "F" and taskChoice != "f" and taskChoice != "C" and taskChoice != "c" and taskChoice != "D" and taskChoice != "d":
        
        print("   o         i n v a l i d     t a s k       ")
        taskChoice = getUserTask()
    
    return taskChoice
    
    
    



def userTaskIdentification(task):
    
    
    
    if task == "F":
        MINFORAGE = 201
        MAXFORAGE = 40001
        population_forage = getUserForagePopulation()
        while population_forage <= MINFORAGE or population_forage >= MAXFORAGE:
            print("   o         i n v a l i d     a m o u n t       ")    
            print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
            print(" o   o                                                                  o   o  ")
            print("  o o                                                                    o o   ")
            population_forage = input("                                    ")        
        
        hivePopulations.foragingPopulation_accumulators(population_forage)
        
        
        
        
        
    elif task == "C":
        MINCREATE = 101
        MAXCREATE = 1851
        population_create = getUserCreateBeesPopulation()
        while population_create <= MINCREATE or population_create >= MAXCREATE:
            print("   o         i n v a l i d     a m o u n t       ")    
            print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
            print(" o   o                                                                  o   o  ")
            print("  o o                                                                    o o   ")
            population_create = input("                                    ")
            
        hivePopulations.createBeesPopulationAddition(population_create)
            
            
    
    else:
        MINDEFENSE = 100
        MAXDEFENSE = 600
        population_defense = getUserDefensePopulation()
        while population_defense <= MINDEFENSE or population_defense >= MAXDEFENSE:
            print("   o         i n v a l i d     a m o u n t       ")    
            print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
            print(" o   o                                                                  o   o  ")
            print("  o o                                                                    o o   ")
            population_defense = input("                                    ")
        hivePopulations.defensePopulation_accumulators(population_defense)



def getUserForagePopulation():
    print("  o o                                                                o o       ")
    print(" o   o                                                              o   o      ")
    print("  o o                                                                 o o      ")
    print("   o o                                                                 o o     ")
    print("  o   o                                                               o   o    ")
    print("   o o                                                                 o o     ")
    print("  o o                                                                   o o    ")
    print(" o   o                                                                 o   o   ")
    print("  o o                                                                   o o    ")
    print("  o o                                                                    o o   ")
    print(" o   o           Enter the number of bees from your population          o   o  ")
    print("  o o      you want to send to go foraging ( the maximum is 40,000 )     o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    
    userInput = input("                                    ")
    
    return userInput
    
    
    
def getUserCreateBeesPopulation():
    print("  o o                                                                o o       ")
    print(" o   o                                                              o   o      ")
    print("  o o                                                                 o o      ")
    print("   o o                                                                 o o     ")
    print("  o   o                                                               o   o    ")
    print("   o o                                                                 o o     ")
    print("  o o                                                                   o o    ")
    print(" o   o                                                                 o   o   ")
    print("  o o                                                                   o o    ")
    print("  o o                                                                    o o   ")
    print(" o   o          Enter the number of bees you want to create             o   o  ")
    print("  o o         to your total population ( the maximum is 1851 )           o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    
    userInput = input("                                    ")
    
    return userInput
    



def getUserDefensePopulation():
    print("  o o                                                                o o       ")
    print(" o   o                                                              o   o      ")
    print("  o o                                                                 o o      ")
    print("   o o                                                                 o o     ")
    print("  o   o                                                               o   o    ")
    print("   o o                                                                 o o     ")
    print("  o o                                                                   o o    ")
    print(" o   o                                                                 o   o   ")
    print("  o o                                                                   o o    ")
    print("  o o                                                                    o o   ")
    print(" o   o            Enter the number of bees you want to assign           o   o  ")
    print("  o o             to defending the hive ( the maximum is 600 )           o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o         ( The average hive has a defense of 2000 bees )          o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    
    userInput = input("                                    ")
    
    return userInput
    

    
    
    
    








