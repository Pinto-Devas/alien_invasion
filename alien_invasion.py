import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
  #Inicializa o jogo e cria um objeto para a tela
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption('Alien Invasion')

  #Cria uma nova espaçonave
  ship = Ship(screen)

  #Inicia o laço principal do jogo
  while True:

    #Observa eventos do teclado e de mouse
    for event in  pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Deixa a tela mais recente visível
    pygame.display.flip()

run_game()