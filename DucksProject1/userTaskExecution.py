'''
Name: Gideon Gaudette, Gavin Goodwin, and Imanol Gonzalez-Hernandez
Program name: userTaskExecution.py
Description:  
'''
from DucksProject1 import welcome_introduction
from DucksProject1 import userInput
from DucksProject1 import realtimeMode


def getUserTask():
    
    print("  o o  ")
    print(" o   o ")
    print("  o o   o o  o o  o o  o o  o o  o o  o o")
    print(" o   o     E N T E R         T A S K     o")
    userTask = input("  o o                ")
    
    return userTask
    
    
    




def getUserTaskValidation(taskChoice):
    
    while taskChoice != "F" and taskChoice != "f" and taskChoice != "C" and taskChoice != "c" and taskChoice != "D" and taskChoice != "d":
        
        print("   o         i n v a l i d     t a s k       ")
        taskChoice = getUserTask()
    
    return taskChoice
