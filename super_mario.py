import sys

import pygame

from src.entities import Player
from src.utils import load_image


class SuperMario:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Super Mario Bros")
        self.window = pygame.display.set_mode((640, 480))

        self.diplay = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {"player": load_image("entities/mario_base.png")}

        self.player = Player(self, "player", (50, 50), (16, 16))

    def run(self):
        while True:
            self.diplay.fill((136, 134, 255))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.diplay)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_UP:
                #         self.movement[0] = True
                #     if event.key == pygame.K_DOWN:
                #         self.movement[1] = True
                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_UP:
                #         self.movement[0] = False
                #     if event.key == pygame.K_DOWN:
                #         self.movement[1] = False

            keys = pygame.key.get_pressed()
            self.movement[0] = keys[pygame.K_LEFT]
            self.movement[1] = keys[pygame.K_RIGHT]

            self.window.blit(
                pygame.transform.scale(self.diplay, self.window.get_size()), (0, 0)
            )
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = SuperMario()
    game.run()
