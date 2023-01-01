import pygame, sys


from classes.fps import FPS
from classes.scenebase import SceneBase
from classes.scenes.gameScene import GameScene
from classes.scenes.title_Scene import TitleScene






# functions

def run_game(width, height, frameps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width ,height))
    clock = pygame.time.Clock()
    fps = FPS()
    active_scene = starting_scene


    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # event flitering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:  
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events,pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        fps.rend(screen)

        pygame.display.flip()
        fps.clock.tick(frameps)


        
run_game(800, 600, 60, TitleScene())