import pygame

from level.Level import Level

current_level = None


def main():
    global current_level
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Pyramid Escape")

    current_level = Level("main-menu.lvl")

    run = True
    while run:
        for event in pygame.event.get():
            current_level.events(event)

        # Send pressed keys to current level
        current_level.key_pressed(pygame.key.get_pressed())

        # Update level
        current_level.update()

        # Render level
        # 1- Render background
        screen.fill((0, 0, 0))
        # 2- Render level
        current_level.render(screen)
        # 3- Update screen to show rendered elements to player
        pygame.display.update()


def get_current_level():
    return current_level


def set_current_level(new_current_level):
    global current_level
    current_level = new_current_level


if __name__ == '__main__':
    main()
