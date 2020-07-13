import ProjGOVariables
import ProjGOFunctions
print('Welcome to the CSGO Round Calculator')
ProjGOVariables.CURRENT_SIDE = input('To begin please choose the starting side (T or CT): ').strip()

ProjGOVariables.GAME_ACTIVE = True
while ProjGOVariables.GAME_ACTIVE == True:
    if ProjGOVariables.CURRENT_ROUND == 31 or ProjGOVariables.PLAYER_TEAM_VICTORIES == 16 or ProjGOVariables.ENEMY_TEAM_VICTORIES == 16:
        print('GAME ENDED')
        ProjGOVariables.GAME_ACTIVE = False
    else:
        print('You currently have $' + str(ProjGOVariables.PLAYER_CURRENT_MONEY))
        enteredInput = input('Enter "B" to go into the buy menu or "GO" to progres to next round: ').strip()
        if enteredInput == 'B':
            ProjGOFunctions.openBuyMenu()
        elif enteredInput == 'GO':
            ProjGOFunctions.postRoundCalculations()
            #ProjGOVariables.ENEMY_TEAM_VICTORIES += 1
            #print('KEEP GOING')

