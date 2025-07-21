import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((width, height))

    def run(self, FPS):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.process_events()
            pygame.display.update()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Zombie Survival")
    game = Game(width=700, height=700)
    game.run(FPS=60)
    pygame.quit()
