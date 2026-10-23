'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: honeyCollected.py
Description: Calculates nectar collection and honey production with environmental events.
'''




# Constants
PER_BEE_NECTAR = 0.00072
PER_BEE_CONSUMED = 0.00060
PER_BEE_HONEY = 0.00012
START_HONEY_RATE = 0.00080
OTHER_BEES_CONSUMPTION = 0.00025
flowerMultipier = 1.0
totalHoney = 0
'''
Starting values:

Open to change later but this is more of a place holder for now; I have plans to change this later on.
'''



def totalHoney_calc(day, nethoney, starterHoney, totalHoney):
    if day == 1:
        totalHoney = starterHoney + nethoney
        if totalHoney < 0:
            totalHoney = 0
        return totalHoney
        
    else:
        
        totalHoney = totalHoney + nethoney
        if totalHoney < 0:
            totalHoney = 0
        
        return totalHoney
        
    
     
    
    

def starterHoney_calc(population):
    
    honey = population * START_HONEY_RATE
    
    return honey
    
    




def flowerMultipier_calc(event):
    
    if event == "drought":
        flowerMultiplier = 0.5

    elif event == "rainy":
        flowerMultiplier = 1.5

    else:
        flowerMultiplier = 1.0
    
    
    return flowerMultiplier
    
    
      
def nectarCollected_calc(foragingBees, flowerMultipier):
    
    nectar = foragingBees * PER_BEE_NECTAR * flowerMultipier
    
    return nectar
    
    
    
    
    
    
    
def nectarConsumed_calc(daysNectar, dayTask, population, foragingBees):
    if dayTask == "F":
        netHoney = 0  
        # calc  bees consumption
        hiveConsumption = (foragingBees * PER_BEE_CONSUMED) + ((population - foragingBees) * OTHER_BEES_CONSUMPTION)
        
        # subtract from nectar
        netHoney = daysNectar - hiveConsumption
        
        return netHoney, hiveConsumption
    
    else:
        netHoney = 0
        hiveConsumption = (population * OTHER_BEES_CONSUMPTION)
        netHoney = (population * OTHER_BEES_CONSUMPTION) * (-1)  # ? 
        
        return  netHoney, hiveConsumption
        
    
    
def dailyHoney_calc(event, starterPopulation, beesForaging, task, day, population, totalHoney):
    if task == "F":
        
        
        flowerMultipier = flowerMultipier_calc(event)
        nectar = nectarCollected_calc(beesForaging, flowerMultipier)
        
        dayshoney, honeyEaten = nectarConsumed_calc(nectar, task, population, beesForaging)
        
        starterHoney = starterHoney_calc(starterPopulation)
        hiveHoney = totalHoney_calc(day, dayshoney, starterHoney, totalHoney)
    else:
        beesForaging = 0
        flowerMultipier = 0
        nectar = nectarCollected_calc(beesForaging, flowerMultipier)
        dayshoney, honeyEaten = nectarConsumed_calc(nectar, task, population, beesForaging)
        starterHoney = starterHoney_calc(starterPopulation)
        hiveHoney = totalHoney_calc(day, dayshoney, starterHoney, totalHoney)
        
    
    return honeyEaten, hiveHoney, nectar
    
    
    
    
    
    
    

    
    
    
    
    
    
    
