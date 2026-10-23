'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: honeyCollected.py
Description: Calculates nectar collection and honey production with environmental events.
'''

import envEvent


# Constants
PER_BEE_NECTAR = 0.00072
PER_BEE_CONSUMED = 0.00060
PER_BEE_HONEY = 0.00012
START_HONEY_RATE = 0.00080
OTHER_BEES_CONSUMPTION = 0.00025
flowerMultiplier = 1.0
totalHoney = 0

'''
Starting values:

Open to change later but this is more of a place holder for now; I have plans to change this later on.
'''



def totalHoney_calc(day, nethoney, starterHoney, totalHoney):
    if day == 1:
        totalHoney = starterHoney
        return totalHoney
        
    else:
        
        totalHoney = totalHoney + nethoney
        
        return totalHoney
        
    
     
    
    

def starterHoney_calc(population):
    
    honey = population * START_HONEY_RATE
    
    return honey
    
    




def flowerMultiplier_calc(event):
    global flowerMultiplier
    
    if event == "drought":
        flowerMultiplier = 0.5

    elif event == "rainy":
        flowerMultiplier = 1.5

    else:
        flowerMultiplier = 1.0
    
    
    return flowerMultiplier
    
    
      
def nectarCollected_calc(foragingBees, flowerMultiplier):
    
    nectar = foragingBees * PER_BEE_NECTAR * flowerMultiplier
    
    return nectar
    
    
    
    
    
    
    
def nectarConsumed_calc(daysNectar, dayTask, population, foragingBees):
    if dayTask == "F":
        netHoney = 0  
        # calc  bees consumption
        hiveConsumption = (foragingBees * PER_BEE_CONSUMED) + (population * OTHER_BEES_CONSUMPTION)
        
        # subtract from nectar
        netHoney = daysNectar - hiveConsumption
        
        
        # Gavin's anti-negative scheme
        if netHoney < 0:
            #kills bees from pop who did not get 1kg of honey!! if negative it is real bad
            population = population + netHoney 
            netHoney = 0
        else:
            netHoney = netHoney
        
        return netHoney, hiveConsumption
    
    else:
        netHoney = 0
        hiveConsumption = (population * OTHER_BEES_CONSUMPTION)
        netHoney = (population * OTHER_BEES_CONSUMPTION) * (-1)  # ? 
        
        return  netHoney, hiveConsumption
        
    
    
def dailyHoney_calc(event, starterPopulation, beesForaging, task, day, population):
    
    if isinstance(event, int):
        event = envEvent.event_identifier(event)
    
    if task == "F":
         
        flowerMultiplier = flowerMultiplier_calc(event)
        nectar = nectarCollected_calc(beesForaging, flowerMultiplier)
        
        dayshoney, honeyEaten = nectarConsumed_calc(nectar, task, population, beesForaging)
        
        starterHoney = starterHoney_calc(starterPopulation)
        hiveHoney = totalHoney_calc(day, dayshoney, starterHoney, totalHoney)
        
    else:
        
        beesForaging = 0
        flowerMultiplier = 0
        nectar = nectarCollected_calc(beesForaging, flowerMultiplier)
        
        dayshoney, honeyEaten = nectarConsumed_calc(nectar, task, population, beesForaging)
        starterHoney = starterHoney_calc(starterPopulation)
        hiveHoney = totalHoney_calc(day, dayshoney, starterHoney, totalHoney)
        
    
    return honeyEaten, hiveHoney, nectar
    