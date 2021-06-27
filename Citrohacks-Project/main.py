import pygame
import sys
import os
import random
from random import randint

def fact_generator():
    n = randint(0,10)
    facts =["More than 80 percent of the world and more than 99 percent of the U.S. and European populations live under light-polluted skies.",
        "The Milky Way is hidden from more than one-third of humankind, including 60 percent of Europeans and nearly 80 percent of North Americans.",
        "Light pollution hurts otherwise pristine and deserted sites because it spreads hundreds of miles from its source.",
        "The most light-polluted country on the planet is Singapore, where the entire population lives under “skies so bright that the eye cannot fully dark-adapt to night vision.",
        "Inhabitants of San Marino, Kuwait, Qatar, and Malta can no longer see the Milky Way.",
        "99 percent of people living in United Arab Emirates are unable to see the Milky Way, as are 98 percent of Israel and 97 percent of Egypt.",
        "The largest swaths of land without Milky Way visibility include the Belgium/Netherlands/Germany transnational region, the Padana plain in northern Italy, and the Boston to Washington expanse. Other large areas where the Milky Way has been lost are the London to Liverpool/Leeds region in England, and regions surrounding Beijing and Hong Kong in China and Taiwan",
        "If you live in or near Paris, to find the closest place with a large area without light pollution you'd have to travel over 500 miles to Corsica, Central Scotland, or Cuenca province, Spain.",
        "If you live in Neuchâtel, Switzerland you’d have to travel 845 miles to northwestern Scotland, Algeria, or Ukraine to find pristine nighttime skies.",
        "The countries with the least amount of people affected by light pollution are Chad, Central African Republic, and Madagascar, with more than three-quarters of their inhabitants living under pristine sky conditions."]
        # Facts from www.treehugger.com/shocking-facts-nighttime-sky-world-atlas-light-pollution-4858161
  print(facts[n])



from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))

#Load complete background image (must be .png)
bg = pygame.image.load(os.path.join("./" "EscLight_game_background .png"))
pygame.mouse.set_visible(0)
# Title of game
pygame.display.set_caption('EscLight')

while True:
  # frame rate
  clock.tick(60)
  screen.blit(bg, (0,0)) #draws image at initial coor.
  x, y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit
  pygame.display.update()

class MovingBackground:
  def __init__(self, screenheight, imagefile):
    self.img = pygame.image.load(imagefile)
    self.coord = [0,0]
    self.coord2 = [0, -screenheight]
    self.y_original = self.coord[1]
    self.y2_original = self.coord2[1]

def Show(self, surface):
    surface.blit(self.img, self.coord)
    surface.blit(self.img, self.coord2)

def UpdateCoords(self, speed_y, time):
  distance_y = speed_y * time
  self.coord[1] += distance_y
  self.coord2[1] += distance_y
  if self.coord[1] >= 0:
    self.coord[1] = self.y_original
    self.coord2[1] = self.y2_original


pygame.init() # initialize pygame
clock = pygame.time.Clock()
#dimensions
screenwidth, screenheight = (1920, 1080)
screen = pygame.display.set_mode((screenwidth, screenheight))

framerate = 60

bg_speed = 100
#fill in/adjust this line below
Cityscape = MovingBackground(screenheight, "EscLight_game_background .png")
pygame.mouse.set_visble(0)
pygame.display.set_caption('EscLight')

while True:
  time = clock.tick(framerate)/1000.0
  x, y = pygame.mouse.get_pos()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  Cityscape.UpdateCoords(bg_speed, time)
  Cityscape.Show(screen)
  pygame.display.update()

#check line 22 code?
