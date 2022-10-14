import pyautogui
import threading
import time
import itertools

conf=0.98

pairs=['AA','KK','QQ','JJ','TT','99','88','77','66','55','44','33','22']
broadways=['AK','AQ','AJ','KQ','KJ','QJ']

hasAce=['AA','A2','A3','A4','A5','A6','A7','A8','A9','AT','AJ','AQ','AK']

allinRange=list(itertools.chain(pairs, broadways,hasAce))
#allinRange=['AA','KK','AK','AQ','QQ','JJ','TT','99','88']

myArea = (1350, 998, 200, 70)
#myArea1080 = (1028, 749, 200, 80)

#whiteBlockPoint = (2225, 1111)
#whiteBlockPoint1080 = (1677, 834)
#yellowCirclePoint1080 = (1655, 794)
yellowCirclePoint = (2230, 1064)

def getNumber():
    global conf, myCards
    myCards=[]
    
    img = pyautogui.screenshot(region=myArea)

    Cards = ['2L','3L','4L','5L','6L','7L','8L','9L','TL','JL','QL','KL','AL','2R','3R','4R','5R','6R','7R','8R', '9R','TR','JR','QR','KR','AR',]

    for i in Cards:
        fileName = str('Numbers\\' + i + '.jpg')
        #print('searching for: ' + fileName)
        result = pyautogui.locateAll(fileName, img, confidence=conf, grayscale=True)
    
        resultList = list(result)
        #print(resultList)
        if not resultList:
            continue
        elif len(resultList) == 1:
            myCards.append(i[:1])
        else:
            #raise Exception("Found more than 1 card that mathces")
            print("confidence may be too low. +0.01")
            conf+=0.01
            getNumber()

    if len(myCards) < 2:
        print(myCards)
        #raise Exception("Cannot find 2 hand cards")
        print("confidence may be too high. -0.01")
        conf-=0.01
        getNumber()

    #print(myCards)

def getSuit():
    leftPos = (1432, 1089)
    rightPos = (1519, 1090)

    spadeRGB = (0, 0, 0)
    heartRGB = (202,44,43)
    clubRGB = (23, 183, 23)
    diamondRGB = (66, 64, 207)


    def belongsColor(pos):   
        if pyautogui.pixelMatchesColor(*pos, (0, 0, 0), tolerance=50):
            return 's'
        elif pyautogui.pixelMatchesColor(*pos, (202,44,43), tolerance=50):
            return 'h'
        elif pyautogui.pixelMatchesColor(*pos, (23, 183, 23), tolerance=50):
            return 'c'
        elif pyautogui.pixelMatchesColor(*pos, (66, 64, 207), tolerance=50):
            return 'd'
        else:
            print("Suit no match")

    #print('Left: '+belongsColor(leftPos))
    #print('Right: '+belongsColor(rightPos))

    myCards[0]+=belongsColor(leftPos)
    myCards[1]+=belongsColor(rightPos)


def cardsToHand(cards):
    card1=cards[0][:1]
    suit1=cards[0][1:]
    card2=cards[1][:1]
    suit2=cards[1][1:]
    
    #compare
    cmpStr='23456789TJQKA'
    
    result = (card2+suit2+card1+suit1) if cmpStr.index(card1)<cmpStr.index(card2) else (card1+suit1+card2+suit2)

    print("converted" + str(cards) + " to " + result)

    return result

def getHand():
    getNumber()
    getSuit()
    print("got Cards" + str(myCards))

    if len(myCards) != 2:
        raise Exception("myCards incorrect!")
    
    return cardsToHand(myCards)

def reset():
    myCards=[]
    myHand=''

#check range
def checkRange(hand, rg):
    print("Checking " + hand[:1]+hand[2:3] + " in range: ")
    print(rg)
    return any(hand[:1]+hand[2:3] in r for r in rg)

def allIn():
    pyautogui.press('r')#raise
    time.sleep(0.1)
    pyautogui.click(x=1400, y=918)#all-in
    time.sleep(0.1)
    pyautogui.click(x=1724, y=958)#enter

def fold():
    pyautogui.press('f')


def isYellowCircleDisplaying():    
    return not pyautogui.pixelMatchesColor(*yellowCirclePoint, (0, 0, 0), tolerance=50)

def checkMyTurn():
    while True:
        if isYellowCircleDisplaying():
            print("My Turn!")
            return
        else:
            print("Not my turn")
            time.sleep(0.5)
            continue


def main():
    while True:
        checkMyTurn()

        myHand=getHand()
    
        if(checkRange(myHand, allinRange)):
            print("In all-in range. I'm all-in")
            allIn()
        
        else:
            print("Not in all-in range. I fold")
            fold()

        time.sleep(5)
    
    

if __name__ == "__main__":
    main()

