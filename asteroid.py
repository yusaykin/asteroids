import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Düz bir çizgide ilerle
        self.position += self.velocity * dt
    def split(self):
        # Her durumda bu asteroid yok oluyor
        self.kill()

        # Küçük asteroidler daha fazla bölünmez
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Rastgele bir açı belirle (20–50 derece)
        random_angle = random.uniform(20, 50)

        # Yeni yön vektörlerini oluştur
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Yeni asteroidlerin yarıçapı
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Yeni iki asteroid oluştur
        from asteroid import Asteroid  # iç içe import, sorun değil çünkü aynı dosya
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2