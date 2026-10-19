'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: honeyCollected.py
Description: Calculates nectar collection and honey production with environmental events.
'''

import envEvent

# Constants
PER_BEE_NECTAR = 0.00072
PER_BEE_CONSUMED = 0.00072
PER_BEE_HONEY = 0.00012

#Starting Variables
totalHoney = 0.0
totalNectar = 0.0



def totalHoney_accumulator(honeyAdd, starterPopulation):
    global totalHoney

    totalHoney += honeyAdd * starterPopulation

    return totalHoney



def calcHoney_production(foraging_bees, flowerMultiplier=1.0):
    global totalNectar

    nectarCollected = (
        PER_BEE_NECTAR
        * foraging_bees
        * flowerMultiplier
    )

    totalNectar += nectarCollected

    return nectarCollected



def apply_event(currentEvent):
    global totalNectar

    flowerMultiplier = 1.0

    if currentEvent == "drought":
        flowerMultiplier = 0.5

    elif currentEvent == "rainy":
        flowerMultiplier = 1.5

    elif currentEvent == "black bear":
        flowerMultiplier = 0.8

    elif currentEvent == "hornets":
        flowerMultiplier = 0.8

    elif currentEvent == "small hive beetle":
        flowerMultiplier = 0.9

    elif currentEvent == "pesticides":
        flowerMultiplier = 0.5
        
    else:
        flowerMultiplier = 1.0
    
    return flowerMultiplier



def end_day(foraging_bees, flowerMultiplier=1.0):
    global totalNectar, totalHoney

    dailyConsumption = PER_BEE_CONSUMED * foraging_bees
    netHoney = PER_BEE_HONEY * foraging_bees * flowerMultiplier

    totalNectar = max(0.0, totalNectar - dailyConsumption)
    totalHoney += netHoney

    return netHoney



def run_daily_events(foraging_bees):
    eventNumber = envEvent.event_randomizer()
    currentEvent = envEvent.event_identifier(eventNumber)

    print("Today's event: " + currentEvent)

    flowerMultiplier = apply_event(currentEvent)

    nectarCollected = calcHoney_production(
        foraging_bees, flowerMultiplier
    )

    print("Nectar collected: " + format(nectarCollected, '.5f') + " kg")

    netHoney = end_day(foraging_bees, flowerMultiplier)

    print("Net honey produced: " + format(netHoney, '.5f') + " kg")

    display_honey()



def display_honey():
    print("\\n===== HONEY REPORT =====")
    print("Stored nectar: " + format(totalNectar, '.5f') + " kg")
    print("Total honey produced: " + format(totalHoney, '.5f') + " kg")
    print("========================")


