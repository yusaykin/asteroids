import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        # position: pygame.Vector2
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        # Mermiyi hareket ettir
        self.position += self.velocity * dt

    def draw(self, screen):
        # position bir Vector2; pygame.draw.circle bazı sürümlerde (int,int) ister
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2,
        )
