'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: honeyCollected.py
Description: Calculates nectar collection and honey production with environmental events.
'''



# Constants
PER_BEE_NECTAR = 0.00072
PER_BEE_CONSUMED = 0.00060
PER_DORMANT_BEE_CONSUMED = 0.00025
PER_BEE_HONEY = 0.00012
START_HONEY = 0.00080
flowerMultipier = 1.0


totalHoney = 0


def totalHoney_accumulator(totalHoney, honeyAdd, day, starter_honey):

    totalHoney = totalHoney + honeyAdd

    return totalHoney





def calcHoney_production(foraging_bees, flowerMultiplier, event, totalHivePop):
    
    totalNectar = 0
    
    if event == "drought":
        flowerMultiplier = 0.5

    elif event == "rainy":
        flowerMultiplier = 1.0
        foraging_bees = int(foraging_bees * 0.70)

    else:
        flowerMultiplier = 1.0
    
    
    
    nectarCollected = flowerMultiplier * foraging_bees * PER_BEE_NECTAR 
    
    honeyTotal = flowerMultiplier * foraging_bees * PER_BEE_HONEY
    
    # Calculate how many bees are not foraging
    dormantBees = totalHivePop - foraging_bees

    # Calculate food consumed by foraging bees
    foragingConsumption = foraging_bees * PER_BEE_CONSUMED

    # Calculate food consumed by dormant bees
    dormantConsumption = dormantBees * PER_DORMANT_BEE_CONSUMED

    # Calculate total food consumption
    nectarConsumed = foragingConsumption + dormantConsumption
    
    totalNectar = totalNectar + nectarCollected
    
    
    return totalNectar, honeyTotal, nectarConsumed




def calcStarterHoney(startingPop):
    
    starter_honey = startingPop * START_HONEY
    
    return starter_honey
    
    
    
    


def end_day(day_honeyTotal, day_nectarTotal, day_nectarEaten, day_task):

    # Calculate food remaining after consumption
    netHoney = day_nectarTotal - day_nectarEaten

    # Calculate daily food consumption
    dailyConsumption = day_nectarEaten

    return dailyConsumption, netHoney




# This function is to be called from main to organize the info. 
def calcHoneyForageFunctionality(startingPopulaton, foraging_bee_pop, currentEvent, totalHivePopulaton, taskForDay, days, totalHoney):
    starter_honey = calcStarterHoney(startingPopulaton)
    
    global flowerMultipier
    nectarProduced, honey, nectarConsumed = calcHoney_production(foraging_bee_pop, flowerMultipier, currentEvent, totalHivePopulaton)
    
    dailyConsumption, netHoney = end_day(honey, nectarProduced, nectarConsumed, taskForDay)
    
    totalHoney = totalHoney_accumulator(totalHoney, netHoney, days, starter_honey)

    if totalHoney < 0:
        totalHoney = 0

    return dailyConsumption, totalHoney
    
    
    

    
    
    
    