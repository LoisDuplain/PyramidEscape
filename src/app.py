import pygame
import Utils
import CONSTANTS
from level.Level import Level

current_level = None


def main():
    global current_level
    pygame.init()
    screen = pygame.display.set_mode((CONSTANTS.CONSTANT_WINDOW_WIDTH, CONSTANTS.CONSTANT_WINDOW_HEIGHT))
    pygame.display.set_caption("Pyramid Escape")

    current_level = Level("main-menu.lvl")

    last_update_date = Utils.get_current_time_millis()
    last_render_date = Utils.get_current_time_millis()

    run = True
    while run:
        # Update level
        update_delta_time = Utils.get_current_time_millis() - last_update_date
        if update_delta_time >= 1000/60:
            last_update_date = Utils.get_current_time_millis()
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
                
        render_delta_time = Utils.get_current_time_millis() - last_render_date
        if render_delta_time >= 1000/30:
            last_render_date = Utils.get_current_time_millis()
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
