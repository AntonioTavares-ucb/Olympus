# Hermes is the internet manager for Olympus, it manages wifi connection, download and upload speed, pings, etc.

from os import system as say 
from os import kill as end
import Header
#________________________________________________________________________________________________________________________

def getOperation():
    return input('Operation:\n1) Connect \n2) Status \n3) Restart \n4) Disable \n5) Back\n')

def runOperation(Operation):
    match Operation:
        case '1':
            say('clear')
            print('\nConnecting\n')
            Header.HermesConnect()

        case '2':
            say('clear')
            print('\nChecking status\n')
            Header.HermesStatus()
            
        case '3':
            say('clear')
            print('\nRestarting\n')
            Header.HermesRestart()
        
        case '4':
            say('clear')
            print('\nDisabling\n')
            Header.HermesDisable()
            
        case _:
            say('clear')
            print('Please select a valid operation.\n')

    return 0

#________________________________________________________________________________________________________________________

operation = ''
while operation != '5':
    operation = getOperation()

    if operation == '5':
        end(0, 0)
    else:
        runOperation(operation)



        





