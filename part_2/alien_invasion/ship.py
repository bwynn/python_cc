import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        # initialize the ship and set it's starting position
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get it's rect.
        self.image = pygame.image.load('./images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update the ships position based on the movement flag
        # update the ships center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # center ship on screen
        self.center = self.screen_rect.centerx
