import pygame
from classes.scenebase import SceneBase

class TitleScene(SceneBase):
    def __init(self):
        super().__init__()
        # SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass

    def Render(self, screen):

        screen.fill((255 ,0 ,0))

      