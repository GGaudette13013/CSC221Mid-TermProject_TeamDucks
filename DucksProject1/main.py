'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: main.py
Description:  
'''

from DucksProject1 import welcome_introduction, envEvent
from DucksProject1 import userInput
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
            totalPopulation = hivePopulations.totalPopulation_accumulator(startingPopulation)
            
            
            # generate event
            eventNumber = envEvent.event_randomizer()
            eventID = envEvent.event_identifier(eventNumber)
            event = envEvent.event_handler(eventID, foraging_bees, totalPopulation, defense_bees, totalHoney)
            
            # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
            startingHoney = honeyCollected.starterHoney_calc(startingPopulation)
            honeyTotal = honeyCollected.totalHoney_calc(day, honeyAdd, startingHoney)
            flower_multipier = honeyCollected.flowerMultipier_calc(event)
            nectarProduction = honeyCollected.nectarCollected_calc(foraging_bees, flower_multipier)
            totalPopulation = hivePopulations.totalPopulation_accumulator(startingPopulation)
            totalBeesForageing = hivePopulations.foragingPopulation_accumulators(foraging_bees)
            TotalBeeDefenceCount = hivePopulations.defensePopulation_accumulators(defense_bees)
            
            
            # Displays updated info on info station - realtimeMode stuff
            realtimeMode.realtimeMode_menu(honeyTotal, nectarProduction, totalPopulation, totalBeesForageing, TotalBeeDefenceCount)
            realtimeMode.realtimeMode_menu_eventDisplay_Normal()
            realtimeMode.realtimeMode_menu_operations()
            # Getting user task
            task = userTaskExecution.getUserTask()
            userTaskExecution.getUserTaskValidation(task)
            taskID = userTaskExecution.userTaskIdentification(task)
            # how to affect the honey production. 
            honeyEaten, totalHoney = honeyCollected.dailyHoney_calc(eventID, startingPopulation, foraging_bees, task, dayCount, totalPopulation)
            starterHoney = honeyCollected.starterHoney_calc(startingPopulation)
            # this is probably going to double our honey... just temporary
            hiveHoneyTotal = honeyCollected.totalHoney_calc(dayCount, totalHoney, starterHoney)
            
            
            
            
            
            # Feed bees
            realtimeMode.realtimeMode_menu_FeedBees_functionality(task, hiveHoneyTotal, totalHoney, totalPopulation, honeyEaten)
            
        
        
        
        
    
        
        
           
        
        # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
        
        
        # Displays updated info on info station
        
        
        # Getting user task
       
    
    
    
    else:
        # simulation mode starts here 
        print("smiles")
        
        
        
        
        
        
        
        
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    