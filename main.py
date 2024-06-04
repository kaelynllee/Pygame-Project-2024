import pygame as pg
import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
TITLE = "Cakeria"

WIDTH = 1280
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_CAKE = 10

class Cake(pg.sprite.Sprite):
    def __init__(self):
       self.image = pg.image.load("Pygame-Project-2024/images/red.png")

       self.rect = self.image.get_rect()

       self.vel_y = 12
       self.rect.centery = random.randrange(0, 720)
       self.rect.centerx = random.randrange(0, WIDTH + 1)
    def update(self):
       self.rect.centery += self.vel_y
       self.rect.y += self.vel_y 
       print(self.rect.y)
       if self.rect.y > HEIGHT:
         self.rect.y -= 720

class Tray(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Pygame-Project-2024/images/tray.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pg.mouse.get_pos()
        
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200
 
def main():
    start()
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    background = pg.image.load("Pygame-Project-2024/images/oven.webp")
    background = pg.transform.scale(background, (WIDTH, HEIGHT))

    cake_sprites = pg.sprite.Group()
    for _ in range(NUM_CAKE):
        cake = Cake()
        cake_sprites.add(cake)

    tray_sprites = pg.sprite.Group()
    tray = Tray()

    tray_sprites.add(tray)
    
    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                tray.rect.centerx = x
                tray.rect.centery = y
                tray_sprites.add(tray)
                print(x, y)

        cake_sprites.update()
        tray_sprites.update()
    
        # --- Update the world state

        # --- Draw items
        screen.blit(background, (0, 0))

        cake_sprites.draw(screen)
        tray_sprites.draw(screen)

        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def start():
    
    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    cake_sprites = pg.sprite.Group()
       
def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y

if __name__ == "__main__":
    main()