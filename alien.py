import pygame

class Alien(pygame.sprite.Sprite):
    """Класс одного пришельца"""

    def __init__(self, screen):
        """Инициализируем и задаём начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельцев"""
        self.y += 0.1
        self.rect.y =self.y
