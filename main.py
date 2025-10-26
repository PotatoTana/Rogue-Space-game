from tkinter import *
import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

moving = False

class player:
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving = True
        
        if moving == True:
            print("Moving")
            
class bot_bandit:
    pass

class bot_police:
    pass

class shop:
    pass

class black_market:
    pass

class projectile:
    pass

def player_movement():
    pass

def player_shooting():
    pass

def player_projectile():
    pass

def bot_movement():
    pass

def bot_shooting():
    pass

def bot_projectile():
    pass

def check_collision():
    pass

def check_collision_projectile():
    pass

def shopping():
    pass

def upgrade():
    pass

def credit():
    pass

def game_over():
    pass

pygame.quit()