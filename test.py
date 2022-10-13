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
         '10L',
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
         '10R',
         'JR',
         'QR',
         'KR',
         'AR',
    ]

for i in Cards:
    fileName = str('Numbers\\' + i + '.jpg')
    print('searching for: ' + fileName)
    result = pyautogui.locateAll(fileName, img, confidence=0.99, grayscale=True)
    print(list(result))
