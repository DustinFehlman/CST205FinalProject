import os
from media import *

def spedUp(sound):
 numSamples = getNumSamples(sound)
 newSound = makeEmptySound(numSamples / 2,int(getSamplingRate(sound)))
 index = 0
 for newIndex in range(numSamples / 2):
   val = getSampleValueAt(sound, int(index))
   setSampleValueAt(newSound, newIndex, val)
   index = index + 2
 return newSound

def slowdown(sound):
 numSamples = getNumSamples(sound)
 newSound = makeEmptySound(numSamples * 2,int(getSamplingRate(sound)))
 index = 0
 for newIndex in range(numSamples * 2):
   val = getSampleValueAt(sound, int(index))
   setSampleValueAt(newSound, newIndex, val)
   index = index + .5
 return newSound
 
def reverse(sound):
  newSound = makeEmptySound(getNumSamples(sound),int(getSamplingRate(sound)))
  newIndex = getNumSamples(sound)-1
  
  # loop through original sound, setting values in new sound
  for index in range(getNumSamples(sound)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(newSound, newIndex, value)
    newIndex = newIndex -1
    # return the new sound
  return newSound

def normalize(sound):
 newSound = duplicateSound(sound)

 # find the largest sample value
 largest = 0
 for s in getSamples(newSound):
   largest = max(largest, abs(getSampleValue(s)))

 # compute the multiplication factor
 factor = 32767.0/largest

 # change the sample values
 for s in getSamples(newSound):
   value = getSampleValue(s)
   setSampleValue(s, value * factor)
 return newSound

def prepSoundFiles():
  path = (os.path.dirname(os.path.realpath(__file__)))
  if os.path.isfile(path + '/media/audio/gameSoundFiles/reversedBB.wav') == False:
    bradyBunch = makeSound(path + '/media/audio/orginalSoundFiles/brady_theme.wav')
    reversedBB = reverse(bradyBunch)
    reversedBB1 = normalize(reversedBB)
    writeSoundTo(reversedBB1, path + '/media/audio/gameSoundFiles/reversedBB.wav')
  
  if os.path.isfile(path + '/media/audio/gameSoundFiles/slowAndy.wav') == False:
    andy = makeSound(path + '/media/audio/orginalSoundFiles/Andy Griffith Show.wav')
    slowAndy = slowdown(andy)
    writeSoundTo(slowAndy, path + '/media/audio/gameSoundFiles/slowAndy.wav')
  
  if os.path.isfile(path + '/media/audio/gameSoundFiles/scoobyhigh.wav') == False:
    scooby = makeSound(path + '/media/audio/orginalSoundFiles/scoobydoo.wav')
    scooby = spedUp(scooby)
    writeSoundTo(scooby, path + '/media/audio/gameSoundFiles/scoobyhigh.wav')
  
  if os.path.isfile(path + '/media/audio/gameSoundFiles/batmanSpedUpReversed.wav') == False:
    batman = makeSound(path + '/media/audio/orginalSoundFiles/38 Batman.wav')
    batmanSpedUp = spedUp(batman)
    batmanSpedUpReversed = reverse(batmanSpedUp)
    batmanSpedUpReversed = normalize(batmanSpedUpReversed)
    writeSoundTo(batmanSpedUpReversed, path + '/media/audio/gameSoundFiles/batmanSpedUpReversed.wav')
  
  if os.path.isfile(path + '/media/audio/gameSoundFiles/officeSlowDownReversed.wav') == False:
    office = makeSound(path + '/media/audio/orginalSoundFiles/The Office.wav')
    officeSlowDown = slowdown(office)
    officeSlowDownReversed = reverse(officeSlowDown)
    officeSlowDownReversed = normalize(officeSlowDownReversed)
    writeSoundTo(officeSlowDownReversed, path + '/media/audio/gameSoundFiles/officeSlowDownReversed.wav')  
 