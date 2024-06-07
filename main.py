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

NUM_CAKE = 15

cake_cooldown = 500

class Cake(pg.sprite.Sprite):
    def __init__(self):
       super().__init__()

       self.image = pg.image.load("Pygame-Project-2024/images/red.png")
       self.image = pg.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2 ))

       self.rect = self.image.get_rect()

       self.vel_y = 5
       self.rect.centery = random.randrange(0, 720)
       self.rect.centerx = random.randrange(0, WIDTH + 1)
    def update(self):
       self.rect.centery += self.vel_y
       self.rect.y += self.vel_y
       print(self.rect.y)
       print(self.rect.x)
       if self.rect.y > HEIGHT:
         self.rect.y -= 720

class Tray(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Pygame-Project-2024/images/tray.png")
        self.image = pg.transform.scale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3 ))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pg.mouse.get_pos()
        
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200

class Sound(pg.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.sound = pg.mixer.Sound("Pygame-Project-2024/sounds/happy.mp3")
        self.sound.play()

def main():
    start()
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)

    score = 0

    pg.display.set_caption(TITLE)

    done = False
    clock = pg.time.Clock()

    font = pg.font.SysFont("Didot", 24)


    background = pg.image.load("Pygame-Project-2024/images/oven.webp")
    background = pg.transform.scale(background, (WIDTH, HEIGHT))

    all_sprites = pg.sprite.Group()
    cake_sprites = pg.sprite.Group()
    for _ in range(NUM_CAKE):
        cake = Cake()
        cake_sprites.add(cake)

    tray_sprites = pg.sprite.Group()
    tray = Tray()

    sound_sprites = pg.sprite.Group()
    sound = Sound()

    tray_sprites.add(tray)

    last_cake = pg.time.get_ticks()

    eating_sound = pg.mixer.Sound("Pygame-Project-2024/sounds/eat.mp3")

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                    pg.quit()
                    return

        if pg.key.get_pressed()[pg.K_SPACE]:
            break

        screen.blit(background, (0, 0))

        start_text = font.render("Press Space to start!!!", True, WHITE)
        quit_text = font.render("Press Q to quit.", True, WHITE)

        start_text_coords = start_text.get_width() // 2, start_text.get_height() // 2
        quit_text_coords = quit_text.get_width() // 2, quit_text.get_height() // 2

        screen.blit(start_text, (WIDTH // 2 - start_text_coords[0], HEIGHT // 2 - start_text_coords[1]))
        screen.blit(quit_text, (WIDTH // 2 - quit_text_coords[0], HEIGHT // 2 - quit_text_coords[1] + 20))
        
        pg.display.flip()
        clock.tick(60)

    done = False
   
    while not done:
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
    

        all_sprites.update()
        cake_sprites.update()
        tray_sprites.update()
        sound_sprites.update()

        tray_collided = pg.sprite.spritecollide(tray, cake_sprites, True)
        

        for coin in tray_collided:
            score += 1

            print(score)
            eating_sound.play()
        
        # Spawn a cake every 500 milliseconds
        now = pg.time.get_ticks()
        
        if now - last_cake > cake_cooldown:
            cake = Cake()

            cake.rect.y = random.randrange(-50, 0)

            all_sprites.add(cake)
            cake_sprites.add(cake)

            last_cake = now

        screen.blit(background, (0, 0))

        cake_sprites.draw(screen)
        tray_sprites.draw(screen)
        sound_sprites.draw(screen)

        score_image = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_image, (5, 5))

        pg.display.flip()
        clock.tick(60)
        
def start():
    pg.init()

    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y

if __name__ == "__main__":
    main()