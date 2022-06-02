#-----------------------------------------------------------------------------
# Name:        Gravity Dood
# Purpose:     An infinite platformer inspired by gravity guy, the main point of the game
#              is to avoid obstacles by 'Flipping' Gravity.
#
# Author:      Yusuf Ahmad
# Created:     24-May-2022
# Updated:     1-June-2022
#-----------------------------------------------------------------------------
#I think this project deserves a level 4+ because ...
#
#Features Added:
#   Object Oriented
#   Reading and writing to files (lines: 64-83, 289-309)
#   Smart spawning algorithm (lines: 219-251)
#   Background music (lines: 66-67)
#   Opening help file in browser (lines: 72, 172)
#   Physics, Gravity and Acceleration 
#    (gravity in Player.py gravity() method, called at lines: 258-267; Acceleration in lines: 124, 126, 186)
#-----------------------------------------------------------------------------

from random import randint, sample
import pygame
import json
from Assets.Player_Assets.Player import Player
from Assets.Collidables.Static.Short.Short import Spike, Saw
from Assets.Collidables.Static.Tall.Tall import Tall_Saw, Spear
from Assets.Collidables.Game_States.Start import Title
from Assets.Collidables.Game_States.Help import Help
from Assets.Collidables.Game_States.Game_Over import GameOver
import os
import webbrowser

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [750, 350]   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))

    # The file path to the background png file used as the background
    bg = pygame.image.load(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'bg.png'))

    # The default x position for the background when blitting the background onto the main surface
    bg_posX = 0

    # Instantiates the player class and prepares it for use
    player_sprite = Player((150, 200), mainSurface, surfaceSize)

    # Initial Instances of the short traps
    spike_trap = Spike([100, 100], mainSurface)
    saw_trap = Saw((100, 200), mainSurface)

    # Initial Instances of the tall traps
    spear_trap = Spear(mainSurface, [200, 100])
    tall_saw = Tall_Saw(mainSurface, [300, 100])

    # Instantiates the game states
    title_screen = Title(mainSurface)
    help_screen = Help(mainSurface, surfaceSize[1])
    game_over = GameOver(mainSurface)

    # prepares and plays the background music infinitely
    pygame.mixer.music.load(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'Jetpack Joyride Main Theme.oggvorbis.ogg'))
    pygame.mixer.music.play(-1)
    #-----------------------------Program Variable Initialization----------------------------#

    # The direct pathway do the instructions file, dynamically changes depending on where the repo is
    # and who's computer this is on
    instructions = 'file:///' + os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'Instructions.html')

    # Boolean variable which controls when the instructions file should be opened in browser
    help_state = False

    # Fixes the player to be 10 pixels off the bottom of the window
    player_sprite.posY = surfaceSize[1] - player_sprite.shell[3] - 10
    # The default orientation of the player is right-side down
    player_sprite.upside_down = False
    # by default the player is not falling
    falling = False
    # constant for gravity, speed increases by 60 pixels per second
    player_gravity = 60

    # Opens up a json file and takes the limit values used for spawning traps and assign them variables
    with open(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'Collidables', 'Limit.json'), 'r') as f:
        Limit = json.load(f)
        tall_range = range(Limit['static']['tall']['min'], Limit['static']['tall']['max'] + 1)
        short_range = range(Limit['static']['short']['min'], Limit['static']['short']['max'] + 1)

    # Defines a point within the spawning limit which then the next trap to be spawned will use
    point_in_sr = sample(short_range, 1)
    point_in_tr = sample(tall_range, 1)
    
    # Boolean value for seeing if the trap which is to be spawned is the first trap spawned
    first_object = True

    # Defines a list containing all 4 possible trap types
    trap_types = [spike_trap,
                  saw_trap,
                  spear_trap,
                  tall_saw]

    # Defines a list which will contain all the traps on the screen
    traps = []
    trap = randint(0, len(trap_types)-1) # The starting point of the infinite chain of trap spawning
                                         # Chooses a random number when the program starts to act as
                                         # A starting point for the next trap to be randomly chosen

    # a variable which counts how many frames have passed since the start of the game
    frame_count = 0

    # A boolean value which is used to start the counting of score
    game_start = False

    # Default Game State
    game_state = 'Start'


    # Defines a speed which the background moves at and which traps move at
    speed = 4
    # Defines an acceleration which the speed increases by each frame, exponentially increasing difficulty as the game progresses
    acceleration = 0.05 / 60

    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        # A binding rectangle set to the coordinates of the mouse positions
        mouse = pygame.mouse.get_pos()
        mouse_hitbox = pygame.Rect(mouse[0], mouse[1], 2, 2)

        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Checks if the game is in the 'Start' / main menu state
        if game_state == 'Start':
            
            mainSurface.blit(bg, (bg_posX, -95))

            # Sets variables to their default values
            player_sprite.upside_down = False
            player_sprite.speed = 1
            falling = False
            player_sprite.posY = surfaceSize[1] - player_sprite.shell[3] - 10
            traps = []
            first_object = True
            bg_posX = 0
            
            title_buttons = title_screen.draw_elements() # element 0 is the hitbox for the start button and 1 is the credits button

            # Changes the gamestate to 'Game' if the start button was clicked
            if ev.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                if pygame.Rect.colliderect(mouse_hitbox, title_buttons[0]):
                    game_state = 'Game'
            # Changes the gamestate to 'Help' if the credit button was clicked
            if ev.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                if pygame.Rect.colliderect(mouse_hitbox, title_buttons[1]):
                    game_state = 'Help'
                    help_state = True

        # Checks if the game is in the 'Help' / help screen state
        if game_state == 'Help':
            mainSurface.blit(bg, (bg_posX, -95))
            
            # Draws the elements of the help screen
            back_button = help_screen.draw_element()

            # Opens the instructions file in the default browser
            if help_state:
                webbrowser.open_new_tab(instructions)
                help_state = not help_state
            
            # If the back button is clicked, bring back to start menu
            if ev.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                if pygame.Rect.colliderect(mouse_hitbox, back_button):
                    game_state = 'Start'

        # Checks if the game is in the 'Game' / currently playing state
        if game_state == 'Game':

            # After each loop (frame) increase the speed which traps and the background travel at
            speed = speed + acceleration

            # After each frame change the x posisition of the bg 
            bg_posX -= speed
            mainSurface.blit(bg, (bg_posX, -95))

            # if half the entire background image (in the x) is off screen, reset the bg to the origin position
            if bg_posX <= surfaceSize[0] - ((bg.get_width() // 2) + surfaceSize[0]):
                bg_posX = 0

            # Checks if the spacebar has been pressed and sets it so that the player is in a 'falling' state 
            # and also flips the orientation of the player in the y axis
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE and falling == False:
                    player_sprite.upside_down = not player_sprite.upside_down
                    falling = True   
            #-----------------------------Program Logic---------------------------------------------#
            # Update your game objects and data structures here...

            # binds the rectangle hitbox of teh player to a variable
            player_hitbox = player_sprite.draw_player()

            # Changes the current frame of the player if the current frame is divisible by the rate at which 
            # the player's animation updates
            player_sprite.frame_update(frame_count)

            # Sets the initial time when the game starts to a variable
            if game_start == False:
                start_of_game = pygame.time.get_ticks()
                game_start = not game_start

            # Spawning Algorithm
            # Picks a trap out of a predetermined list containing all trap types at random
            # Creates a new instance of the selected trap, if it is the first trap spawned
            # It will be defined as the first trap so that the next object will be spawned
            # Relative to the previous trap, being the start to the infintie chain
            if first_object:
                trap_types[trap].posX = 1000
                if isinstance(trap_types[trap], Saw) or isinstance(trap_types[trap], Tall_Saw):
                    trap_types[trap].posY = 0
                elif isinstance(trap_types[trap], Spike) or isinstance(trap_types[trap], Spear):
                    trap_types[trap].posY = surfaceSize[1] - trap_types[trap].shell[3] - 10
                traps.append(trap_types[trap])
                first_object = False
            elif first_object == False:
                if isinstance(trap_types[trap], Spike):
                    if traps[-1].posX <= 1000 - point_in_sr[0]:
                        point_in_sr = sample(short_range, 1)
                        spike_trap = Spike([1000, surfaceSize[1] - trap_types[trap].shell[3] - 10], mainSurface)
                        traps.append(spike_trap)
                        trap = randint(0 , len(trap_types)-1)
                elif isinstance(trap_types[trap], Saw):
                    if traps[-1].posX <= 1000 - point_in_sr[0]:
                        point_in_sr = sample(short_range, 1)
                        saw_trap = Saw([1000, 0], mainSurface)
                        traps.append(saw_trap)
                        trap = randint(0 , len(trap_types)-1)
                elif isinstance(trap_types[trap], Spear):
                    if traps[-1].posX <= 1000 - point_in_tr[0]:
                        point_in_tr = sample(tall_range, 1)
                        spear_trap = Spear(mainSurface, [1000, surfaceSize[1] - trap_types[trap].shell[3] - 10])
                        traps.append(spear_trap)
                        trap = randint(0 , len(trap_types)-1)
                elif isinstance(trap_types[trap], Tall_Saw):
                    if traps[-1].posX <= 1000 - point_in_tr[0]:
                        point_in_tr = sample(tall_range, 1)
                        tall_saw = Tall_Saw(mainSurface, [1000, 0])
                        traps.append(tall_saw)
                        trap = randint(0 , len(trap_types)-1)

            # Falling Mechanism
            # If the players state is currently 'falling' it then exponentially changes the players y position
            # to come closer toward the direction which the player is falling to, simulating a sense of gravity
            if falling:
                player_sprite.gravity(player_gravity)
                if player_sprite.upside_down:
                    if player_sprite.posY == 10:
                        falling = not falling
                        player_sprite.speed = 1
                elif player_sprite.upside_down == False:
                    if player_sprite.posY == surfaceSize[1] - player_sprite.shell[3] - 10:
                        falling = not falling
                        player_sprite.speed = 1
                
            # Updates the x position of the traps which are on screen 
            for current_trap in traps:
                current_trap.posX -= speed

            for current_trap in traps:
                # Updates the animations of the trap every set frames
                current_trap.update_animation(frame_count, current_trap.framerate)
                trap_hitbox = current_trap.draw_trap()

                # Collision Detection
                # Checks if the player has collided with any object then sets the game state to 'Game Over'
                if pygame.Rect.colliderect(player_hitbox, trap_hitbox):
                    game_state = 'Game Over'
                    final_time = pygame.time.get_ticks() # The Total time it took since start of the program
                    score_modifier = (final_time - start_of_game) * ((acceleration * frame_count) / 10) # Score modifier which is just the difference between
                                                                                                        # Starting time and ending time of the game, multipled by 
                                                                                                        # the value of acceleration applied on the objects since the
                                                                                                        # start of the game divided by 10

                    score = int((final_time - start_of_game) + score_modifier) # Adds the score modifier to the difference in final and inital time

                    # Opens up the highscore file which will contain either an empty value: "\n" or a highscore previously set
                    with open(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'Highscore.json'), 'r') as f:
                        score_file = json.load(f)

                        # Checks if teh highscore is an empty value if it is, replace the 
                        # empty value with the score which was just set
                        if score_file['highscore'] == '\n':
                            with open(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'Highscore.json'), 'w') as j:
                                data_to_write = {'highscore': score}
                                json.dump(data_to_write, j, indent=2)
                                highscore = score
                        
                        # If the highscore read from teh file wasn't an empty value, checks if the 
                        # current score is greater than the highscore in the file, 
                        # If it is replace the old highscore with the currently set score
                        # If it is not greater do not perform any modifications on this file
                        else:
                            if score_file['highscore'] < score:
                               with open(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Game', 'Assets', 'Highscore.json'), 'w') as j:
                                data_to_write = {'highscore': score}
                                json.dump(data_to_write, j, indent=2)
                                highscore = score
                            else:
                                highscore = score_file['highscore']

            # Checks if any traps have gone off screen and deletes them if they are
            if traps:
                if traps[0].posX == (0 - traps[0].shell[2]):
                    traps.remove(traps[0])

        # Checks if the game has been lost
        if game_state == 'Game Over':
            game_over_buttons = game_over.draw_elements(score, highscore) # element 0 is quit button
                                                                          # element 1 is menu button
                                                                          # element 2 is restart button
            
            if ev.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:

                # If the quit button is pressed, exit the program
                if pygame.Rect.colliderect(mouse_hitbox, game_over_buttons[0]):
                    break

                # If the main menu button was pressed, sends back to the main menu
                if pygame.Rect.colliderect(mouse_hitbox, game_over_buttons[1]):
                    game_state = 'Start'

                # If the restart button is pressed sets all important variables back to their defaults 
                # and restarts the game directly
                if pygame.Rect.colliderect(mouse_hitbox, game_over_buttons[2]):
                    player_sprite.upside_down = False
                    player_sprite.speed = 1
                    falling = False
                    player_sprite.posY = surfaceSize[1] - player_sprite.shell[3] - 10
                    traps = []
                    first_object = True
                    bg_posX = 0
                    game_state = 'Game'


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        frame_count += 1
        clock.tick(60) #Force frame rate to be slower
 

    pygame.quit()     # Once we leave the loop, close the window.

main()