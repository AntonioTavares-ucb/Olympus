# Hephaestus is the version manager for Olympus, with it the user may Set up, Update or Remove Olympus frm their system.

from os import system as say 
from os import kill as end
import Header
#________________________________________________________________________________________________________________________

def getOperation():
    return input('Operation:\n1) Setup\n2) Update\n3) Remove\n4) Back\n')

def runOperation(Operation):
    match Operation:
        case '1':
            say('clear')
            print('\nBeginning setup\n')
            Header.HephaestusSetup()
            
        case '2':
            say('clear')
            print('\nBeginning update\n')
            Header.HephaestusUpdate()
            
        case '3':
            say('clear')
            print('\nBeginning removal\n')
            Header.HephaestusRemove()
            
        case _:
            say('clear')
            print('Please select a valid operation.\n')

    return 0

#________________________________________________________________________________________________________________________

operation = ''
while operation != '4':
    operation = getOperation()

    if operation == '4':
        end(0, 0)
    else:
        runOperation(operation)



        





