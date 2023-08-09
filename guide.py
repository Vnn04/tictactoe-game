import pygame
import sys
import textwrap

from const import *

class Guide:
    def __init__(self, surface):
        self.heading = 'Guide'
        self.surface = surface

        self.rect_guide = pygame.Rect(150, 150, 300, 300)
        self.rect_back = pygame.Rect(10, 10, 70, 40)
        self.font = pygame.font.SysFont('sans', 22)

    def show_heading(self):
        font_heading = pygame.font.SysFont('sans', 30)
        heading_text = font_heading.render(self.heading, True, TEXT_COLOR)
        heading_rect_text = heading_text.get_rect(center=self.rect_guide.center)
        self.surface.blit(heading_text, heading_rect_text)

    def draw_back_button(self):
        # hover state on back button
        if self.rect_back.collidepoint(pygame.mouse.get_pos()):
            hovered_back = True 
        else:
            hovered_back = False
        # create back button
        if hovered_back:
            back_button = pygame.draw.rect(self.surface, BUTTON_HOVER_COLOR, (10, 10, 70, 40), border_radius=10)
            text_back = self.font.render('Back', True, TEXT_COLOR_HOVER)
        else:
            back_button = pygame.draw.rect(self.surface, BUTTON_COLOR, (10, 10, 70, 40), border_radius=10)
            text_back = self.font.render('Back', True, TEXT_COLOR)
        text_rect_back = text_back.get_rect(center=self.rect_back.center)
        self.surface.blit(text_back, text_rect_back)

    def show_guide(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.surface.fill(BG_COLOR)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 10 <= pos[0] <= 80 and 10 <= pos[1] <= 50:
                        return

            self.draw_back_button()

            self.show_heading()

            pygame.display.update()