import pygame
from classes.scenebase import SceneBase

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        
        screen.fill((0, 0, 0))
