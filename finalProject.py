#Team Educode Final Project

class Scoreboard:
  score = 0
  playerName = None
  
  def __init__(self, playerName):
    self.playerName = playerName
    
  def getScore():
    return score
  
  def getPlayerName():
    return playerName
    
  def setScore(score):
    self.score = score
  
  def addScore(add):
    self.score += add
    
  def subtractScore(sub):
    self.score -= sub
    
def main():
  scoreboard = Scoreboard("test")
  
  