'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: main.py
Description:  
'''

from DucksProject1 import welcome_introduction
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
    # Title and program instructions
    welcome_introduction.display_welcome_functionality()
    dayCount, starterPopulation = welcome_introduction.display_userInput_functionality()
    
    # displays game mode
    
    game_mode = welcome_introduction.display_instructions_userInput_ModeSelector_functionality()
    
    
    
    # for loop for days starts here after days and starer population has been given
    
    # This is realtime mode :
    # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
    honeyTotal = honeyCollected.totalHoney_accumulator(honeyAdd, starterPopulation)
    nectarProduction = honeyCollected.calcHoney_production(foraging_bees)
    totalBeehivePopulation = hivePopulations.totalPopulation_accumulator(starterPopulation)
    totalBeesForageing = hivePopulations.foragingPopulation_accumulators(foraging_bees)
    TotalBeeDefenceCount = hivePopulations.defensePopulation_accumulators(defense_bees)
    
    
    # Displays updated info on info station - realtimeMode stuff
    realtimeMode.realtimeMode_menu(honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount)
    realtimeMode.realtimeMode_menu_eventDisplay_Normal()
    realtimeMode.realtimeMode_menu_operations()
    # Getting user task
    task = userTaskExecution.getUserTask()
    userTaskExecution.getUserTaskValidation(task)
    taskID = userTaskExecution.userTaskIdentification(task)
    # how to affect the honey production. 
    
    # Feed bees
    realtimeMode.realtimeMode_menu_FeedBees_functionality(task, honeyTotal, nectarProduction, totalBeehivePopulation)
    
    if game_mode == "R":
        
        
        
            # realtime mode starts here 
            # Get simulation days and starting bee population
        days = userInput.getUserDays()
        startingPopulation = userInput.getUserBeehiveStarterPopulation(days)
        # realtime mode:
        # Loop through each simulation day
        for day in range(1, days + 1, 1):
            print("Day", day)
        # Getting user task
            task = getUserTask()
            task = getUserTaskValidation(task)
    # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
    
    
    # Displays updated info on info station
    
    # simulation mode:
    # have not yet worked on this... 
 
    
    
        
        
           
        
        # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
        
        
        # Displays updated info on info station
        
        
        # Getting user task
        task = getUserTask()
        getUserTaskValidation(task)
        
    
    
    
    
    
    else:
        # simulation mode starts here 
        
        
        
        
        
        
        
        
        
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    