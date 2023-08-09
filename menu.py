import pygame
import sys

from const import *
from guide import Guide

class Menu:

    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont('sans', 35)
        self.rect_start = pygame.Rect(60, 100, 220, 100)
        self.rect_guide = pygame.Rect(60, 250, 220, 100)
        self.rect_quit = pygame.Rect(60, 400, 220, 100)
        self.img = pygame.image.load(r"image\game_show.png")
        self.img = pygame.transform.scale(self.img, (270, 270))

    def display(self):
        self.surface.fill(BG_COLOR)
    
    def create_buttons(self):
        # hover state on start button
        if self.rect_start.collidepoint(pygame.mouse.get_pos()):
            hovered_start = True 
        else:
            hovered_start = False
        # create start button
        if hovered_start:
            start_button = pygame.draw.rect(self.surface, BUTTON_HOVER_COLOR, (60, 100, 220, 100), border_radius=30)
            text_start = self.font.render('Start', True, TEXT_COLOR_HOVER)
        else:
            start_button = pygame.draw.rect(self.surface, BUTTON_COLOR, (60, 100, 220, 100), border_radius=30)
            text_start = self.font.render('Start', True, TEXT_COLOR)
        text_rect_start = text_start.get_rect(center=self.rect_start.center)
        self.surface.blit(text_start, text_rect_start)

        # hover state on guide button
        if self.rect_guide.collidepoint(pygame.mouse.get_pos()):
            hovered_guide = True 
        else:
            hovered_guide = False
        # create guide button
        if hovered_guide:
            guide_button = pygame.draw.rect(self.surface, BUTTON_HOVER_COLOR, (60, 250, 220, 100), border_radius=30)
            text_guide = self.font.render('Guide', True, TEXT_COLOR_HOVER)
        else:
            guide_button = pygame.draw.rect(self.surface, BUTTON_COLOR, (60, 250, 220, 100), border_radius=30)
            text_guide = self.font.render('Guide', True, TEXT_COLOR)
        text_rect_guide = text_guide.get_rect(center=self.rect_guide.center)
        self.surface.blit(text_guide, text_rect_guide)

        # hover state on quit button
        if self.rect_quit.collidepoint(pygame.mouse.get_pos()):
            hovered_quit = True 
        else:
            hovered_quit = False
        # create quit button
        if hovered_quit:
            quit_button = pygame.draw.rect(self.surface, BUTTON_HOVER_COLOR, (60, 400, 220, 100), border_radius=30)
            text_quit = self.font.render('Quit', True, TEXT_COLOR_HOVER)
        else:
            quit_button = pygame.draw.rect(self.surface, BUTTON_COLOR, (60, 400, 220, 100), border_radius=30)
            text_quit = self.font.render('Quit', True, TEXT_COLOR)
        text_rect_quit = text_quit.get_rect(center=self.rect_quit.center)
        self.surface.blit(text_quit, text_rect_quit)

        # show image game
        self.surface.blit(self.img, (300, 165))


    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # click quit button
                    if 60 <= pos[0] <= 280 and 400 <= pos[1] <= 500:
                        sys.exit()
                    
                    # click guide button
                    elif 60 <= pos[0] <= 280 and 250 <= pos[1] <= 350:
                        guide = Guide(self.surface)
                        guide.show_guide()

                    # click start button
                    elif 60 <= pos[0] <= 280 and 100 <= pos[1] <= 200:
                        return

            self.display()
            self.create_buttons()
            
            pygame.display.update()