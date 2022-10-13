import threading
import pyautogui

def printit():
  threading.Timer(5.0, printit).start()
  print( pyautogui.position())

printit()
