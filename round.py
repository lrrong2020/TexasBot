import threading
import pyautogui
import time

whiteBlockPoint2k = (2225, 1111)
whiteBlockPoint1080 = (1677, 834)
yellowCirclePoint1080 = (1655, 794)


thread=None
isMyTurn=False

def getMyRound():
  thread=threading.Timer(0.6, getMyRound)
  thread.start()

  isYellowCircleDisplaying(thread)

def allIn():
  pyautogui.press('r')#raise
  pyautogui.click(x=1400, y=918)#all-in
  pyautogui.click(x=1724, y=958)#enter

def fold():
  pyautogui.press('f')
  
def isYellowCircleDisplaying(thread):
  isMyTurn = not pyautogui.pixelMatchesColor(*yellowCirclePoint1080, (0, 0, 0), tolerance=50)
  if isMyTurn:
      print("My Turn!")
      
      
      '''
      Check if hand is in range
      '''

      '''
      all-in or fold
      '''

      
      isMyTurn=False
      thread.cancel()
  else:
      print("Not my turn")

getMyRound()

