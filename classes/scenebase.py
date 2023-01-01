import pygame

class SceneBase:
    def __init(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print(
            'god damn it. you didnt override this in the child class'
            )
    
    def Update(self):
        print(
            'god damn it. you didnt override this in the child class'
            )
        
    def Render(self, screen):
        print(
            'god damn it. you didnt override this in the child class'
            )
    
    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)