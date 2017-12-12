#Team Educode Final Project: Dustin Fehlman, Carlos Sanchez, Hanna Bonert
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from soundManipulation import prepSoundFiles

class Scoreboard:
  score = 0
  playerName = None
  
  def __init__(self, playerName):
    self.playerName = playerName
    
  def getScore(self):
    return self.score
  
  def getPlayerName(self):
    return self.playerName
    
  def setScore(self, score):
    self.score = score
  
  def addScore(self, add):
    self.score += add
    
  def subtractScore(self, sub):
    self.score -= sub
    
class Player:
  name = None
  def __init__(self, name):
    self.name = name

def playSound(file):
  sound = makeSound(file)
  play(sound)
  return sound

def game():
  path = (os.path.dirname(os.path.realpath(__file__)))
  
  showInformation("Welcome! You are about to embark on a journey that will stretch your hearing capabilities to their maximum!")
  playerName = requestString("What is your name, adventurous adventurer?")
  player1 = Player(playerName)
  scoreboard = Scoreboard(player1.name)
  
  showInformation("Current Score: " + str(scoreboard.score) + "\nYou enter a large room with a phonograph. There are posters from old movies adorning the walls.")
  soundPointer = playSound(path + '/media/audio/gameSoundFiles/reversedBB.wav')
  sound1Response = requestString("What do you hear playing from the phonograph?")
  stopPlaying(soundPointer)
  
  if soundAccuracy(sound1Response, "the brady brunch"):
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("Current Score: " + str(scoreboard.score) + "\nYou enter a second room. Blinking from the bright lights, you realize you have walked right onto a stage. " + 
                      "The audience is full- standing room only.")
  soundPointer = playSound(path + '/media/audio/gameSoundFiles/slowAndy.wav')
  sound2Response = requestString("Current Score: " + str(scoreboard.score) + "\nQuickly- before they remove you forcibly- what is the singer singing?")
  stopPlaying(soundPointer)
  if soundAccuracy(sound2Response, "the andy griffith show"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("The security guard takes you off the satge and leads you outside to a car. The radio is playing.")
  soundPointer = playSound(path + '/media/audio/gameSoundFiles/scoobyhigh.wav')
  sound3Response = requestString("Current Score: " + str(scoreboard.score) + "\nWhat do you hear on the radio?")
  stopPlaying(soundPointer)
  if soundAccuracy(sound3Response, "the scooby-doo show"):
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("After you fill in some paperwork, you are free to go. You pass a music store.")
  soundPointer = playSound(path + '/media/audio/gameSoundFiles/batmanSpedUpReversed.wav')
  sound4Response = requestString("Current Score: " + str(scoreboard.score) + "\nWhat are they playing in the store?")
  stopPlaying(soundPointer)
  if soundAccuracy(sound4Response, "batman"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("You pass an outdoor concert in a park.")
  soundPointer = playSound(path + '/media/audio/gameSoundFiles/officeSlowDownReversed.wav')
  sound5Response = requestString("Current Score: " + str(scoreboard.score) + "\nWhat is the lead singer singing?")
  stopPlaying(soundPointer)
  if soundAccuracy(sound5Response, "the office"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
   
  if scoreboard.score > 3:  #4 or 5
    showInformation(player1.name + ", you are a sound expert! You guessed " + str(scoreboard.score) + " sounds correctly!")
  elif scoreboard.score > 1: #2 or 3
    showInformation(player1.name + ", you correctly guessed some of the sounds, " + str(scoreboard.score) + " to be exact.") 
  else: # 0 or 1
    showInformation(player1.name + ", nice try. You gussed " + str(scoreboard.score) + " sounds correctly.")
  
#determines if the user has entered the correct respons  
def soundAccuracy(response, correctString):
  if response.lower() == correctString:
    return True
  else:
    return False
   
def main():
  print("Preparing games files...")
  prepSoundFiles()
  game()
  
  