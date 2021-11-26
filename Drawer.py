import pygame

class Drawer:
    def draw(self, coords, window, sprite_path, sprite_name, animated=False, frames_count=0):
        if not animated:
            sprite = pygame.image.load(f"{sprite_path}/{sprite_name}")
            window.blit(sprite, coords)
        else:
            assert frames_count
