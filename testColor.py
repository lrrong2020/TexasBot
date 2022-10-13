import pyautogui

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
        return 'x'

print('Left: '+belongsColor(leftPos))
print('Right: '+belongsColor(rightPos))

'''
b = pyautogui.pixelMatchesColor(1519, 1090, (23, 183, 23), tolerance=50)
print(b)
'''
