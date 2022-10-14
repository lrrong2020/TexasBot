import threading
import pyautogui

whiteBlockPoint2k = (2225, 1111)
whiteBlockPoint1080 = (1677, 834)
yellowCirclePoint1080 = (1655, 794)

thread=None
isMyTurn=False

def getMyRound():
  thread=threading.Timer(0.5, getMyRound)
  thread.start()
  isMyTurn=isYellowCircleDisplaying()
  if isMyTurn:
      print("My Turn!")
      
      pyautogui.press('f')
      
      thread.cancel()
  else:
      print("Not my turn")
  

def isYellowCircleDisplaying():
  return not pyautogui.pixelMatchesColor(*yellowCirclePoint1080, (0, 0, 0), tolerance=50)


getMyRound()

