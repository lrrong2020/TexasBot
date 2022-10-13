import pyautogui

leftPos = (1432, 1089)
rightPos = (1519, 1090)

spadeRGB = (0, 0, 0)
heartRGB = (202,44,43)
clubRGB = (23, 183, 23)
diamondRGB = 66, 64, 207)


def belongsColor(*args):   
    if pyautogui.pixelMatchesColor(*args, spadeRGB, tolerance=50):
        return 's'
    elif pyautogui.pixelMatchesColor(*args, heartRGB, tolerance=50):
        return 'h'
    elif pyautogui.pixelMatchesColor(*args, clubRGB, tolerance=50):
        return 'c'
    elif pyautogui.pixelMatchesColor(*args, diamondRGB, tolerance=50):
        return 'd'
    else:
        return 'x'

print('Left: '+belongsColor(leftPos))
