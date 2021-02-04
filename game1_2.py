import pygame, os, random                   

class Settings(object):
    width = 700
    height = 400
    fps = 60       
    title = "game1_2" 
    file_path = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(file_path, "images2")
    bordersize = 10

    @staticmethod
    def get_dim():
        return (Settings.width, Settings.height)

class Spieler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "dude.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.left = (Settings.width - self.rect.width) // 2
        self.rect.bottom = Settings.height - Settings.bordersize
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        self.speed = 5

    def update(self):
        if self.left == 1:
            self.rect.x -= self.speed
        if self.right == 1:
            self.rect.x += self.speed
        if self.up == 1:
            self.rect.y -= self.speed
        if self.down == 1:
            self.rect.y += self.speed

        if self.rect.right >= Settings.width - Settings.bordersize:
            self.right = 0
            self.rect.right = Settings.width - Settings.bordersize
        if self.rect.left <= Settings.bordersize:
            self.left = 0
            self.rect.left = Settings.bordersize
        if self.rect.bottom >= Settings.height - Settings.bordersize:
            self.down = 0
            self.rect.bottom = Settings.height - Settings.bordersize
        if self.rect.top <= Settings.bordersize:
            self.up = 0
            self.rect.top = Settings.bordersize


    def teleport(self):
        self.new_postion_x = random.randrange((Settings.bordersize +30) , (Settings.width - Settings.bordersize -30))
        self.new_postion_y = random.randrange((Settings.bordersize +30) , (Settings.height - Settings.bordersize -30))
        self.rect.left = self.new_postion_x 
        self.rect.bottom = self.new_postion_y 

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.get_dim())
        pygame.display.set_caption(Settings.title)
        #Background erstellen
        self.background = pygame.image.load(os.path.join(Settings.images_path, "background.png")).convert()
        self.background = pygame.transform.scale(self.background, (Settings.width, Settings.height))
        self.background_rect = self.background.get_rect()
        
        #objekt zur sprite hinzufügen
        self.all_spieler = pygame.sprite.Group()
        self.spieler = Spieler()
        self.all_spieler.add(self.spieler)

        self.clock = pygame.time.Clock()
        self.done = False

    def run(self):
        while not self.done:                
            self.clock.tick(Settings.fps)           
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:   
                    self.done = True 
                elif event.type == pygame.KEYUP:          
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                    if event.key == pygame.K_LEFT:
                        self.spieler.left = 0
                    if event.key == pygame.K_RIGHT:
                        self.spieler.right = 0
                    if event.key == pygame.K_UP:
                        self.spieler.up = 0
                    if event.key == pygame.K_DOWN:
                        self.spieler.down = 0
                    elif event.key == pygame.K_SPACE:
                        self.spieler.teleport()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spieler.left = 1 
                    elif event.key == pygame.K_RIGHT:
                        self.spieler.right = 1 
                    elif event.key == pygame.K_UP:
                        self.spieler.up = 1
                    elif event.key == pygame.K_DOWN:
                        self.spieler.down = 1

            self.all_spieler.update()

            self.screen.blit(self.background, self.background_rect)
            self.all_spieler.draw(self.screen)
            pygame.display.flip()          


if __name__ == '__main__':      
                                    
    pygame.init()               
    game = Game()
    game.run()
    pygame.quit()
