import pygame
import utils
import CONSTANTS
from level import levelloader
from level.level import Level

current_level = None


def main():
    global current_level
    pygame.init()
    screen = pygame.display.set_mode((CONSTANTS.CONSTANT_WINDOW_WIDTH, CONSTANTS.CONSTANT_WINDOW_HEIGHT))
    pygame.display.set_caption("Pyramid Escape")

    set_current_level(Level("main-menu.lvl"), True)

    last_update_date = utils.get_current_time_millis()
    last_render_date = utils.get_current_time_millis()

    run = True
    while run:
        # Update level
        update_delta_time = utils.get_current_time_millis() - last_update_date
        if update_delta_time >= 1000/120:
            last_update_date = utils.get_current_time_millis()
            current_level.update(update_delta_time, pygame.key.get_pressed())
            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    current_level.key_pressed(event.key)
                elif event.type == pygame.KEYUP:
                    current_level.key_released(event.key)

                current_level.events(event)
                
        render_delta_time = utils.get_current_time_millis() - last_render_date
        if render_delta_time >= 1000/120:
            last_render_date = utils.get_current_time_millis()
            # Render level
            # 1- Render background
            screen.fill((0, 0, 0))
            # 2- Render level
            current_level.render(screen)
            # 3- Update screen to show rendered elements to player
            pygame.display.update()

    pygame.quit()


def get_current_level():
    return current_level


def set_current_level(new_current_level, load_tiles):
    global current_level
    # Set new level to variable
    current_level = new_current_level
    # Load level tiles if necessary
    if load_tiles:
        levelloader.load_level(new_current_level)


if __name__ == '__main__':
    main()
