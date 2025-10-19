import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.time.Clock()
    dt = 0
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    score = 0

    while True:
        tick = pygame.time.Clock().tick(60)
        dt = tick / 1000.0
        screen.fill("black")
        # Skoru ekrana yaz
        font = pygame.font.SysFont(None, 36)  # font boyutu 36
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # sol üst köşe

        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    score += int(asteroid.radius)
                    asteroid.split()
                    shot.kill()
                    if asteroid.radius > ASTEROID_MIN_RADIUS * 2:
                        score += 60
                    elif asteroid.radius > ASTEROID_MIN_RADIUS:
                        score += 40
                    else:
                        score += 20


        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                screen.fill("black")
                font = pygame.font.SysFont(None, 72)
                game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))
                screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2,
                                 (SCREEN_HEIGHT - game_over_text.get_height()) // 2 - 50))
                screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2,
                             (SCREEN_HEIGHT - score_text.get_height()) // 2 + 50))
                pygame.display.flip()
                pygame.time.delay(3000)
                return  # programı bitir
        # High score dosyası
        try:
            with open("highscore.txt", "r") as f:
                highscore = int(f.read())
        except FileNotFoundError:
            highscore = 0

        # Eğer yeni skor yüksekse güncelle
        if score > highscore:
            highscore = score
        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()
