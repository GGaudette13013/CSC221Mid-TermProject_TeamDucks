'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: envEvent.py
Description:  
'''
from random import randint






def event_randomizer():
    
    event = randint(1,34)
    
    return event
    
    #IF YOU SEE THIS IT MEANS GAVIN FUNCTION USING GIT



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
        condition = "pesicides"
    
    
    
    else:
        condition = "normal"
        
        
    return condition
    




#def event_handler(eventIdentity):
    
    
#    if eventIdentity == "drought":
        
    
    
    
    
    
    
    
    
    
    
    
    
    
