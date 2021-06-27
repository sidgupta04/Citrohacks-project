import pygame
import sys
import os
from pygame.locals import *

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

class Birdcontrol:
  def __init__(self, screenheight, screenwidth, imagefile):
    self.shape = pygame.image.load(imagefile)
    self.top = screenheight - self.shape.get_height()
    self.left = screenwidth/2 - self.shape.get_width()/2
  
  def Show(self, surface):
    surface.blit(self.shape, (self.left, self.top))
  
  def control(self,x,y):
    self.movex += x
    self.movey += y
  
  def UpdateCoords(self):
    self.rect.x = self.rect.x + self.movex
    self.rect.y = sect.rect.y + self.movey

Bird = Birdcontrol(screenheight, screenwidth, "bird.png")
x, y = pygame.mouse.get_pos()

Bird.UpdateCoords(x, y)

Bird.Show(screen)