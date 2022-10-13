import pyautogui

myArea = (1350, 998, 200, 70)

img = pyautogui.screenshot(region=myArea)

Cards = ['2L',
         '3L',
         '4L',
         '5L',
         '6L',
         '7L',
         '8L',
         '9L',
         'TL',
         'JL',
         'QL',
         'KL',
         'AL',
         '2R',
         '3R',
         '4R',
         '5R',
         '6R',
         '7R',
         '8R',
         '9R',
         'TR',
         'JR',
         'QR',
         'KR',
         'AR',
    ]

myHand=[]

for i in Cards:
    fileName = str('Numbers\\' + i + '.jpg')
    #print('searching for: ' + fileName)
    result = pyautogui.locateAll(fileName, img, confidence=0.98, grayscale=True)
    
    resultList = list(result)
    #print(resultList)
    if not resultList:
        continue
    elif len(resultList) == 1:
        myHand.append(i[:1])
    else:
        raise Exception("Confidence too low")

if len(myHand) < 2:
    raise Exception("Confidence too high")

print(list(myHand))
