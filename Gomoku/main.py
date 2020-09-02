import pygame, sys
import pygame as pg
from pygame.locals import *

# pyGame 초기화
pygame.init()

# 디스플레이 정의
pygame.display.set_caption('Hello Wolrd!')
size = [400, 300]
screen = pygame.display.set_mode(size)

# 색정의
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
