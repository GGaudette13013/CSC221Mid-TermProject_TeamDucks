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

        
    
    
    
    
    
    
    
    
    
    
    
    
    
