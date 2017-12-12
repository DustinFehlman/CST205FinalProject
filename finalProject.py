#Team Educode Final Project

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

def game():
  showInformation("Welcome! You are about to embark on a journey that will stretch your hearing capabilities to their maximum!")
  playerName = requestString("What is your name, adventurous adventurer?")
  player1 = Player(playerName)
  scoreboard = Scoreboard(player1.name)
  
  showInformation("Current Score: " + str(scoreboard.score) + "\nYou enter a large room with a phonograph. There are posters from old movies adorning the walls.")
  #insert first sound file
  sound1Response = requestString("What do you hear playing from the phonograph?")
  if soundAccuracy(sound1Response, "correct"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("Current Score: " + str(scoreboard.score) + "\nYou enter a second room. Blinking from the bright lights, you realize you have walked right onto a stage. " + 
                      "The audience is full- standing room only.")
  #insert second sound file
  sound2Response = requestString("Current Score: " + str(scoreboard.score) + "\nQuickly- before they remove you forcibly- what is the singer singing?")
  if soundAccuracy(sound2Response, "correct"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("The security guard takes you off the satge and leads you outside to a car. The radio is playing.")
  #insert third sound file
  sound3Response = requestString("Current Score: " + str(scoreboard.score) + "\nWhat do you hear on the radio?")
  if soundAccuracy(sound3Response, "correct"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("After you fill in some paperwork, you are free to go. You pass a music store.")
  #insert fourth sound file
  sound4Response = requestString("Current Score: " + str(scoreboard.score) + "\nWhat are they playing in the store?")
  if soundAccuracy(sound4Response, "correct"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
  
  showInformation("You pass an outdoor concert in a park.")
  #insert fifth sound file
  sound5Response = requestString("Current Score: " + str(scoreboard.score) + "\nWhat is the lead singer singing?")
  if soundAccuracy(sound5Response, "correct"): #placeholder- insert correct answer instead of "correct"
    scoreboard.addScore(1)
    showInformation("Correct!")
  else:
    showInformation("Sorry. That is incorrect.")
   
  if scoreboard.score > 3:  #4 or 5
    showInformation(player1.name + ", you are a sound expert! You guessed " + str(scoreboard.score) + " sounds correctly!")
  elif scoreboard.score > 1: #2 or 3
    showInformation(player1.name + ", you correctly guessed some of the sounds- " + str(scoreboard.score) + " to be exact.") 
  else: # 0 or 1
    showInformation(player1.name + ", nice try. You gussed " + str(scoreboard.score) + " sounds correctly.")
  
#determines if the user has entered the correct respons  
def soundAccuracy(response, correctString):
  if response.lower() == correctString:
    return True
  else:
    return False
   
def main():
  game()
  
  