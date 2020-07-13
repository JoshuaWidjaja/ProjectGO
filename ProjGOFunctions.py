import ProjGOVariables
def openBuyMenu():
    print('Your current money = ' + str(ProjGOVariables.PLAYER_CURRENT_MONEY))
    selectMenu = input('Select which menu to enter, enter GO, or enter QUIT: 1 - Pistols, 2 - Heavy, 3 - SMG, 4 - Rifles, 5 - Grenades, 6 - Equipment: ').strip()
    if selectMenu == '1':
        openPistolsMenu(ProjGOVariables.CURRENT_SIDE)
    elif selectMenu == '2':
        openHeavyMenu(ProjGOVariables.CURRENT_SIDE)
    elif selectMenu == '3':
        openSMGMenu(ProjGOVariables.CURRENT_SIDE)
    elif selectMenu == '4':
        openRifleMenu(ProjGOVariables.CURRENT_SIDE)
    elif selectMenu == '5':
        openGrenadeMenu(ProjGOVariables.CURRENT_SIDE)
    elif selectMenu == '6':
        openEquipmentMenu(ProjGOVariables.CURRENT_SIDE)
    elif selectMenu == 'GO':
        postRoundCalculations()
    elif selectMenu == 'QUIT':
        ProjGOVariables.ENEMY_TEAM_VICTORIES == 16

def postRoundCalculations():
    print('Round Ended, please answer the following (Y/N) or with integers: ')
    repeatQuestion = True
    while repeatQuestion == True:
        roundWinAnswer = input('Did you win the round? (Y/N) ').strip()
        if roundWinAnswer == 'Y' or roundWinAnswer == 'N':
            repeatQuestion = False
    _winLossCalculation(roundWinAnswer, ProjGOVariables.CURRENT_SIDE)

    validInputs = [0, 1, 2, 3, 4, 5]
    totalKills = int(input('How many kills did you get during the round? ').strip())
    while totalKills not in validInputs:
        totalKills = int(input('How many kills did you get during the round? ').strip())
    if totalKills != 0:
        killCounter = int(totalKills)
        nonRifleCheck = input('Did you use a shotgun, sniper, CZ, or any SMG except the P90 to get kills this round? (Y/N) ').strip()
        if nonRifleCheck == 'Y': #add knife killss later
            shotgunKills = input('Of your total kills how many were kills with a shotgun (Nova, Sawed Off, MAG-7, or XM1014)? ').strip()
            killCounter -= int(shotgunKills)
            if killCounter > 0:
                sniperKills = input('Of your total kills how many were kills with a sniper or CZ?(AWP, CZ, G3GS1, SCAR-20)? ').strip()
                killCounter -= int(sniperKills)
                if killCounter > 0:
                    smgKills = input('Of your total kills how many were kills with a budget SMG (MAC-10, MP9, MP7, PP-Bizon)? ').strip()
                    killCounter -= int(smgKills)
                    rifleKills = killCounter
                    _killProfitCalculation(nonRifleCheck, totalKills, shotgunKills, sniperKills, smgKills, rifleKills)
                elif killCounter == 0:
                    _killProfitCalculation(nonRifleCheck, totalKills, shotgunKills, sniperKills, smgKills = 0, rifleKills = 0)
            elif killCounter == 0:
                _killProfitCalculation(nonRifleCheck, totalKills, shotgunKills, sniperKills = 0, smgKills = 0, rifleKills = 0)
        elif nonRifleCheck == 'N':
            _killProfitCalculation(nonRifleCheck, totalKills, heavyKills = 0, sniperKills = 0 , smgKills = 0, rifleKills = 0)
    print(ProjGOVariables.PLAYER_CURRENT_MONEY)




def openPistolsMenu(currentSide):
    menuOpen = True
    while menuOpen == True:
        pistolPriceDict = {'1': 200, '2': 500, '3': 300, '4':500, '5':700}
        if currentSide == 'CT':
            pistolNameDict = {'1': 'USP-S', '2': 'Dual Berettas', '3': 'P250', '4': 'Five-Seven', '5': 'Desert Eagle'}
            #priceDict = {'1': 200, '2': 500, '3': 300, '4':500, '5':700}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - USP-S/$200, 2 - Dual Berettas/$500, 3 - P250/$300, 4 - Five-Seven/$500, 5 - Desert Eagle/$700: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
                #openBuyMenu()
            else:
                _deductPlayerBalance(selectedItem, pistolNameDict, pistolPriceDict, menuOpen)
        elif currentSide == 'T':
            pistolNameDict = {'1': 'Glock', '2' : 'Duel Berettas', '3' : 'P250', '4' : 'Tec-9', '5': 'Desert Eagle'}
            #priceDict = {'1': 200, '2': 500, '3': 300, '4': 500, '5': 700}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - Glock/$200, 2 - Dual Berettas/$500, 3 - P250/$300, 4 - Tec-9/$500, 5 - DesertEagle/$700: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, pistolNameDict, pistolPriceDict, menuOpen)
    openBuyMenu()

def openHeavyMenu(currentSide):
    menuOpen = True
    while menuOpen == True:
        heavyPriceDict = {'1': 1200, '2': 2000, '3': 0, '4': 1700, '5': 4200}
        if currentSide == 'CT':
            updatedPrice = {'3': 1300}
            heavyPriceDict.update(updatedPrice)
            heavyNameDict = {'1': 'Nova', '2': 'XM1014', '3': 'MAG-7', '4': 'Negev', '5': 'M249'}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - Nova/$1200, 2 - XM1014/$2000, 3 - MAG-7/$1300, 4 - Negev/$1700, 5 - M249/$4200: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, heavyNameDict, heavyPriceDict, menuOpen)
        elif currentSide == 'T':
            updatedPrice = {'3': 1100}
            heavyPriceDict.update(updatedPrice)
            heavyNameDict = {'1': 'Nova', '2': 'XM1014', '3': 'Sawed-Off', '4': 'Negev', '5': 'M249'}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - Nova/$1200, 2 - XM1014/$2000, 3 - Sawed-Off/$1100, 4 - Negev/$1700, 5 - M249/$4200: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, heavyNameDict, heavyPriceDict, menuOpen)
    openBuyMenu()


def openSMGMenu(currentSide):
    menuOpen = True
    while menuOpen == True:
        smgPriceDict = {'1': 1000, '2': 1200, '3': 1700, '4': 2350, '5': 1400}
        if currentSide == 'CT':
            smgNameDict = {'1': 'MP9', '2': 'UMP-45', '3': 'MP7', '4': 'P90', '5': 'PP-Bizon'}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - MP9/$1000, 2 - UMP-45/$1200, 3 - MP7/$1500, 4 - P90/$2350, 5 - PP-Bizon/$1400: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, smgNameDict, smgPriceDict, menuOpen)
        elif currentSide == 'T':
            smgNameDict = {'1': 'MAC-10', '2': 'UMP-45', '3': 'MP7', '4': 'P90', '5': 'PP-Bizon'}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - MP9/$1000, 2 - UMP-45/$1200, 3 - MP7/$1500, 4 - P90/$2350, 5 - PP-Bizon/$1400: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, smgNameDict, smgPriceDict, menuOpen)
    openBuyMenu()

def openRifleMenu(currentSide):
    menuOpen = True
    while menuOpen == True:
        if currentSide == 'CT':
            rifleNameDict = {'1': 'FAMAS', '2': 'M4A1-S', '3': 'M4A4', '4': 'SSG-18', '5':'AUG', '6':'AWP', '7' : 'SCAR-20'}
            riflePriceDict = {'1': 2250, '2': 3100, '3': 3200, '4': 1700, '5': 3300, '6': 4750, '7': 5000}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - FAMAS/$2250, 2 - M4A1-S/$3100, 3 - M4A$/$3200, 4 - SSG-18/$1700, 5 - AUG/$3300, 6 - AWP/$4750, 7 - SCAR-20/$5000: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, rifleNameDict, riflePriceDict, menuOpen)
        elif currentSide == 'T':
            rifleNameDict = {'1': 'Galil', '2': 'AK47', '3': 'SSG-18', '4': 'SG-553', '5': 'AWP', '6': 'G3GS1'}
            riflePriceDict = {'1': 2000, '2': 2700, '3': 1700, '4': 2800, '5': 4750, '6': 5000}
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - Galil/$2000, 2 - AK47/$2700, 3 - SSG-18/$1700, 4 - SG-553/$2800, 5 - AWP/$4750, 6 - G3GS1/$5000: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, rifleNameDict, riflePriceDict, menuOpen)
    openBuyMenu()

def openGrenadeMenu(currentSide):
    menuOpen = True
    while menuOpen == True:
        grenadePriceDict = {'1': 0, '2': 50, '3': 200, '4': 300, '5': 300}
        grenadeNameDict = {'1': '', '2': 'Decoy Grenade', '3': 'Flashbang', '4': 'HE Grenade', '5': 'Smoke Grenade'}
        if currentSide == 'CT':
            updatedPrice, updatedName = {'1', 600}, {'1', 'Incindiary Grenade'}
            grenadePriceDict.update(updatedPrice)
            grenadeNameDict.update(updatedName)
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - Incindiary Grenade/$600, 2 - Decoy Grenade/$50, 3 - Flashbang/$200, 4 - HE Grenade/$300, 5 - Smoke Grenade/$300: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, grenadeNameDict, grenadePriceDict, menuOpen)
        elif currentSide == 'T':
            updatedPrice, updatedName = {'1', 400}, {'1', 'Molotov'}
            grenadePriceDict.update(updatedPrice)
            grenadeNameDict.update(updatedName)
            selectedItem = input('Select which gun to purchase (or enter "E" to go back): 1 - Molotov/$400, 2 - Decoy Grenade/$50, 3 - Flashbang/$200, 4 - HE Grenade/$300, 5 - Smoke Grenade/$300: ').strip()
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, grenadeNameDict, grenadePriceDict, menuOpen)
    openBuyMenu()

def openEquipmentMenu(currentSide):
    menuOpen = True
    while menuOpen == True:
        equipmentPriceDict = {'1': 650, '2': 1000, '3': 200}
        equipmentNameDict = {'1': 'Kevlar Vest', '2': 'Kevlar Vest and Helmet', '3': 'Zeus'}
        if currentSide == 'CT':
            equipmentPriceDict['4'] = 400 #add into dictionary
            equipmentNameDict['4'] = 'Defuse Kit'
            selectedItem = input('Select which equipment to purchase (or enter "E" to go back): 1 - Kevlar Vest/$650, 2 - Kevlar Vest and Helmet/$1000, 3 - Zeus/$200, 4 - Defuse Kit/$400: ')
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool()
            else:
                _deductPlayerBalance(selectedItem, equipmentNameDict, equipmentPriceDict, menuOpen)        
        elif currentSide == 'T':
            selectedItem = input('Select which equipment to purchase (or enter "E" to go back): 1 - Kevlar Vest/$650, 2 - Kevlar Vest and Helmet/$1000, 3 - Zeus/$200: ')
            if selectedItem == 'E':
                menuOpen = _changeMenuOpenBool
            else:
                _deductPlayerBalance(selectedItem, equipmentNameDict, equipmentPriceDict, menuOpen)
    openBuyMenu()



def _deductPlayerBalance(selectedItem: str, nameDict: dict, priceDict: dict, menuOpen: bool):
    if selectedItem in priceDict:
        if ProjGOVariables.PLAYER_CURRENT_MONEY - priceDict[selectedItem] < 0:
            print('You don\'t have enough money! Current Money = ' + str(ProjGOVariables.PLAYER_CURRENT_MONEY))
        else:
            ProjGOVariables.PLAYER_CURRENT_MONEY -= priceDict[selectedItem]
            print('You purchased ' + nameDict[selectedItem] + '! Current Money = ' + str(ProjGOVariables.PLAYER_CURRENT_MONEY))
    else:
        print('User input error, try again')

def _changeMenuOpenBool():
    return False
        

def _winLossCalculation(winRoundAnswer : str, currentSide : str):
    ProjGOVariables.CURRENT_ROUND += 1
    if winRoundAnswer == 'Y':
        ProjGOVariables.PLAYER_CURRENT_MONEY += ProjGOVariables.BASE_WIN_EARNINGS
        ProjGOVariables.PLAYER_TEAM_VICTORIES += 1
        ProjGOVariables.LOSS_STREAK = 0
    elif winRoundAnswer == 'N':
        ProjGOVariables.PLAYER_CURRENT_MONEY += ProjGOVariables.BASE_LOSS_EARNINGS
        ProjGOVariables.PLAYER_CURRENT_MONEY += ProjGOVariables.LOSS_STREAK * ProjGOVariables.LOSS_STREAK_BONUS
        if currentSide == 'T':
            bombPlanted = input('Did your team plant the bomb? (Y/N) ')
            if bombPlanted == 'Y':
                ProjGOVariables.PLAYER_CURRENT_MONEY += ProjGOVariables.BOMB_PLANT_BONUS
                beingPlanter = input('Were you the bomb planter? (Y/N) ')
                if beingPlanter == 'Y':
                    ProjGOVariables.PLAYER_CURRENT_MONEY += ProjGOVariables.BOMB_PLANTER_BONUS
        if ProjGOVariables.LOSS_STREAK < 4:
            ProjGOVariables.LOSS_STREAK += 1
        else:
            pass
        ProjGOVariables.ENEMY_TEAM_VICTORIES += 1
    else:
        pass


def _killProfitCalculation(haveNonRifle: str, totalKills: int, heavyKills : int, sniperKills: int, smgKills: int, rifleKills: int):
    if haveNonRifle == 'N':
        ProjGOVariables.PLAYER_CURRENT_MONEY += totalKills * ProjGOVariables.KILL_BONUS_NORM
    else:
        ProjGOVariables.PLAYER_CURRENT_MONEY += heavyKills * ProjGOVariables.KILL_BONUS_SHOTGUN
        ProjGOVariables.PLAYER_CURRENT_MONEY += sniperKills * ProjGOVariables.KILL_BONUS_SNIPER
        ProjGOVariables.PLAYER_CURRENT_MONEY += smgKills * ProjGOVariables.KILL_BONUS_SMG
        ProjGOVariables.PLAYER_CURRENT_MONEY += rifleKills * ProjGOVariables.KILL_BONUS_NORM
