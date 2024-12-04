import pygame

from TrinityForce import config
from TrinityForce.screens.optionScreen import options_screen

clock = pygame.time.Clock()

config.set_settings()


def start_screen():
	config.WIN.blit(config.BG, (0, 0))

	# Definicija opcija i njihovih pozicija
	options = ["PLAY", "OPTIONS", "QUIT"]
	option_rects = []

	running = True
	while running:

		fonts = {
			"PLAY": config.PLAY_TEXT,
			"OPTIONS": config.OPTION_TEXT,
			"QUIT": config.QUIT_TEXT
		}

		big_fonts = {
			"PLAY": config.PLAY_TEXT_BIG,
			"OPTIONS": config.OPTION_TEXT_BIG,
			"QUIT": config.QUIT_TEXT_BIG
		}
		config.WIN.blit(config.BG, (0, 0))  # Očisti ekran pre crtanja

		mouse_pos = pygame.mouse.get_pos()  # Pozicija miša
		option_rects = []  # Osveži pravougaonike za hover

		# Crtanje opcija
		for i, option in enumerate(options):
			# Odabir fonta na osnovu pozicije miša
			if fonts[option].render(option, True, (255, 255, 255)).get_rect(
					center=(config.WIN_WIDTH / 2 + config.horizontal_resolution_offset(),
					        config.WIN_HEIGHT / 2 + config.WIN_HEIGHT / 9.23 + i * config.WIN_HEIGHT / 12 + config.vertical_resolution_offset())).collidepoint(
				mouse_pos):
				font = big_fonts[option]  # Povećan font
			else:
				font = fonts[option]  # Originalni font

			# Renderovanje teksta
			text = font.render(option, True,
			                   (209, 29, 59) if option == "PLAY" else (21, 46, 209) if option == "OPTIONS" else (
				                   255, 255, 255))
			rect = text.get_rect(center=(
				config.WIN_WIDTH // 2 + config.horizontal_resolution_offset(),
				config.WIN_HEIGHT // 2 + config.WIN_HEIGHT / 9.23 + i * config.WIN_HEIGHT / 12 + config.vertical_resolution_offset()))
			config.WIN.blit(text, rect.topleft)
			option_rects.append((option, rect))  # Čuvamo tekst i pravougaonik za klik detekciju

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				for option, rect in option_rects:
					if rect.collidepoint(event.pos):  # Provera da li je klik unutar pravougaonika
						if option == "PLAY":
							print("Play clicked!")  # Ovde pokrećeš igru
						elif option == "OPTIONS":
							print("Options clicked!")
							options_screen()
						elif option == "QUIT":
							pygame.quit()
							exit()
		clock.tick(config.CLOCK_RATE)
