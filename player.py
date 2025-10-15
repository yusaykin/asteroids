from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame
from shot import Shot
from constants import PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
          
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        from constants import PLAYER_TURN_SPEED
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
        # sola dönmek için negatif yönde
            self.rotate(-dt)
        if keys[pygame.K_d]:
        # sağa dönmek için pozitif yönde
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        from constants import PLAYER_SPEED
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
        # position.copy() ile orijinal pozisyonu bozmadan kopya ver
        new_shot = Shot(self.position.copy(), shot_velocity)
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN




        