from config import *
import myPygameWorkflow
import pygame

class SceneStart(myPygameWorkflow.presets.Scene):
    def start(self):
        font = pygame.font.Font(None, 64)
        icon = pygame.Surface((64, 64))
        icon.fill('#ffffff')
        icon.blit(font.render('S', True, '#000000'), icon.get_rect(center=(32, 32)))

        pygame.display.set_icon(icon)
        pygame.display.set_caption("Snake Game - DuskyElf")
        StartTitle(self, 1)
        StartButton(self, 2)
    
    def update(self):
        pass

class StartTitle(myPygameWorkflow.presets.Sprite):
    def start(self):
        self.font = pygame.font.Font(None, TITLE_SIZE)
        self.image = self.font.render('Snake Game', True, TITLE_COLOR)
        self.rect = self.image.get_rect(center=(WIN_WID/2, 200))

class StartButton(myPygameWorkflow.presets.Sprite):
    def start(self):
        self.font = pygame.font.Font(None, 32)
        self.image = pygame.Surface(START_BUTTON_SIZE, pygame.SRCALPHA)
        self.image.fill(START_BUTTON_COLOR)
        self.text = self.font.render('Start', True, START_BUTTON_TEXT_COLOR)
        self.text_rect = self.text.get_rect(center=START_BUTTON_SIZE/2)
        self.image.blit(self.text, self.text_rect)
        self.rect = self.image.get_rect(center=(WIN_WID/2, WIN_HEI-150))
        self.clicked = False
    
    def update(self):
        
        if self.rect.collidepoint(*pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
                    self.scene.running = False
