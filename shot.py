import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, player_position, player_rotation):
        super().__init__(player_position[0], player_position[1], SHOT_RADIUS)
        self.rotation = player_rotation
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_RADIUS)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt
