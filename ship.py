import pygame

class Ship:
    """Classe pour gérer la fusée."""

    def __init__(self, ai_game):
        """
        Initialiser la fusée et définir sa position initiale.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Charger l'image de fusée et obtenir son rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Placer chaque nouvelle fusée au centre et en bas 
        # de l'ecran
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dessiner la fusée à son emplacement actuel."""
        self.screen.blit(self.image, self.rect)