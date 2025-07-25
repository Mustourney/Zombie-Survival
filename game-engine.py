import pygame
from collections.abc import Callable
from typing import List, Tuple, Dict

class _2D:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class _2Dobject:
    def __init__(self, pos:_2D, size:_2D, texture:pygame.Surface):
        self.pos = pos
        self.size = size
        self.texture = texture
        self.func:Callable[[_2Dobject, pygame.Surface], bool]

class _Color:
    def __init__(self, red:int, green:int, blue:int):
        self.red = red
        self.green = green
        self.blue = blue

        self.r = red
        self.g = green
        self.b = blue
        
class GameEngine:
    def __init__(self, width:int, height:int, title:str, FPS:int, fullscreen:bool, bgcolor:_Color):
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        pygame.display.set_caption(title)
        self.FPS = FPS

        self.running = False
    
        self.objects:List[_2Dobject] = []
        self.current_events:List[pygame.event.Event] = []

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((width, height), fullscreen)

    def draw_all(self):
        pygame.display.update()
        self.window.fill((self.bgcolor.r, self.bgcolor.g, self.bgcolor.b))

    def process_events(self):
        self.current_events = pygame.event.get()
        for event in self.current_events:
            if event.type == pygame.QUIT:
                self.running = False
                break

        objects_to_remove:List[int] = []
        for index, object in enumerate(self.objects):
            if not object.func(object, self.window):
                objects_to_remove.append(index)

        if objects_to_remove:
            offset:int = 0
            for index in objects_to_remove:
                self.objects.pop(index - offset)
                offset += 1

    def add_object(self, object:_2Dobject, func:Callable[[_2Dobject, pygame.Surface], bool]):
        object.func = func
        self.objects.append(object)

    def start(self):
        self.running = True

        while self.running:
            self.clock.tick(self.FPS)

            self.draw_all()
            self.process_events()

if __name__ == "__main__":
    example = GameEngine(
        width = 800,
        height = 800,
        title = "Example",
        FPS = 60,
        fullscreen = False,
        bgcolor = _Color(70, 70, 70)
    )

    the_moon = _2Dobject(
        pos = _2D(40, 40),
        size = _2D(70, 70),
        texture = pygame.image.load("Spawn_Decal.png")
    )

    def huh(object:_2Dobject, window:pygame.Surface) -> bool:
        if pygame.key.get_pressed()[pygame.K_w]:
            object.pos.x += 10
            object.pos.y += 10

        window.blit(object.texture, (object.pos.x, object.pos.y))
        for event in example.current_events:
            if event.type == pygame.KEYUP:
                return False
        
        return True

    example.add_object(the_moon, huh)

    example.start()

    pygame.quit()