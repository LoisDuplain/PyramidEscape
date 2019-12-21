import pygame
from player.Player import Player

player = None


def main():
    global player
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Pyramid Escape")

    player = Player()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keyPressed(pygame.key.get_pressed())

        render(screen)

        pygame.display.update()
        screen.fill((0, 0, 0))


def render(screen):
    player.render(screen)


def keyPressed(keys):
    if keys[pygame.K_RIGHT]:
        pass


if __name__ == '__main__':
    main()
