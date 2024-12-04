import copy
import math
import pygame
import config
from TrinityForce.screens.startScreen import start_screen

pygame.init()
pygame.mixer.init()


# Ikonica
icon = pygame.image.load('assets/images/logo.png')
pygame.display.set_icon(icon)

# Muzika
pygame.mixer.music.load('assets/sounds/Soundtrack.mp3')
pygame.mixer.music.set_volume(0) # TREBA 0.1 ALI ME SMORILO DA GU SAMO SLUSAM
pygame.mixer.music.play(-1, 0, 10000)


def drwa_hexsagon_n(hex_size):
	radius = 90
	a = radius
	h = radius * math.sqrt(3) / 2

	main_diagonal = []
	center_x, center_y = config.WIN_WIDTH // 2, config.WIN_HEIGHT // 2
	for i in range(0 - hex_size + 1, hex_size):
		main_diagonal.append((center_x + a / 2 * i, center_y + h * i))

	hexagon_NxN = set(copy.copy(main_diagonal))

	for i_node in enumerate(main_diagonal):
		if i_node[0] == hex_size - 1:
			continue

		if i_node[0] < hex_size - 1:
			for i in range(1, hex_size):
				hexagon_NxN.add((i_node[1][0] + a * i, i_node[1][1]))
				hexagon_NxN.add((i_node[1][0] - a / 2 * i, i_node[1][1] + h * i))

		if i_node[0] > hex_size - 1:
			for i in range(1, hex_size):
				hexagon_NxN.add((i_node[1][0] + a / 2 * i, i_node[1][1] - h * i))
				hexagon_NxN.add((i_node[1][0] - a * i, i_node[1][1]))

	for x, y in hexagon_NxN:
		pygame.draw.circle(config.WIN, (0, 0, 0), (int(x), int(y)), 8)

def draw_buttons():
	button_texts = ["Very Small", "Small", "Medium", "Large", "Extra Large"]
	for i, text in enumerate(button_texts):
		pygame.draw.rect(config.WIN, (0, 0, 0), (50, 50 + i * 60, 200, 50))
		font = pygame.font.Font(None, 36)
		rendered_text = font.render(text, True, (255, 255, 255))
		config.WIN.blit(rendered_text, (60, 60 + i * 60))

def not_start_screen():
	running = True
	selected_grid_size = 0
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = event.pos
				for i, size in enumerate([4, 5, 6, 7, 8]):
					if 50 <= mouse_x <= 250 and 50 + i * 60 <= mouse_y <= 100 + i * 60:
						selected_grid_size = size

		#not_draw_scene(selected_grid_size)

	# Izlazak iz Pygame-a
	pygame.quit()

def main():
	start_screen()

	# Izlazak iz Pygame-a
	pygame.quit()

if __name__ == '__main__':
	main()
