import pygame


def loadImage(imageName):
    image_path = "resources/img/" + imageName
    try:
        image = pygame.image.load(image_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', image_path)
        raise SystemExit(message)
    return image


class RenderableObject(pygame.sprite.Sprite):

    def __init__(self, image, x=0, y=0, angle=0):
        super(RenderableObject, self).__init__()
        self.original_image = loadImage(image)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.angle = angle

    def render(self, screen, x=0, y=0, angle=0):
        self.image = pygame.transform.rotozoom(self.original_image, angle, 1)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)
        self.x = x
        self.y = y
        self.angle = angle

    def get_original_image(self):
        return self.original_image

    def get_image(self):
        return self.image

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_angle(self):
        return self.angle
