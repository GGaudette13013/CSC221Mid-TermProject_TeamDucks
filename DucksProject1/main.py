'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: main.py
Description:  
'''

from DucksProject1 import welcome_introduction, envEvent
from DucksProject1 import userTaskExecution
from DucksProject1 import hivePopulations
from DucksProject1 import honeyCollected
from DucksProject1 import realtimeMode

def main():
    # constants
    honeyAdd = 0
    foraging_bees = 0
    defense_bees = 0
    totalHoney = 0
    additionalPopulation = 0
    totalPopulation = 0
    # Title and program instructions
    welcome_introduction.display_welcome_functionality()
    dayCount, startingPopulation, game_mode = welcome_introduction.display_userInput_functionality()
    
    # for loop for days starts here after days and starer population has been given
    
    if game_mode == "R":
    
            # realtime mode starts here 
            # Get simulation days and starting bee population
        
        # realtime mode:
        
        
        # Loop through each simulation day
        for day in range(1, dayCount + 1, 1):
                    
            # This is realtime mode :
            # population accumulators
            totalPopulation = hivePopulations.totalPopulation_accumulator(startingPopulation, day, additionalPopulation, totalPopulation)
            
            
            # generate event
            eventNumber = envEvent.event_randomizer()
            eventID = envEvent.event_identifier(eventNumber)
            event = envEvent.event_handler(eventID, foraging_bees, totalPopulation, defense_bees, totalHoney)
            
            # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
            startingHoney = honeyCollected.starterHoney_calc(startingPopulation)
            honeyTotal = honeyCollected.totalHoney_calc(day, honeyAdd, startingHoney, totalHoney)
            flower_multipier = honeyCollected.flowerMultipier_calc(event)
            nectarProduction = honeyCollected.nectarCollected_calc(foraging_bees, flower_multipier)
            # deleted additional totalPopulations repeat
            totalBeesForageing = hivePopulations.foragingPopulation_accumulators(foraging_bees)
            defense_bees = hivePopulations.defensePopulation_accumulators(defense_bees, day, defense_bees)
            
            
            # Displays updated info on info station - realtimeMode stuff
            realtimeMode.realtimeMode_menu(honeyTotal, nectarProduction, totalPopulation, totalBeesForageing, defense_bees)
            #Need to create a display functionality that displays event graphic to user. 
            #realtimeMode.realtimeMode_menu_eventDisplay_Normal() normal mode
            realtimeMode.realtimeMode_menu_operations()
            
            # Getting user task
            task = userTaskExecution.getUserTask()
            userTaskExecution.getUserTaskValidation(task)
            taskAction = userTaskExecution.userTaskIdentification(task, totalPopulation, day, startingPopulation, defense_bees)
            # how to affect the honey production. 
            honeyEaten, totalHoney, daysHoney = honeyCollected.dailyHoney_calc(eventID, startingPopulation, taskAction, task, day, totalPopulation)
            # this is probably going to double our honey... just temporary
            
            # Feed bees
            realtimeMode.realtimeMode_menu_FeedBees_functionality(task, daysHoney, totalHoney, totalPopulation, honeyEaten)
            honeyAdd = daysHoney
    
    else:
        # simulation mode starts here 
        print("smiles")
        
        
        
        
        
        
        
        
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    