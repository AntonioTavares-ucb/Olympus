from os import system as say

def isNumber(suspect):
    if suspect == ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0'):
        return True
    else:
        return False
    
#____________________________________________________________________________________________________________________
    

def HephaestusSetup():
    if input('It is highly recomended to \'sudo apt-get update\' before setting up Olympus, would you like to? (Y/n)') == ('' or 'y' or 'Y'):
        say('sudo apt-get update')
    say('pip install -r requirements.txt')
    return 0

# Maybe set up the update so that it doesn't change Haephestus, check if it's possible to clone a single file, if so then replace all other tools with the updated version and leave Haephestus alone. If this is done Haephestus will either need to be perfect, simple or manualy updated.
def HephaestusUpdate():
    if input('It is highly recomended to \'sudo apt-get update\' before updating Olympus, would you like to? (Y/n)') == ('' or 'y' or 'Y'):
        say('sudo apt-get update')
    say('git clone https://github.com/AntonioTavares-ucb/Olympus')
    return 0

def HephaestusRemove():
    if input('\nYou are about to delete Olympus from this system\n\033[91mAre you sure you want to continue? (y/N)\033[0m') == ('y' or 'Y'):
        say('sudo rm -r /../Olympus')
    return 0


#____________________________________________________________________________________________________________________

def HermesConnect():
    return 0

def HermesStatus():
    return 0

def HermesRestart():
    return 0

def HermesDisable():
    return 0