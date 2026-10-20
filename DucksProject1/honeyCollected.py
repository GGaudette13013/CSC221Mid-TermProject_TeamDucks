'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: honeyCollected.py
Description: Calculates nectar collection and honey production with environmental events.
'''



# Constants
PER_BEE_NECTAR = 0.00072
PER_BEE_CONSUMED = 0.00060
PER_BEE_HONEY = 0.00012
START_HONEY = 0.00080
flowerMultipier = 1.0
'''
Starting values:

Open to change later but this is more of a place holder for now; I have plans to change this later on.
'''


totalHoney = 0


def totalHoney_accumulator(honeyAdd, day, starter_honey):
    if day == 1:
        totalHoney = starter_honey
    
    else:
        totalHoney = totalHoney + honeyAdd
    
    
    return totalHoney





def calcHoney_production(foraging_bees, flowerMultiplier, event, totalHivePop):
    
    totalNectar = 0
    
    if event == "drought":
        flowerMultiplier = 0.5

    elif event == "rainy":
        flowerMultiplier = 1.5

    else:
        flowerMultiplier = 1.0
    
    
    
    nectarCollected = flowerMultiplier * foraging_bees * PER_BEE_NECTAR 
    
    honeyTotal = flowerMultiplier * foraging_bees * PER_BEE_HONEY
    
    nectarConsumed = totalHivePop * PER_BEE_CONSUMED
    
    totalNectar = totalNectar + nectarCollected
    
    
    return totalNectar, honeyTotal, nectarConsumed










