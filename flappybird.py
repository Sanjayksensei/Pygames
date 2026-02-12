import pygame
import random


pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -6
PIPE_SPEED = 3
GAP_SIZE = 150


WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.rect = pygame.Rect(50, SCREEN_HEIGHT // 2, 30, 30)
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self):
        pygame.draw.ellipse(screen, YELLOW, self.rect)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.top_rect = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + GAP_SIZE, 50, SCREEN_HEIGHT)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

def main():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + 100)]
    score = 0
    running = True

    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

       
        bird.update()

       
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe(SCREEN_WIDTH))
        
        for pipe in pipes:
            pipe.update()
            if pipe.x < -50:
                pipes.remove(pipe)
                score += 1

            
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                running = False

      
        if bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT:
            running = False

       
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()