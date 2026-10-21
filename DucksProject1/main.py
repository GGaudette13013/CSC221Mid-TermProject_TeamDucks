'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: main.py
Description:  
'''

from DucksProject1 import welcome_introduction
from DucksProject1 import userInput
from DucksProject1.userTaskExecution import getUserTask, getUserTaskValidation
from DucksProject1 import honeyCollected
from DucksProject1 import envEvent
def main():
    # constants
    
    
    
    
    
    
    
    # Title and program instructions
    welcome_introduction.display_welcome_functionality()
    welcome_introduction.display_userInput_functionality()
    
    # displays game mode
    
    game_mode = welcome_introduction.display_instructions_userInput_ModeSelector_functionality()
    
    
    
    
    
    
    
    if game_mode == "R":
        
        
        
        # realtime mode starts here 
             # Get simulation days and starting bee population
        days = userInput.getUserDays()
        startingPopulation = userInput.getUserBeehiveStarterPopulation(days)
        # Calculate the starting honey supply
        totalHoney = honeyCollected.calcStarterHoney(startingPopulation)

        print("Starting Honey Supply:", format(totalHoney, ".4f"), "kg")
        # realtime mode:
        # Loop through each simulation day
        for day in range(1, days + 1, 1):
            print("Day", day)
            # Generate a random event for the day
            eventNumber = envEvent.event_randomizer()

            # Identify which event occurred
            currentEvent = envEvent.event_identifier(eventNumber)

            # Display the event
            print("Today's Event:", currentEvent)
        # Getting user task
            task = getUserTask()
            task = getUserTaskValidation(task)
            foragingBees = 0
            # Check if the player wants to forage
            if task == "F" or task == "f":

                foragingBees = userInput.getUserForagingBees(startingPopulation)

                print("Bees sent foraging:", foragingBees)
                # Calculate daily honey collection and consumption
                dailyConsumption, totalHoney = honeyCollected.calcHoneyForageFunctionality(
                startingPopulation,
                foragingBees,
                currentEvent,
                startingPopulation,
                task,
                day,
                totalHoney
            )

# Display updated honey supply
            print("Honey Consumed:", format(dailyConsumption, ".4f"), "kg")
            print("Honey Remaining:", format(totalHoney, ".4f"), "kg")
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
        pass
        
        
        
        
        
        
        
        
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    