import pygame
import os
from copy import copy


class Player:
    """
    A class which represents the player.

    Attributes
    ----------
    posX: int
        the x position of the player
    posY: int
        the y position of the player
    main_surface: pygame.Surface
        the main surface which will be drawn apon
    surfaceY: int
        the height of the main surface
    animations: pygame.Surface
        the spritesheet which will be used for animations
    shell: list
        a list containing the x, y, width, and height of the player frame on the spritesheet
    def_shell: list
        a copy of the default shell
    shell_phase: int
        the starting frame of the player running animation on the spritesheet
    max_phase: int
        the last frame of the player running animation
    player_rate: int
        the rate at which the player animations update
    speed: int
        the default speed in the y axis
    upside_down: bool
        a boolean determining if the player is currently upside down or not

    Methods
    -------
    draw_player():
        a method which draws the player onto the screen in its correct orientation
    player_run():
        a method which increases the animation frame by 1
    frame_update(current_frame):
        runs the player_run() method after a set interval
    gravity(gravity_acceleration):
        a method which simulates gravity and makes the player fall to the opposite side of the screen
    """

    def __init__(self, posIn, surface, surface_dimensions):
        """
        Constructs all necessary attributes for the player.

        Parameters
        ----------
        posIn: list
            a list containing the initial x,y coordinates of the player
        surface: pygame.Surface
            the main surface which will be drawn onto
        surface_dimensions: list
            a list containing the width and height of the main surface
        """

        self.posX = posIn[0]
        self.posY = posIn[1]
        self.main_surface = surface
        self.surfaceY = surface_dimensions[1]

        self.animations = pygame.image.load(os.path.join("Game\Assets\Player_Assets\Animations", "adventurer-v1.5-Sheet.png"))

        self.animations = pygame.transform.scale(self.animations, (385*3, 592*3))
        
        self.shell = [54, 44, 50, 30]
                    # x, y, width, height
        
        for i in range(len(self.shell)):
            self.shell[i] = self.shell[i]*3

        self.def_shell = copy(self.shell)

        self.shell_phase = 0
        self.max_phase = 6     
        self.player_rate = 6

        self.speed = 1
        self.upside_down = False

    def draw_player(self):
        """
        A method which draws the player in its specified orientation and position.

        Parameters
        ----------
        None

        Returns
        -------
        hitbox: pygame.Rect
            the rectangular hitbox of the player
        """

        hitbox = pygame.Surface((64, self.shell[3]))
        hitbox.set_colorkey((0,0,0))

        hitbox.blit(self.animations, (-36, 0), self.shell)

        if self.upside_down:
            hitbox = pygame.transform.flip(hitbox, False, True)

        hitbox = self.main_surface.blit(hitbox, (self.posX, self.posY))
        
        return hitbox

    def player_run(self):
        """
        A method which increases the animation frame of the player by 1.

        The method increments the animation frame by 1 each call and if the
        animation frame is the last one it resets to the beginning.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if self.shell_phase <= self.max_phase - 1:
            self.shell_phase += 1
            self.shell[0] += self.shell[2]

        if self.shell_phase >= self.max_phase:
            self.shell_phase = 0
            self.shell = copy(self.def_shell)

    def frame_update(self, current_frame):
        """
        A method which runs player_run() at set intervals.

        This method will take the current frame which the program is on
        and then see if the current frame modulo the set rate which the 
        player animates at returns 0, and then run the player_run() method.

        Parameters
        ----------
        current_frame: int
            the frame that the program is currently on

        Returns
        -------
        None
        """

        if current_frame % self.player_rate == 0:
            self.player_run()

    def gravity(self, gravity_acceleration):
        """
        A method which replicates gravity and moves the player accordingly

        Parameters
        ----------
        gravity_acceleration: int
            a constant which is the acceleration of gravity, measured in pixels/s

        Returns
        -------
        None
        """
        speed_modifier = gravity_acceleration / 60

        if self.upside_down:
            self.posY -= self.speed
            self.speed = self.speed + speed_modifier
        
        else:
            self.posY += self.speed
            self.speed = self.speed + speed_modifier

        if self.posY >= self.surfaceY - self.shell[3] - 10:
            self.posY = self.surfaceY - self.shell[3] - 10
        elif self.posY <= 10:
            self.posY = 10