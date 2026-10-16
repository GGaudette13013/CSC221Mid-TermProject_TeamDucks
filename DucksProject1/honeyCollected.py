'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: honeyCollected.py
Description:  
'''
totalHoney = 0
totalNectar = 0
PER_BEE_NECTAR = 0.00072


def totalHoney_accumulator(honeyAdd, starterPopulation):
    if honeyAdd == 0:
        totalHoney = starterPopulation
    else:
        totalHoney = totalHoney + honeyAdd
        
    
    
    return totalHoney



def calcHoney_production(foraging_bees):
    dailyHoney = PER_BEE_NECTAR * foraging_bees
    
    return dailyHoney
    
    
    

    
    
    
    
    

    
    
    
    

    
    
    
    