'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: hivePopulations.py
Description: Manages the beehive population by tracking the number of bees and updating the population throughout the simulation.
'''
# how does this work with the global - this might cause some bugs
totalPopulation = 0
totalDefensePopulation = 0

# THIS FUNCTION AND CREATEBEESPOPULATIONADDITION DO THE SAME THING...NOT SURE IF THAT IS GOING TO BE A PROBLEM
def totalPopulation_accumulator(population, day, additionalPop, runningPopulation):
    # population is from main input - starter
    # after starter, it is from tasks
    
    if day == 1:
        additionalPop = 0
        runningPopulation = population
        
    
    
    runningPopulation = runningPopulation + additionalPop
    
    
    return runningPopulation


    
    
    
    
    

def foragingPopulation_accumulators(beesSentToForage):
    foraging_bees = 0
    foraging_bees = foraging_bees + beesSentToForage
    
    
    
    
    return foraging_bees
    
    
    


 
def defensePopulation_accumulators(beesSentToDefense, day, totalDefensePopulation):
    if day == 1:
        totalDefensePopulation = 100
        if totalDefensePopulation > 100:
            totalDefensePopulation = 100
    
    else:
        totalDefensePopulation = totalDefensePopulation + beesSentToDefense
        beesSentToDefense = 0
    
    
    return totalDefensePopulation
    
    
    
    
    