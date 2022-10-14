import pyautogui


myCards=[]

def getNumber():
    myArea = (1350, 998, 200, 70)
    #myArea1080 = (1028, 749, 200, 80)

    img = pyautogui.screenshot(region=myArea)

    Cards = ['2L','3L','4L','5L','6L','7L','8L','9L','TL','JL','QL','KL','AL','2R','3R','4R','5R','6R','7R','8R', '9R','TR','JR','QR','KR','AR',]

    for i in Cards:
        fileName = str('Numbers\\' + i + '.jpg')
        #print('searching for: ' + fileName)
        result = pyautogui.locateAll(fileName, img, confidence=0.98, grayscale=True)
    
        resultList = list(result)
        #print(resultList)
        if not resultList:
            continue
        elif len(resultList) == 1:
            myCards.append(i[:1])
        else:
            raise Exception("Found more than 1 card that mathces")

    if len(myCards) < 2:
        print(list(myCards))
        raise Exception("Cannot find 2 hand cards")

    #print(list(myCards))

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
            raise Exception("Suit no match")

    #print('Left: '+belongsColor(leftPos))
    #print('Right: '+belongsColor(rightPos))

    myCards[0]+=belongsColor(leftPos)
    myCards[1]+=belongsColor(rightPos)

'''
Sort hand
'''
    

def cardsToHand(cards):
    card1=cards[0][:1]
    suit1=cards[0][1:]
    card2=cards[1][:1]
    suit2=cards[1][1:]
    
    #compare
    cmpStr='23456789TJQKA'
    return (card2+suit2+card1+suit1) if cmpStr.index(card1)<cmpStr.index(card2) else (card1+suit1+card2+suit2)
    


getNumber()
getSuit()
print(list(myCards))
print(cardsToHand(myCards))
