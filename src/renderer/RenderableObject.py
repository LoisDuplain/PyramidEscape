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

    """
        CONSTRUCT
    """

    def __init__(self, image):
        super(RenderableObject, self).__init__()

        self.original_image = loadImage(image)
        self.original_width = self.original_image.get_width()
        self.original_height = self.original_image.get_height()

        self.current_image = self.original_image
        self.current_width = self.current_image.get_width()
        self.current_height = self.current_image.get_height()

        self.anchor_x = self.original_width/2
        self.anchor_y = self.original_height/2

    """
        METHODS
    """

    def render(self, screen, x=0, y=0, angle=0):
        # TODO Render
        pass

    def compute_center_point(self):
        # TODO Compute
        pass

    """
        GETTERS AND SETTERS
    """

    def get_original_image(self):
        return self.original_image

    def set_original_image(self, new_original_image):
        self.original_image = new_original_image
        self.original_width = new_original_image.get_width()
        self.original_height = new_original_image.get_height()

    def get_original_width(self):
        return self.original_width

    def get_original_height(self):
        return self.original_height

    def get_current_image(self):
        return self.current_image

    def set_current_image(self, new_current_image):
        self.current_image = new_current_image
        self.current_width = new_current_image.get_width()
        self.original_height = new_current_image.get_height()

    def get_current_width(self):
        return self.current_width

    def get_current_height(self):
        return self.current_height

    def get_anchor_x(self):
        return self.anchor_x

    def set_anchor_x(self, new_anchor_x):
        self.anchor_x = new_anchor_x

    def get_anchor_y(self):
        return self.anchor_y

    def set_anchor_y(self, new_anchor_y):
        self.anchor_y = new_anchor_y
