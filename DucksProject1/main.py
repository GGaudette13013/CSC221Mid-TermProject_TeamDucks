'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: main.py
Description:Runs the main beehive simulator, manages player choices, and updates the hive's population, honey supply, and daily events.
'''

def main():
    # constants
    honeyAdd = 0
    foraging_bees = 0
    defense_bees = 0
    totalHoney = 0
    additionalPopulation = 0
    totalPopulation = 0
    # Title and program instructions
    display_welcome_functionality()
    dayCount, startingPopulation = display_userInput_functionality()
    
    # for loop for days starts here after days and starer population has been given
    
    

        # realtime mode starts here 
        # Get simulation days and starting bee population
    
    # realtime mode:
    
    
    # Loop through each simulation day
    for day in range(1, dayCount + 1, 1):
                
        # This is realtime mode :
        # population accumulators
        totalPopulation = totalPopulation_accumulator(startingPopulation, day, additionalPopulation, totalPopulation)
        
        startingHoney = starterHoney_calc(startingPopulation)
        if day == 1:
            totalHoney = totalHoney + startingHoney
        # generate event
        eventNumber = event_randomizer()
        eventID = event_identifier(eventNumber)
        print("Defense before event:", defense_bees)
        foraging_bees, totalPopulation, defense_bees, totalHoney = event_handler(eventID, foraging_bees, totalPopulation, defense_bees, totalHoney)
        print("Defense after event:", defense_bees)
        # accumulates all the running totals including honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount
        flower_multipier = flowerMultiplier_calc(eventID)
        nectarProduction = nectarCollected_calc(foraging_bees, flower_multipier)
        # deleted additional totalPopulations repeat
        foraging_bees = foragingPopulation_accumulators(foraging_bees)
        Defense_beesTotalFromPreviousDay = 0
        defense_bees = defensePopulation_accumulators(defense_bees, day, Defense_beesTotalFromPreviousDay)
        
        
        # Displays updated info on info station - realtimeMode stuff
        daysremaining = realtimeMode_menu_CalcDaysRemaining(day, dayCount)
        realtimeMode_menu(totalHoney, daysremaining, totalPopulation, foraging_bees, defense_bees)
        #Need to create a display functionality that displays event graphic to user. 
        print()
        print("========================================")
        print("           TODAY'S EVENT")
        print("========================================")
        print("Event:", eventID)
        print("========================================")
        print()
        if eventID == "normal":
            realtimeMode_menu_eventDisplay_Normal()
        elif eventID == "black bear":
            realtimeMode_menu_eventDisplay_BlackBear()
        elif eventID == "hornets":
            realtimeMode_menu_eventDisplay_Hornets()
        elif eventID == "rainy":
            realtimeMode_menu_eventDisplay_Rainy()
        elif eventID == "drought":
            realtimeMode_menu_eventDisplay_Drought()
        elif eventID == "small hive beetle":
            realtimeMode_menu_eventDisplay_Beetle()
        elif eventID == "pesticides":
            realtimeMode_menu_eventDisplay_Pesticides()
        realtimeMode_menu_operations()
        # Getting user task
        task = getUserTask()
        task = getUserTaskValidation(task)
        foraging_bees, totalPopulation, defense_bees = userTaskIdentification(task, totalPopulation, day, startingPopulation, defense_bees)
        
        # how to affect the honey production. 
        honeyEaten, totalHoney, daysHoney = dailyHoney_calc(eventID, startingPopulation, foraging_bees, task, day, totalPopulation, totalHoney)
        # this is probably going to double our honey... just temporary
        
        # Feed bees
        realtimeMode_menu_FeedBees_functionality(task, daysHoney, totalHoney, totalPopulation, honeyEaten)
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
    










    
'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: envEvent.py
Description:  Generates random environmental events that affect the beehive's honey production, population, and defense.
'''
from random import randint






def event_randomizer():
    
    event = randint(1,34)
    
    return event
    



def event_identifier(currentEvent):
    # if else statements concerning the identification of current event produced by event_randomizer
    '''
    KEY FOR EVENTS
    
    11          drought
    15          rainy
    22          blackbear
    32          hornets
    2           small hive beetle
    6           pesticides
    '''
    
    if currentEvent == 11 or currentEvent == 8 or currentEvent == 9:
        condition = "drought"
     
    elif currentEvent == 15 or currentEvent == 17 or currentEvent == 18:
        condition = "rainy"
    
    elif currentEvent == 22:
        condition = "black bear"
    
    elif currentEvent == 32 or currentEvent == 33 or currentEvent == 34:
        condition = "hornets"
   
    elif currentEvent == 2 or currentEvent == 3 or currentEvent == 4:
        condition = "small hive beetle"
    
    elif currentEvent == 6:
        condition = "pesticides"
    
    
    
    else:
        condition = "normal"
        
        
    return condition
    



def eventCondition_drought():
    # direct affect - flowerMultipier()
    weather = "drought"
    
    return weather
    
    

def eventCondition_rainy(forage_pop):
    RAINY_FORAGING_RATE = .30
    
    weather = "rainy"
    
    forage_pop = int(forage_pop * RAINY_FORAGING_RATE)
    
    return weather, forage_pop
    

def eventCondition_blackBear(defense, totalHoney):
    BEAR_ATTACK_CONSTANT = .50

    defense = int(defense * BEAR_ATTACK_CONSTANT)
    totalHoney = totalHoney * BEAR_ATTACK_CONSTANT

    return defense, totalHoney
    
    
    
    

def eventCondition_hornets(defense, population, totalHoney):
    
    HORNET_ATTACK_CONSTANT = .80
    HORNETS_HONEY = .80
    

    defense = defense * HORNET_ATTACK_CONSTANT
    population = population * HORNET_ATTACK_CONSTANT
    totalHoney = totalHoney * HORNETS_HONEY
    
    return defense, population, totalHoney
    
    

def eventCondition_smallHiveBeetle(defense, totalHoney):
    SMALLHIVEBEETLE_ATTACK_CONSTANT = 10
    
    defense = defense - 10
    totalHoney = totalHoney - SMALLHIVEBEETLE_ATTACK_CONSTANT
    

    return defense, totalHoney
    
    

def eventCondition_pesticides(population):
    
    PESTICIDE_DAMAGE = .50
    
    population = population * PESTICIDE_DAMAGE
    
    return population
    
    
    

def eventCondition_normal():
    weather = "normal"
    
    return weather
    
    

    
 
 
 
    

def event_handler(eventIdentity, forage_pop, population, defense, totalHoney):
    if eventIdentity == "drought":
        eventCondition_drought()
    
    elif eventIdentity == "rainy":
        weather, forage_pop = eventCondition_rainy(forage_pop)
        
        
    elif eventIdentity == "black bear":
        defense, totalHoney = eventCondition_blackBear(defense, totalHoney)
        
        
    elif eventIdentity == "hornets":
        if defense < 500:
            defense, population, totalHoney = eventCondition_hornets(defense, population, totalHoney)
        
        else:
            
            eventCondition_normal()
            
        
    elif eventIdentity == "small hive beetle":
        if totalHoney <= 39:
            defense, totalHoney = eventCondition_smallHiveBeetle(defense, totalHoney)
        
            if defense < 0:
                defense = 0
            else:
                defense = defense
                
        else:
            eventCondition_normal()        
                
        
    
    elif eventIdentity == "pesticides":
        population = eventCondition_pesticides(population)
        
    
    else:
        eventCondition_normal()
    
    if totalHoney < 0:
        totalHoney = 0
        if population < 0:
            population = 0

        if defense < 0:
            defense = 0
    population = int(population)
    defense = int(defense)
    return forage_pop, population, defense, totalHoney

        
    
    
    
    
    
    
    



'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: hivePopulations.py
Description: Manages the beehive population by tracking the number of bees and updating the population throughout the simulation.
'''

totalPopulation = 0
totalDefensePopulation = 0

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
flowerMultiplier = 1.0
totalHoney = 0

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
    
    




def flowerMultiplier_calc(event):
    global flowerMultiplier
    
    if event == "drought":
        flowerMultiplier = 0.5

    elif event == "rainy":
        flowerMultiplier = 1.0

    else:
        flowerMultiplier = 1.5
    
    
    return flowerMultiplier
    
    
      
def nectarCollected_calc(foragingBees, flowerMultiplier):
    
    nectar = foragingBees * PER_BEE_NECTAR * flowerMultiplier
    
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
        originalBees = beesForaging
        flowerMultiplier = flowerMultiplier_calc(event)

        if event == "rainy":
            beesForaging = int(beesForaging * 0.70)

        nectar = nectarCollected_calc(beesForaging, flowerMultiplier)
        
        dayshoney, honeyEaten = nectarConsumed_calc(nectar, task, population, originalBees)
        
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
    









'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: simulation_mode#starter.py
Description: Displays the beehive's current honey supply, population, defense, and days remaining during the simulation.
'''



def realtimeMode_menu_CalcDaysRemaining(daysTotal, today):
    dayLeft = today - daysTotal
    return dayLeft
    
    


def realtimeMode_menu(honeyTotal, daysLeft, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount):
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o   ")
    print(" o     HONEY PRODUCION (KG): ", format (honeyTotal, ".2f"), " Days Remaining: ", daysLeft, "            BEEHIVE POPULATION: ", totalBeehivePopulation, "         o  ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o   ")
    print("                                                                                 o                       o  ")
    print("                                                                                  o BEES FORAGING :", totalBeesForageing, "    o   ")
    print("                                                                                 o                       o  ")
    print("                                                                                  o BEE DEFENSE   :", TotalBeeDefenceCount, "    o   ")
    print("                                                                                 o                       o  ")
    print("                                                                                  o o  o o  o o  o o  o o   ")
    
'''
honeyTotal                    -    totalHoney_accumulator(honeyAdd, starterPopulation)
nectarProduction              -    calcHoney_production(foraging_bees)
totalBeehivePopulation        -    totalPopulation_accumulator(population)
totalBeesForageing            -    foragingPopulation_accumulators(beesSentToForage)
TotalBeeDefenceCount          -    defensePopulation_accumulators(beesSentToDefense)




'''








def realtimeMode_menu_eventDisplay_Hornets():
    print("          ooooo     ..                           *                                    ")
    print("         oo..:oo    :.:.  *    *                                                      ")
    print("        oo.::.:oo   .::     *  *   *  *    * * *                                      ")
    print("        oo:.:.:::.:.           *    *     *  * **                                     ")
    print("        ooooooooo                *          * * *                                     ")
    print("        EVENT STATUS: Hornets                                                         ")
    print("                       kills beehive population by 20% and reduces defense bees by 20%")
    print("\t")
    print("\t")
    
    

    
def realtimeMode_menu_eventDisplay_BlackBear():
    print("   (((    ooooo  / \__ / \     .. .              ")
    print("   @@@ ) oo .:oo( >___=  ) ...::.::.. .          ")
    print("  {   @ oo.  .:oo /* *\   ) ::.:.:.. .. .        ")
    print("  |    \oo:. .:.:  ___    )  .. :.:.  .          ")
    print("  |     ooooooooo::.::.  .. . .::.  ..           ")
    print("  {     EVENT STATUS: Black bear!!                 ")
    print(" reduces bee defense by 50% and stored honey by 50%")
    print("\t")
    print("\t")



    
def realtimeMode_menu_eventDisplay_Beetle():
    print("          ooooo                                                                               ")
    print("         oo O oo                                                                              ")
    print("        oo  ` oo    .:...                                                                     ")
    print("        oo O` .. ..:.:.:..                                                                    ")
    print("        ooooooooo                                                                             ")
    print("        EVENT STATUS: Small Hive Beetle!!                                                     ")
    print("                      consumes honey from the honey production and destroys bee defense by 10%")
    print("\t")
    print("\t")
    
    
    
def realtimeMode_menu_eventDisplay_Rainy():
    print("          ooooo     ' '  '  ''  '   '  '  ' '           ")
    print("         oo..:oo ' '  '  '   '  ''  ' ' '' '            ")
    print("        oo.::.:oo ' ' '  ' ''   '  '   '''  ' '  '      ")
    print("        oo:.:.:::  '  ' ''  '  '' '   '  '  ' '         ")
    print("        ooooooooo  '   '   ' '     '   '    '  '        ")
    print("        EVENT STATUS: Rainy                             ")
    print("                      reduces foraging bee limit by 30% ")
    print("\t")
    print("\t")
    
    
    
def realtimeMode_menu_eventDisplay_Drought():
    print("          ooooo                  . ..:..                              ")
    print("         oo. :oo              .    . .                                ")
    print("        oo. : :oo              #      #   #                           ")
    print("        oo:.                   |      |   |                           ")
    print("        ooooooooo                                                     ")
    print("        EVENT STATUS: Drought                                         ")
    print("                      flowers die and nectar collection is diminished ")
    print("\t")
    print("\t")
    
    
    
    
   

def realtimeMode_menu_eventDisplay_Pesticides():
    print("          ooooo    .                                                            ")
    print("         oo   oo                      .      .                                  ")
    print("        oo  .  oo      .        .                                               ")
    print("        oo    .                                                                 ")
    print("        ooooooooo  #- -         #--      --#     --#                            ")
    print("        EVENT STATUS: Pesticides                                                ")
    print("                      kills 50% of the hive and nectar collection is diminished ")
    print("\t")
    print("\t")
    
    
    
def realtimeMode_menu_eventDisplay_Normal():
    print("          ooooo     ..          ...    8    .          ")
    print("         oo..:oo    :.:.       .   .  888    ..        ")
    print("        oo.::.:oo   .:: . .:.   .      |       .       ")
    print("        oo:.:.:::.:.  .  .   . o    o  |   o  O        ")
    print("        ooooooooo              |    |  |  /   |        ")
    print("        EVENT STATUS: Normal                           ")
    print("                      nothing could be better!         ")
    print("\t")
    print("\t")



    
    
    






def realtimeMode_menu_operations():
        # Forage
    print("  o o  o o  o o  o o  o o  o o  ")
    print(" o  FORAGE        get honey  o ")
    print("  o           :              o  ")
    print(" o   PRESS            F       o ")
    print("  o                          o ")
    
    
    
    # Create bees
    print("  o                          o  ")
    print(" o  CREATE       produce bees o ")
    print("  o           :              o  ")
    print(" o   PRESS            C       o ")
    print("  o                          o ")
    
    
    
    # Defend Nest
    print("  o                          o  ")
    print(" o  DEFEND        defend nest o ")
    print("  o           :              o  ")
    print(" o   PRESS            D       o ")
    print("  o o  o o  o o  o o  o o  o o ")
    




#def display_realtimeMode_functionality(honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount):
#    realtimeMode_menu(honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount):
    
    
    
    
    

def realtimeMode_menu_FeedBeesDispset1a(totalHoney, totalNectar, totalPopulation, beeConsumption):
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    print(" o          T O         C O N C L U D E         D A Y          F E E D        B E E H I V E         H O N E Y           o ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    print("  o                                                                                                                    o  ")
    print(" o                                                                                                                      o ")
    print("  o                     All  bees  return  home  from  foraging  and  are  very  hungry.                               o  ")
    print(" o                      It  is  time  to  feed  the  hive  with  the  honey  you  have.                                 o ")
    print("  o                              Total Honey: ", format(totalHoney, ".2f"), "                                                                       o  ")
    print(" o                     Honey Collected Today: ", totalNectar, "                                                                        o ")
    print("  o                 Total Beehive Population: ", totalPopulation, "                                                                         o  ")
    print(" o                     Total Hive Consumption: ",  beeConsumption,"                                                       o ")
    print("  o                             P R E S S     E N T E R   T O   C O N T I N U E                                        o  ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    input("                                      ")
    
    
    
def realtimeMode_menu_FeedBeesDispSet1b():
    print("  o o  ")
    print(" o   o ")
    print("  o o   o o  o o  o o  o o  o o  o o  o o  o o  o o")
    print(" o   o  Press Enter to     F E E D    H I V E      o")
    
    
    
    userTask = input("  o o          ")







def realtimeMode_menu_FeedBeesDispset2a(totalHoney, totalNectar, totalPopulation, beeConsumption):
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    print(" o          T O         C O N C L U D E         D A Y          F E E D        B E E H I V E         H O N E Y           o ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    print("  o                                                                                                                    o  ")
    print(" o                                                                                                                      o ")
    print("  o                    The bees have been busy increasing the population within the hive                               o  ")
    print(" o                      It  is  time  to  feed  the  hive  with  the  honey  you  have.                                 o ")
    print("  o                 Total Honey: ", format(totalHoney, ".2f"), "                o  ")
    print(" o                     Honey Collected Today: ", totalNectar, "                                                                        o ")
    print("  o                 Total Beehive Population: ", totalPopulation, "                                                                         o  ")
    print(" o                  Total Hive Consumption: ",  beeConsumption,"                                                       o ")
    print("  o                    P R E S S     E N T E R   T O   C O N T I N U E                                                   o  ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    input("                                      ")
    
    
    
def realtimeMode_menu_FeedBeesDispSet2b():
    print("  o o  ")
    print(" o   o ")
    print("  o o   o o  o o  o o  o o  o o  o o  o o  o o  o o")
    print(" o   o  Press Enter to     F E E D    H I V E      o")
    
    
    userTask = input("  o o          ")









def realtimeMode_menu_FeedBeesDispset3a(totalHoney, totalNectar, totalPopulation, beeConsumption):
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    print(" o          T O         C O N C L U D E         D A Y          F E E D        B E E H I V E         H O N E Y           o ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    print("  o                                                                                                                    o  ")
    print(" o                                                                                                                      o ")
    print("  o                    The bees are ready to sleep after a long day of guarding the nest                               o  ")
    print(" o                      It  is  time  to  feed  the  hive  with  the  honey  you  have.                                 o ")
    print("  o                 Total Honey: ", format(totalHoney, ".2f"), "                o  ")
    print(" o                     Honey Collected Today: ", totalNectar, "                                                                        o ")
    print("  o                 Total Beehive Population: ", totalPopulation, "                                                                         o  ")
    print(" o                    Total Hive Consumption: ",  beeConsumption,"                                                                  o ")
    print("  o                       P R E S S     E N T E R   T O   C O N T I N U E                                            o  ")
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  ")
    input("                                      ")
    
    
    
def realtimeMode_menu_FeedBeesDispSet3b():
    print("  o o  ")
    print(" o   o ")
    print("  o o   o o  o o  o o  o o  o o  o o  o o  o o  o o")
    print(" o   o  Press Enter to     F E E D    H I V E      o")
    
    
    userTask = input("  o o          ")


def realtimeMode_menu_FeedBees_functionality_validation(enter):
    while enter != "":
        print(" o   o  Press Enter to     F E E D    H I V E      o")
        enter = input("  o o          ")
    
    
    
    

def realtimeMode_menu_FeedBees_functionality(daysTask, totalNectar, totalHoney, totalPopulation, eatenHoney):
    
    if daysTask == "F":
        
        userInput = realtimeMode_menu_FeedBeesDispset1a(totalHoney, totalNectar, totalPopulation, eatenHoney)
        feed = realtimeMode_menu_FeedBees_functionality_validation(userInput)
        
    
    elif daysTask == "C":
        userInput = realtimeMode_menu_FeedBeesDispset2a(totalHoney, totalNectar, totalPopulation, eatenHoney)
        feed = realtimeMode_menu_FeedBees_functionality_validation(userInput)
        
        
    else:
        userInput = realtimeMode_menu_FeedBeesDispset3a(totalHoney, totalNectar, totalPopulation, eatenHoney)
        feed = realtimeMode_menu_FeedBees_functionality_validation(userInput)
        
        
        
    
    
    
    







'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userInput.py
Description: Gets the number of days and starting bee population from the user and makes sure both are within the allowed ranges. 
'''


#  GET THE NUMBER OF DAYS IN WHICH THE USER CYCLES TASKS ANS FEEDS THE HIVE
def getUserDays():
    display_instructions_userInput_DaysPopulationDispSet1()

    userDays = int(input("                                  "))
    while userDays < 7 or userDays > 28:
        print("  o o                                                                    o o   ")
        print(" o   o          The number of days must be between 7 and 28.            o   o  ")
        print("  o o              E N T E R     D A Y S      B E L O W                  o o   ")
        
        userDays = int(input("                          "))

    return userDays



# GETS USER STARTER POPULATION
def getUserBeehiveStarterPopulation(days):
    display_instructions_userInput_DaysPopulationDispSet2(days)

    userPopulation = int(input("                                              "))

    while userPopulation < 1000 or userPopulation > 100000:
        print("  o o     The population is not in the range of permitted population.    o o   ")
        print(" o   o   Choose population ( average is between 20,000 and 80,000 )     o   o  ")
        print("  o o        E N T E R     P O P U L A T I O N      B E L O W            o o   ")
        
        userPopulation = int(input("                                      "))

    return userPopulation


















'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userTaskExecution.py
Description:  
'''







def getUserTask():
    
    print("  o o  ")
    print(" o   o ")
    print("  o o   o o  o o  o o  o o  o o  o o  o o")
    print(" o   o     E N T E R         T A S K     o")
    userTask = input("  o o          ")
    
    return userTask
    
    
    




def getUserTaskValidation(taskChoice):
    
    while taskChoice != "F" and taskChoice != "f" and taskChoice != "C" and taskChoice != "c" and taskChoice != "D" and taskChoice != "d":
        
        print("   o         i n v a l i d     t a s k       ")
        taskChoice = getUserTask()
    
    return taskChoice


    
    

def userTaskIdentification(tasks, hivePopulation, day, startingPop, defenseBees):
    
    if tasks == "F":
        foragePop = userTaskIdentificationForage(hivePopulation)
        DefensePop = defenseBees
        # subtract from total pop
        createPop = hivePopulation
        
        
        return foragePop, createPop, DefensePop
        
    elif tasks == "C":
        createPop = userTaskIdentificationCreate(startingPop, day, hivePopulation)
        foragePop = 0
        DefensePop = defenseBees
        return foragePop, createPop, DefensePop
            
    else:
        DefensePop = userTaskIdentificationDefense(day, defenseBees)
        foragePop = 0
        createPop = hivePopulation
        return foragePop, createPop, DefensePop
   
def userTaskIdentificationForage(population):
    MAX_POPULATION_PERCENT_CONSTANT = .83
    MINFORAGE = 201
    MAXFORAGE = population * MAX_POPULATION_PERCENT_CONSTANT
    
    population_forage = getUserForagePopulation()
    
    while population_forage <= MINFORAGE or population_forage >= MAXFORAGE:
        print("   o         i n v a l i d     a m o u n t       ")    
        print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
        print(" o   o                                                                  o   o  ")
        print("  o o                                                                    o o   ")
        population_forage = int(input("                                    "))
    
    population_forage = foragingPopulation_accumulators(population_forage)
    return population_forage
    
       
def userTaskIdentificationCreate(startingPop, day, hivePopulation):
    MINCREATE = 101
    MAXCREATE = 1851
    population_create = getUserCreateBeesPopulation()
    while population_create <= MINCREATE or population_create > MAXCREATE:
        print("   o         i n v a l i d     a m o u n t       ")    
        print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
        print(" o   o                                                                  o   o  ")
        print("  o o                                                                    o o   ")
        population_create = int(input("                                    "))
    
    
    return hivePopulation + population_create
     
    
    
def userTaskIdentificationDefense(day, defenseBees):
    MINDEFENSE = 100
    MAXDEFENSE = 600
    population_defense = getUserDefensePopulation()
    while population_defense <= MINDEFENSE or population_defense > MAXDEFENSE:
        print("   o         i n v a l i d     a m o u n t       ")    
        print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
        print(" o   o                                                                  o   o  ")
        print("  o o                                                                    o o   ")
        population_defense = int(input("                                    "))
    
    population_defense = defensePopulation_accumulators(population_defense, day, defenseBees)
    return population_defense


   




def getUserForagePopulation():
    print("  o o                                                                o o       ")
    print(" o   o                                                              o   o      ")
    print("  o o                                                                 o o      ")
    print("   o o                                                                 o o     ")
    print("  o   o                                                               o   o    ")
    print("   o o                                                                 o o     ")
    print("  o o                                                                   o o    ")
    print(" o   o                                                                 o   o   ")
    print("  o o                                                                   o o    ")
    print("  o o                                                                    o o   ")
    print(" o   o           Enter the number of bees from your population          o   o  ")
    print("  o o            You can send less than 83% of your bees foraging.       o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    
    userInput = int(input("                                    "))
    
    return userInput
    
    
    
def getUserCreateBeesPopulation():
    print("  o o                                                                o o       ")
    print(" o   o                                                              o   o      ")
    print("  o o                                                                 o o      ")
    print("   o o                                                                 o o     ")
    print("  o   o                                                               o   o    ")
    print("   o o                                                                 o o     ")
    print("  o o                                                                   o o    ")
    print(" o   o                                                                 o   o   ")
    print("  o o                                                                   o o    ")
    print("  o o                                                                    o o   ")
    print(" o   o          Enter the number of bees you want to create             o   o  ")
    print("  o o         to your total population ( the maximum is 1851 )           o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    
    userInput = int(input("                                    "))
    
    return userInput
    



def getUserDefensePopulation():
    print("  o o                                                                o o       ")
    print(" o   o                                                              o   o      ")
    print("  o o                                                                 o o      ")
    print("   o o                                                                 o o     ")
    print("  o   o                                                               o   o    ")
    print("   o o                                                                 o o     ")
    print("  o o                                                                   o o    ")
    print(" o   o                                                                 o   o   ")
    print("  o o                                                                   o o    ")
    print("  o o                                                                    o o   ")
    print(" o   o            Enter the number of bees you want to assign           o   o  ")
    print("  o o             to defending the hive ( the maximum is 600 )           o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o         ( The average hive has a defense of 2000 bees )          o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          E N T E R     B E E    A M O U N T     B E L O W          o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    
    userInput = int(input("                                    "))
    
    return userInput
    

    
    
    
    









'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: simulation_mode#starter.py
Description:Displays the welcome screen for Beehive Prepper and introduces the player to the beehive simulation.
'''


# DISPLAYS WELCOME SCREEN    
def display_introduction_welcome_Home():
    print("  o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o  ")
    print(" o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o ")
    print("  o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o  ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o       B  E  E  H  I  V  E                P  R  E  P  P  E  R       o o  ")
    print("  o o             o o o o o o o o o o o o o o o o o o o o o o            o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o           P R E S S     E N T E R     T O     S T A R T            o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print(" o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o   ")
    print("o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o  ")
    print(" o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o   ")
    userInput = input("                                                                               ")
    return userInput

# DISPLAYS THE LITTLE TAIL END OF A HONEYCOMB TEXT DISPLAY
def display_instructions_welcome_HomeTail():
    print(" o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o   ")
    print("o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o   o  ")
    print(" o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o   ")
    


# DISPLAYS EMPTY SPACE TO BRING CLARITY IN BETWEEN HONEYCOMB TEXT DISPLAYS    
def display_instructions_welcome_HomeSpace():
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")   
    
    
    
    
    

# DISPLAYS INSTRUCTINO SET 1
def display_instructions_welcome_DispSet1():
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o             o o o o o o o o o o o o o o o o o o o o o o            o o   ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print(" o  o     Welcome to Beehive Prepper! In this simulation you can     o  o ")
    print(" o  o     manage your beehive and prepare it for winter.             o  o ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          P R E S S     E N T E R   T O   C O N T I N U E           o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    userInput = input("                                                                               ")
    return userInput   


# DISPLAYS INSTRUCTINO SET 2       
def display_instructions_welcome_DispSet2():
    
    
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o             o o o o o o o o o o o o o o o o o o o o o o            o o   ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o            Simulation mode enables you to control the              o o   ")
    print("   o o           environment and produce consistent results               o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          P R E S S     E N T E R   T O   C O N T I N U E           o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    userInput = input("                                                                               ")
    return userInput
    
# DISPLAYS INSTRUCTINO SET 3   
def display_instructions_welcome_DispSet3():

    
    
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o             o o o o o o o o o o o o o o o o o o o o o o            o o   ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o          Realtime mode is a more life-like representation          o o   ")
    print("   o o              that features many unpredictable events               o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o          P R E S S     E N T E R   T O   C O N T I N U E           o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    userInput = input("                                                                               ")
    return userInput                 
   




# DISPLAYS THE LAST BIT OF INTRODUCTION BACK TO MAIN()
def display_instructions_welcome_HomeEnd():
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o             o o o o o o o o o o o o o o o o o o o o o o            o o   ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o        Follow prompts and bee-ware of dangers along the way!       o o   ")
    print("   o o                      To begin press Enter . . .                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o             P R E S S    E N T E R   T O   S T A R T               o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    userInput = input("                                                                               ")
    return userInput                 





def display_instructions_userInput_DaysPopulationDispSet1():
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o     We need to decide how many days we will have to prepare        o o  ")
    print("  o o             before the signs of winter start emerging.             o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o              E N T E R     D A Y S      B E L O W                  o o   ")
    
def display_instructions_userInput_DaysPopulationDispSet2(days):
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o   The hive has only", days, "left before the snow starts falling.         o o   ")
    print("   o o                                                                    o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o   We must decide what our beehive population is going to bee       o o  ")
    print("  o o            ( generally between 20,000 to 80,000 bees )             o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o        E N T E R     P O P U L A T I O N      B E L O W            o o   ")
    





def display_instructions_userInput_ModeSelectorDispset3():
    
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o               ooooo     ..          ...    8    .                  o o   ")
    print("   o o             oo..:oo    :.:.       .  :.  888    ..                 o o  ")
    print("  o   o           oo.::.:oo   .:: . .:.   .      |       .               o   o ")
    print("   o o            oo:.:.:::.:.  .  .   . o    o  |   o  O                 o o  ")
    print("  o o             ooooooooo              |    |  |  /   |                o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                    Welcome to simulation mode                      o o   ")
    print("   o o                     To begin press Enter . . .                     o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o             P R E S S    E N T E R   T O   S T A R T               o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    userInput = input("                                    ")
    return userInput                 

    
    
    
    
    
    
    
    
    
def display_instructions_userInput_ModeSelectorDispset2():
    
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o               ooooo     ..          ...    8    .                  o o   ")
    print("   o o             oo..:oo    :.:.       .  :.  888    ..                 o o  ")
    print("  o   o           oo.::.:oo   .:: . .:.   .      |       .               o   o ")
    print("   o o            oo:.:.:::.:.  .  .   . o    o  |   o  O                 o o  ")
    print("  o o             ooooooooo              |    |  |  /   |                o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    print("  o o                                                                    o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                    Welcome to Beehive Prepper                      o o   ")
    print("   o o                     To begin press Enter . . .                     o o  ")
    print("  o   o                                                                  o   o ")
    print("   o o                                                                    o o  ")
    print("  o o             P R E S S    E N T E R   T O   S T A R T               o o   ")
    print(" o   o                                                                  o   o  ")
    print("  o o                                                                    o o   ")
    userInput = input("                                    ")
    return userInput                 






def display_instructions_userInput_ModeSelector_functionality_validation(userInput):
    
    while userInput != "":
        
        userInput = input("  o o             P R E S S    E N T E R   T O   S T A R T               o o   ")
    
    
    
# VALIDATES USER INPUT AND LOOPS UNTIL CORRECT KEYPRESS
def display_welcome_functionality_validation(dataInput):    
    while dataInput != "":
        dataInput = input("  o o             P R E S S    E N T E R   T O   S T A R T               o o   ")      
    
    return dataInput
    



# ORCHESTRATES TEXT AND DISPLAYS ALL THE INSTRUCTINO SETS IN SEQUENCIAL FASHION  
def display_welcome_functionality():
    userChoice = "NotEnter"
    userChoice = display_introduction_welcome_Home()
    userChoice = display_welcome_functionality_validation(userChoice)
    
    
    
    while userChoice == "":
        userChoice = "NotEnter"
        display_instructions_welcome_HomeSpace()
        userChoice = display_instructions_welcome_DispSet1()
        userChoice = display_welcome_functionality_validation(userChoice)
        display_instructions_welcome_HomeSpace()
        display_instructions_welcome_HomeTail()
        
        
        if userChoice == "":
            userChoice = "NotEnter"
            display_instructions_welcome_HomeSpace()
            userChoice = display_instructions_welcome_DispSet2()
            userChoice = display_welcome_functionality_validation(userChoice)
            display_instructions_welcome_HomeSpace()
            display_instructions_welcome_HomeTail()
            
        
        
            if userChoice == "":
                userChoice = "NotEnter"
                display_instructions_welcome_HomeSpace()
                userChoice = display_instructions_welcome_DispSet3()
                userChoice = display_welcome_functionality_validation(userChoice)
                display_instructions_welcome_HomeSpace()
                display_instructions_welcome_HomeTail()
                
        
        
                if userChoice == "":
                    userChoice = "NotEnter"
                    display_instructions_welcome_HomeSpace()
                    userChoice = display_instructions_welcome_HomeEnd()
                    userChoice = display_welcome_functionality_validation(userChoice)
                    display_instructions_welcome_HomeSpace()
                    display_instructions_welcome_HomeTail()
                    display_instructions_welcome_HomeSpace()
                    display_instructions_welcome_HomeSpace()
                    userChoice = "NotEnter"
        
        
    
    
    
def display_userInput_functionality():
    
    display_instructions_welcome_HomeSpace()
    days = getUserDays()
    display_instructions_welcome_HomeSpace()
    population = getUserBeehiveStarterPopulation(days)
    display_instructions_welcome_HomeSpace()
    
    userEnter = display_instructions_userInput_ModeSelectorDispset2()
    display_instructions_userInput_ModeSelector_functionality_validation(userEnter)
    return days, population
    
    
    

    
    
    







    
    
    
    
    
    
    
        
        
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    