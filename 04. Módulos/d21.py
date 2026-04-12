import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o nome do arquivo MP3
pygame.mixer.music.load('C:/Users/marco/OneDrive/Documentos/Curso em Vídeo Python/Modulo1/Aula8/HINO DO VASCO DA GAMA.mp3')

# Reproduz o aúdio
pygame.mixer.music.play()

# Mantém o aúdoio até o usuário encerrar
input('Pressione Enter para encerrar a reprodução...')