'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: simulation_mode#starter.py
Description:  
'''

from DucksProject1 import userInput
from DucksProject1 import userTaskExecution


def realtimeMode_menu(honeyTotal, nectarProduction, totalBeehivePopulation, totalBeesForageing, TotalBeeDefenceCount):
    print("  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o  o o   ")
    print(" o     HONEY PRODUCION (KG): ", honeyTotal, "          NECTAR PRODUCTION: ", nectarProduction, "            BEEHIVE POPULATION: ", totalBeehivePopulation, "         o  ")
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
    print("                      kills beehive population by 70% and all defense bees are killed ")
    print("\t")
    print("\t")
    
    

    
def realtimeMode_menu_eventDisplay_BlackBear():
    print("   (((    ooooo  / \__ / \     .. .              ")
    print("   @@@ ) oo .:oo( >___=  ) ...::.::.. .          ")
    print("  {   @ oo.  .:oo /* *\   ) ::.:.:.. .. .        ")
    print("  |    \oo:. .:.:  ___    )  .. :.:.  .          ")
    print("  |     ooooooooo::.::.  .. . .::.  ..           ")
    print("  {     EVENT STATUS: Black bear!!                 ")
    print("                      destroys beehive defense by 50% and honey production by 50%")
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
    print("        oo:.:.:::.:.  .  . 0 . o    o  |   o  O        ")
    print("        ooooooooo          |   |    |  |  /   |        ")
    print("        EVENT STATUS: Normal                           ")
    print("                      nothing could be better!         ")
    print("\t")
    print("\t")



    
    
    






def realtimeMode_menu_operations():
        # Forage
    print("  o o  o o  o o  o o  o o  o o  ")
    print(" o  FORAGE        Get nectar  o ")
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
    
    
    
    
    
    
    
    







'''
realtimeMode_menu_eventDisplay_Hornets()
realtimeMode_menu_eventDisplay_BlackBear()
realtimeMode_menu_eventDisplay_Rainy()
realtimeMode_menu_eventDisplay_Drought()
realtimeMode_menu_eventDisplay_Normal()
realtimeMode_menu_eventDisplay_Beetle()
'''
