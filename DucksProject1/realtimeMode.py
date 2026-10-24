'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: simulation_mode#starter.py
Description:  
'''
from DucksProject1 import userInput
from DucksProject1 import userTaskExecution

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
realtimeMode_menu_eventDisplay_Hornets()
realtimeMode_menu_eventDisplay_BlackBear()
realtimeMode_menu_eventDisplay_Rainy()
realtimeMode_menu_eventDisplay_Drought()
realtimeMode_menu_eventDisplay_Normal()
realtimeMode_menu_eventDisplay_Beetle()
'''
