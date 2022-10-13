import pyautogui
leftIs = pyautogui.pixelMatchesColor(1451, 1091, (255, 255, 255), tolerance=100)
print(leftIs)
