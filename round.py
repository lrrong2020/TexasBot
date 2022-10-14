import threading

thread=None

def getMyRound():
  thread=threading.Timer(0.5, getMyRound)
  thread.start()
  print( "Hello, World!")

def isWhite():
  

getMyRound()

