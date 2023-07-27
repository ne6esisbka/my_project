import pygame

class Ino(pygame.sprite.Sprite):
    # класс одного пришельца
    def __init__(self, screen):
        # инациализируем и задаём начальную позицию
        super(Ino,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Images/INO.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # Вывод пришельца на экран
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Перемещение пришельцев
        self.y += 0.1
        self.rect.y = self.y