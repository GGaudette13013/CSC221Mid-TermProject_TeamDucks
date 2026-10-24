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
    dayCount, startingPopulation = welcome_introduction.display_userInput_functionality()
    
    # for loop for days starts here after days and starer population has been given
    
    

        # realtime mode starts here 
        # Get simulation days and starting bee population
    
    # realtime mode:
    
    
    # Loop through each simulation day
    for day in range(1, dayCount + 1, 1):
                
        # This is realtime mode :
        # population accumulators
        totalPopulation = hivePopulations.totalPopulation_accumulator(startingPopulation, day, additionalPopulation, totalPopulation)
        
        startingHoney = honeyCollected.starterHoney_calc(startingPopulation)
        if day == 1:
            totalHoney = totalHoney + startingHoney
        # generate event
        eventNumber = envEvent.event_randomizer()
        eventID = envEvent.event_identifier(eventNumber)
        print("Defense before event:", defense_bees)
        foraging_bees, totalPopulation, defense_bees, totalHoney = envEvent.event_handler(eventID, foraging_bees, totalPopulation, defense_bees, totalHoney)
        print("Defense after event:", defense_bees)
        # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
        flower_multipier = honeyCollected.flowerMultiplier_calc(eventID)
        nectarProduction = honeyCollected.nectarCollected_calc(foraging_bees, flower_multipier)
        # deleted additional totalPopulations repeat
        foraging_bees = hivePopulations.foragingPopulation_accumulators(foraging_bees)
        Defense_beesTotalFromPreviousDay = 0
        defense_bees = hivePopulations.defensePopulation_accumulators(defense_bees, day, Defense_beesTotalFromPreviousDay)
        
        
        # Displays updated info on info station - realtimeMode stuff
        daysremaining = realtimeMode.realtimeMode_menu_CalcDaysRemaining(day, dayCount)
        realtimeMode.realtimeMode_menu(totalHoney, daysremaining, totalPopulation, foraging_bees, defense_bees)
        #Need to create a display functionality that displays event graphic to user. 
        print()
        print("========================================")
        print("           TODAY'S EVENT")
        print("========================================")
        print("Event:", eventID)
        print("========================================")
        print()
        if eventID == "normal":
            realtimeMode.realtimeMode_menu_eventDisplay_Normal()
        elif eventID == "black bear":
            realtimeMode.realtimeMode_menu_eventDisplay_BlackBear()
        elif eventID == "hornets":
            realtimeMode.realtimeMode_menu_eventDisplay_Hornets()
        elif eventID == "rainy":
            realtimeMode.realtimeMode_menu_eventDisplay_Rainy()
        elif eventID == "drought":
            realtimeMode.realtimeMode_menu_eventDisplay_Drought()
        elif eventID == "small hive beetle":
            realtimeMode.realtimeMode_menu_eventDisplay_Beetle()
        elif eventID == "pesticides":
            realtimeMode.realtimeMode_menu_eventDisplay_Pesticides()
        realtimeMode.realtimeMode_menu_operations()
        # Getting user task
        task = userTaskExecution.getUserTask()
        task = userTaskExecution.getUserTaskValidation(task)
        foraging_bees, totalPopulation, defense_bees = userTaskExecution.userTaskIdentification(task, totalPopulation, day, startingPopulation, defense_bees)
        
        # how to affect the honey production. 
        honeyEaten, totalHoney, daysHoney = honeyCollected.dailyHoney_calc(eventID, startingPopulation, foraging_bees, task, day, totalPopulation, totalHoney)
        # this is probably going to double our honey... just temporary
        
        # Feed bees
        realtimeMode.realtimeMode_menu_FeedBees_functionality(task, daysHoney, totalHoney, totalPopulation, honeyEaten)
        # adds back the forage pop to total pop
        # Reset foraging bees for the next day
        foraging_bees = 0
    
    print()
    print("========================================")
    print("         SIMULATION COMPLETE")
    print("========================================")
    print("Days Simulated:", dayCount)
    print("Final Bee Population:", totalPopulation)
    print("Honey Remaining (KG):", format(totalHoney, ".2f"))
    print("========================================")
    if totalPopulation > 0 and totalHoney > 0:
        print("Congratulations! Your beehive survived the winter preparation!")
    else:
        print("Unfortunately, your beehive did not survive.")
    
    
    
    
        
        
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    