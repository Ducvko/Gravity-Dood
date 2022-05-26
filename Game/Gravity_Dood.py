#-----------------------------------------------------------------------------
# Name:        Assignment Template (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
#I think this project deserves a level XXXXXX because ...
#
#Features Added:
#   ...
#   ...
#   ...
#-----------------------------------------------------------------------------

import pygame
import json
from Assets.Player_Assets.Player import Player
from Assets.Collidables.Static.Short.Short import Spike, Saw

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [750, 350]   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))

    player_sprite = Player((200, 200), mainSurface, surfaceSize, 0)

    spike_trap = Spike([100, 100], mainSurface)
    saw_trap = Saw((100, 200), mainSurface)

    player_sprite.upside_down = False

    frame_count = 0
    game_start = False

    #-----------------------------Program Variable Initialization----------------------------#
    # Set up some data to describe a small circle and its color



    #-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...


        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        player_sprite.frame_update(frame_count)
        player_sprite.draw_player()

        spike_trap.draw_trap(1, spike_trap.posX, spike_trap.posY)
        spike_trap.update_animation(frame_count, spike_trap.spike_rate)

        saw_trap.draw_trap(0, saw_trap.posX, saw_trap.posY)
        saw_trap.update_animation(frame_count, saw_trap.saw_rate)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        frame_count += 1
        clock.tick(60) #Force frame rate to be slower
 

    pygame.quit()     # Once we leave the loop, close the window.

main()