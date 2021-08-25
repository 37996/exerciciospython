import pygame
print("Click no play")
print("---------------")

file = 'midia.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
