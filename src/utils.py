import pygame

BASE_IMG_PATH = "resources/images/"


def load_image(path: str):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    return img
