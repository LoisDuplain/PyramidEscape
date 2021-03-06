import pygame

images = {}


def loadImage(imageName):
    if imageName in images:
        return images[imageName]

    image_path = "resources/img/" + imageName
    try:
        image = pygame.image.load(image_path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        images[imageName] = image
    except pygame.error as message:
        print('Cannot load image:', image_path)
        raise SystemExit(message)
    return image
