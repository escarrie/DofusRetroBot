from pyautogui import *
import pyautogui
import time
import keyboard
import random
import _thread
import winsound
import json

# Variable d'environnement
process =   {
    'position':     ['0', '0'],
    'level':        0,
    'isStop':       False,
    'comeFrome':    'none'
}

combat = {
    'pass':'space',
    'sort1':  '&',
    'sort2': 'é',
    'sort3': '"'
}

screen  =   {
    'start':    [0,     364],
    'end':      [1917,  1817],
    'append':   [1917 - 0, 1817 - 364],
    'center':   [(1917 / 2), ((1817 - 364) / 2) + 364],
    'pods':     [1022,  1544],
    'levelup':  [1006,  993],
    'combat':   [[81, 74, 60], [96, 190, 52]]
}

metier = {
    'bucheron': {
        'Frêne':        0,
        'Chataigné':    10,
        'Noyer':        20
    }
}

stats   =   {
    'changeMap':            0,
    'click':                0,
    'ressourceCollecter':   0,
    'levelup':              0,
    'finishCause':          'Ne rentre pas dans le process'
}

map     = {
    '2,-23': {
        'porte': {
            'disponible': ['haut', 'gauche'],
            'haut':     [620,   403],
            'droite':   [1856,  892],
            'gauche':   [69,    1100]
        },
        'ressources': [
            ['Nombre de ressource:', 6],
            ['Frêne', 1574, 1281,   [174, 149, 6]],
            ['Frêne', 1711, 580,    [174, 149, 6]],
            ['Frêne', 680,  1314,   [174, 149, 6]],
            ['Frêne', 1160, 583,    [174, 149, 6]],
            ['Frêne', 542,  757,    [174, 149, 6]],
            ['Frêne', 270,  757,    [174, 149, 6]]
        ]
    },
    '2,-24': {
        'porte': {
            'disponible': ['bas', 'haut', 'droite', 'gauche'],
            'haut':     [1169,  408],
            'bas':      [616,   1447],
            'droite':   [1857,  1028],
            'gauche':   [70,    889],
            'commentaire': 'Ajout de ressource au level up disponible'
        },
        'ressources': [
            ['Nombre de ressource:', 8],
            ['Chêne', 209, 1272, [116, 121, 42]],
            ['Chêne', 273, 1304, [111, 119, 45]],
            ['Noyer', 751, 932, [188, 164, 29]],
            ['Noyer', 684, 964, [153, 138, 21]],
            ['Chataigné', 204, 651, [206, 121, 36]],
            ['Chataigné', 270, 618, [206, 121, 36]],
            ['Frêne', 1365, 617,    [174, 149, 6]],
            ['Frêne', 1431, 650,    [174, 149, 6]]
        ]
    },
    '2,-25': {
        'porte': {
            'disponible': ['bas', 'droite', 'gauche'],
            'bas':      [1169,  1452],
            'droite':   [1852,  822],
            'haut':     [753,   408],
            'gauche':   [72,    1172]
        },
        'ressources': [
            ['Nombre de ressource:', 14],
            ['Chataigné', 1709, 1349,   [206, 121, 36]],
            ['Chataigné', 1091, 1244,   [206, 121, 36]],
            ['Chataigné', 1437, 931,    [206, 121, 36]],
            ['Chataigné', 682, 966,     [206, 121, 36]],
            ['Chataigné', 476, 1212,    [181, 138, 28]],
            ['Chataigné', 340, 512,     [206, 121, 36]],
            ['Chataigné', 955, 547,     [206, 121, 36]],
            ['Chataigné', 1506, 548,    [206, 121, 36]],
            ['Frêne', 1573, 1069,   [172, 147, 6]],
            ['Frêne', 1021, 930,    [174, 149, 6]],
            ['Frêne', 1090, 684,    [174, 149, 6]],
            ['Frêne', 1641, 615,    [174, 149, 6]],
            ['Frêne', 203, 929,      [174, 149, 6]],
            ['Frêne', 131, 546,     [174, 149, 6]]
        ]
    },
    '3,-24': {
        'porte': {
            'disponible': ['gauche'],
            'gauche':       [67,  1043]
        },
        'ressources': [
            ['Nombre de ressource:', 10],
            ['Noyer', 617, 1210,    [167, 145, 25]],
            ['Noyer', 681, 1173,    [156, 136, 24]],
            ['Noyer', 548, 1174,    [156, 136, 24]],
            ['Noyer', 615, 1140,    [156, 136, 24]],
            ['Chataigné', 1301, 583,    [205, 120, 35]],
            ['Chataigné', 1234, 547,    [197, 118, 30]],
            ['Chataigné', 1370, 548,    [203, 120, 34]],
            ['Chataigné', 1300, 511,    [206, 121, 36]],
            ['Frêne', 684, 613,     [177, 155, 5]],
            ['Frêne', 749, 581,     [174, 149, 6]]
        ]
    },
    '3,-25': {
        'porte': {
            'disponible': ['bas', 'gauche'],
            'bas':      [621, 1452],
            'gauche':   [74, 822],
            'haut':     [1035, 406],
            'droite':   [1856, 1102]
        },
        'ressources': [
            ['Nombre de ressource:', 14],
            ['Chataigné', 1027, 1419,   [206, 121, 36]],
            ['Chataigné', 1505, 1383,   [206, 121, 36]],
            ['Chataigné', 751,  1209,   [206, 121, 36]],
            ['Chataigné', 1711, 930,    [206, 121, 36]],
            ['Chataigné', 1301, 720,    [206, 121, 36]],
            ['Chataigné', 202,  1280,   [206, 121, 36]],
            ['Chataigné', 610,  512,    [206, 121, 36]],
            ['Frêne', 1161, 1068,   [168, 145, 7]],
            ['Frêne', 612,  927,    [167, 149, 5]],
            ['Frêne', 269,  549,    [168, 137, 4]],
            ['Frêne', 63,   440,    [174, 149, 6]],
            ['Frêne', 1433, 440,    [174, 149, 6]],
            ['Frêne', 1711, 580,    [174, 149, 6]]
        ]
    },
    '1,-23': {
        'porte': {
            'disponible': ['droite', 'haut'],
            'gauche':   [80,    892],
            'haut':     [1024,  408],
            'droite':   [1849,  1106]
        },
        'ressources': [
            ['Nombre de ressource:', 9],
            ['Chataigné', 953,  1174,   [206, 121, 36]],
            ['Chataigné', 1365, 617,    [206, 121, 36]],
            ['Frêne', 615,  1139,   [174, 149, 6]],
            ['Frêne', 1642, 1384,   [174, 149, 6]],
            ['Frêne', 1709, 1000,   [174, 149, 6]],
            ['Frêne', 1637, 753,    [174, 149, 6]],
            ['Frêne', 1574, 509,    [174, 149, 5]],
            ['Frêne', 542,  475,    [173, 150, 9]],
            ['Frêne', 1778, 470,    [249, 194, 11]]
        ]
    },
    '1,-24': {
        'porte': {
            'disponible': ['droite', 'bas', 'haut'],
            'bas':      [1034,  1449],
            'gauche':   [69,    960],
            'haut':     [894,   403],
            'droite':   [1899,  891]
        },
        'ressources': [
            ['Nombre de ressource:', 9],
            ['Chataigné', 1571, 1348,   [206, 121, 36]],
            ['Chataigné', 1368, 825,    [206, 121, 36]],
            ['Chataigné', 1711, 580,    [206, 121, 36]],
            ['Frêne', 1232, 1243,   [174, 149, 6]],
            ['Frêne', 544,  963,    [174, 149, 6]],
            ['Frêne', 958,  827,    [174, 149, 6]],
            ['Frêne', 1501, 894,    [174, 149, 6]],
            ['Frêne', 133,  615,    [174, 149, 6]],
            ['Frêne', 271,  545,    [174, 149, 6]],
            ['Frêne', 63,   505,    [249, 194, 11]],
            ['Frêne', 684,  615,    [174, 149, 6]],
            ['Frêne', 1164, 572,    [214, 182, 63]]
        ]
    },
    '1,-25': {
        'porte': {
            'disponible': ['droite', 'bas'],
            'bas':      [896,   1449],
            'gauche':   [64,    1104],
            'haut':     [1302,  405],
            'droite':   [1851,  1172]
        },
        'ressources': [
            ['Nombre de ressource:', 14],
            ['Chataigné', 1365, 1315,   [206, 121, 36]],
            ['Chataigné', 681,  1176,   [206, 121, 36]],
            ['Chataigné', 1026, 861,    [206, 121, 36]],
            ['Chataigné', 1708, 930,    [206, 121, 36]],
            ['Chataigné', 1641, 546,    [206, 121, 36]],
            ['Frêne', 1708, 1420,   [174, 149, 6]],
            ['Frêne', 888,  1136,   [174, 149, 6]],
            ['Frêne', 884,  648,    [174, 149, 6]]
        ]
    }
}


# FONCTION UTILS
def printStats():
    os.system('cls')
    print('-----    STATISTIQUES    -----')
    print('Changement de map: ' + str(stats['changeMap']))
    print('nombre de click: ' + str(stats['click']))
    print('Ressources collecté: ' + str(stats['ressourceCollecter']))
    print('Niveau obtenu: ' + str(stats['levelup']))
    print('Finish chause: ' + stats['finishCause'])


def sleep(secondes):
    time.sleep(secondes)


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def getPositionStart():
    flag = False
    start = input('Entrée votre position ( ex: "0,-24" ): ')
    process['position'] = start.split(',')
    if not RepresentsInt(process['position'][0]):
        flag = True
    if not RepresentsInt(process['position'][1]):
        flag = True
    if flag:
        print('Erreur dans la map suivez l\'exemple!')
        exit()


def verifKeyStopPress(nothing):
    while True:
        if (keyboard.is_pressed('q') or (keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'))):
            stats['finishCause'] = 'Interrompu par l\'utilisateur'
            printStats()
            exit()
        if (process['isStop'] == True):
            exit()
    return False


def getPicture():
    pic = pyautogui.screenshot(region=(screen['start'][0], screen['start'][1], screen['append'][0], screen['append'][1]))
    return pic


def verifPods():
    pic = pyautogui.screenshot(region=(screen['start'][0], screen['start'][1], screen['end'][0], screen['end'][1]))
    r, g, b = pic.getpixel((1022 - screen['start'][0], 1545 - screen['start'][1]))
    if not (r in range(75, 85) or g in range(70, 80) or b in range(55, 65)):
        pic = pyautogui.screenshot(region=(screen['start'][0], screen['start'][1], screen['end'][0], screen['end'][1]))
        r, g, b = pic.getpixel(((1006 - 0), (993 - 364)))
        if (r == 255 and g == 97 and b == 0):
            pyautogui.press('enter')
            stats['levelup'] = stats['levelup'] + 1
            print('-----    LEVEL UP: ' + str(process['level']) + '    -----')
            return True
        print('/!\\ ----- INVENTAIRE PLEIN ----- /!\\')
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        for i in range(1, 5):
            winsound.Beep(frequency, duration)
            sleep(0.5)
        stats['finishCause'] = 'Inventaire plein'
        printStats()
        process['isStop'] = True
    else:
        return True


def checkChangeMapFinish():
    print('Changement de map en cours')
    pic = getPicture()
    br, bg, bb = pic.getpixel((screen['center'][0], screen['center'][1]))
    while (True and not keyboard.is_pressed('right')):
        pic = getPicture()
        nr, ng, nb = pic.getpixel((screen['center'][0], screen['center'][1]))
        if (br != nr or bg != ng or bb != nb):
            break
    bn = bg = bb = 0
    print('Chargement en cours')
    while (True and not keyboard.is_pressed('right')):
        pic = getPicture()
        nr, ng, nb = pic.getpixel((screen['center'][0], screen['center'][1]))
        if (br != nr or bg != ng or bb != nb):
            break
    print('Map chargée')


def changeMap(porte):
    i = random.randint(0, len(porte['disponible']) - 1)
    click(porte[porte['disponible'][i]][0], porte[porte['disponible'][i]][1])
    checkChangeMapFinish()
    if (porte['disponible'][i] == 'droite'):
        process['position'][0] = str(int(process['position'][0]) + 1)
        process['comeFrome'] = 'gauche'
    elif (porte['disponible'][i] == 'gauche'):
        process['position'][0] = str(int(process['position'][0]) - 1)
        process['comeFrome'] = 'droite'
    elif (porte['disponible'][i] == 'haut'):
        process['position'][1] = str(int(process['position'][1]) - 1)
        process['comeFrome'] = 'bas'
    elif (porte['disponible'][i] == 'bas'):
        process['position'][1] = str(int(process['position'][1]) + 1)
        process['comeFrome'] = 'haut'
    print('----     MAP: ' + process['position'][0] + ', ' + process['position'][1] + ' ----')
    print('Nombre de ressources à récolté: ' + str(map[process['position'][0] + ',' + process['position'][1]]['ressources'][0][1]))
    stats['changeMap'] = stats['changeMap'] + 1


def collectMap(carte):
    collectRessources(carte['ressources'])
    changeMap(carte['porte'])


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    sleep(0.2)
    stats['click'] = stats['click'] + 1
    return True


def collectRessources(ressources):
    i = 1
    while (i < len(ressources)):
        pic = getPicture()
        r, g, b = pic.getpixel(((ressources[i][1] - screen['start'][0]), (ressources[i][2] - screen['start'][1])))
        if not (r in range((ressources[i][3][0] - 2), (ressources[i][3][0] + 2)) and g in range((ressources[i][3][1] - 2), (ressources[i][3][1] + 2)) and b in range((ressources[i][3][2] - 2), (ressources[i][3][2] + 2))):
            click(ressources[i][1], ressources[i][2])
            click(ressources[i][1] + 50, ressources[i][2] + 75)
            if (ressources[i][2] + 75 > 1477):
                click(ressources[i][1], ressources[i][2])
                click(ressources[i][1] + 50, 1470)
            checkRessourceCollected(ressources[i])
            verifPods()
            print(ressources[i][0] + ' récolté')
            i = 1
        i = i + 1


def checkRessourceCollected(ressource):
    while (True and not keyboard.is_pressed('f9')):
        pic = getPicture()
        r, g, b = pic.getpixel(((ressource[1] - screen['start'][0]), (ressource[2] - screen['start'][1])))
        if (r in range((ressource[3][0] - 2), (ressource[3][0] + 2)) and g in range((ressource[3][1] - 2), (ressource[3][1] + 2)) and b in range((ressource[3][2] - 2), (ressource[3][2] + 2))):
            stats['ressourceCollecter'] = stats['ressourceCollecter'] + 1
            break
    verifPods()


def checkLevelup(level):
    while True:
        pic = pyautogui.screenshot(region=(screen['start'][0], screen['start'][1], screen['end'][0], screen['end'][1]))
        r, g, b = pic.getpixel(((1006 - 0), (993 - 364)))
        if (r == 255 and g == 97 and b == 0):
            pyautogui.press('enter')
            stats['levelup'] = stats['levelup'] + 1
            print('-----    LEVEL UP: ' + str(process['level']) + '    -----')
        sleep(0.5)


def main(nothing):
    getPositionStart()
    process['level'] = int(input('Niveau de votre métier de bucheron? '))
    sleep(5)
    print('----     MAP: ' + process['position'][0] + ', ' + process['position'][1] + '    -----')
    print('Nombre de ressources à récolté: ' + str(map[process['position'][0] + ',' + process['position'][1]]['ressources'][0][1]))
    while (verifPods()):
        collectMap(map[process['position'][0] + ',' + process['position'][1]])


def checkCombat():
    sleep(2)
    pic = pyautogui.screenshot(region=(screen['start'][0], screen['start'][1], screen['append'][0], screen['append'][1]))
    r, g, b = pic.getpixel((1145 - screen['start'][0], 1542 - screen['start'][1]))
    if (r != screen['combat'][0][0] and g != screen['combat'][0][1] and b != screen['combat'][0][2] and
        r != screen['combat'][1][0] and g != screen['combat'][1][1] and b != screen['combat'][1][2]):
        # GET READY FOR COMBAT
        pyautogui.press(combat['pass'])
        print('Combat starting')


#_thread.start_new_thread(main, ('',))
#_thread.start_new_thread(checkLevelup, (process['level'],))
#verifKeyStopPress('')
print(json.dumps(map, indent=4))