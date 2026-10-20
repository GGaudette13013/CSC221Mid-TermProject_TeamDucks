'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: main.py
Description:  
'''

from DucksProject1 import welcome_introduction
from DucksProject1 import userInput
from DucksProject1.userTaskExecution import getUserTask, getUserTaskValidation
def main():
    # constants
    
    
    
    
    
    
    
    # Title and program instructions
    welcome_introduction.display_welcome_functionality()
    welcome_introduction.display_userInput_functionality()
  
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
 
    
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    