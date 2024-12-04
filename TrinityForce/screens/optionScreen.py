import pygame
from TrinityForce import config

clock = pygame.time.Clock()


def options_screen():
	config.WIN.blit(config.BG, (0, 0))  # Ista pozadina kao na start ekranu

	# Liste rezolucija
	resolutions = [
		(1024, 768), (1280, 720), (1366, 768), (1600, 900),
		(1920, 1080), (2560, 1440), (3840, 2160)
	]

	colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'white']
	dropdown_open = False  # Da li je padajuća lista otvorena
	resolution_rects = []

	running = True
	while running:

		config.WIN.blit(config.BG, (0, 0))  # Ponovo prikazujemo pozadinu
		mouse_pos = pygame.mouse.get_pos()

		# Definisanje dugmadi za "Back"
		back_text = config.BACK_FONT.render("BACK", True, (230, 230, 230))  # Bela boja za tekst
		back_rect = back_text.get_rect(topleft=(config.WIN_WIDTH / 64 + config.horizontal_resolution_offset(),
		                                        config.WIN_HEIGHT / 36 + config.vertical_resolution_offset()))
		if back_rect.collidepoint(mouse_pos):
			back_text = config.BACK_FONT_BIG.render("BACK", True, (230, 230, 230))
		config.WIN.blit(back_text, back_rect.topleft)

		# Definisanje dugmadi za "Select Resolution"
		resolution_button_text = config.RESOLUTION_FONT.render("Select Resolution", True,
		                                                       (230, 230, 230))  # Dugme za rezoluciju
		resolution_button_rect = resolution_button_text.get_rect(
			topleft=(config.WIN_WIDTH / 64 + config.horizontal_resolution_offset(),
			         config.WIN_HEIGHT / 7.2 + config.vertical_resolution_offset()))
		if resolution_button_rect.collidepoint(mouse_pos):
			resolution_button_text = config.BACK_FONT_BIG.render("Select Resolution", True, (230, 230, 230))
		config.WIN.blit(resolution_button_text, resolution_button_rect.topleft)

		resolution_text = []

		for res in resolutions:
			resolution_text.append(config.RESOLUTION_NUMBER_FONT.render(f"{res[0]}x{res[1]}", True, (230, 230, 230)))

		if dropdown_open:
			for i, res in enumerate(resolutions):

				rext = resolution_text[i].get_rect(
					topleft=(resolution_button_rect.left + config.WIN_WIDTH / 30,
					         resolution_button_rect.bottom + config.WIN_WIDTH / 25 + (i * config.WIN_HEIGHT / 12)))
				if rext.collidepoint(mouse_pos):
					resolution_text[i] = config.RESOLUTION_NUMBER_FONT_BIG.render(f"{res[0]}x{res[1]}", True,
					                                                              (230, 230, 230))
				config.WIN.blit(resolution_text[i], rext.topleft)
				resolution_rects.append((res, rext))

		pygame.display.update()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_rect.collidepoint(event.pos):
					print("Back clicked!")
					running = False
				elif resolution_button_rect.collidepoint(event.pos):
					dropdown_open = not dropdown_open
				elif dropdown_open:
					for res, rect in resolution_rects:
						if rect.collidepoint(event.pos):
							config.set_resolution(res)
							print(f"Selected resolution: {res[0]}x{res[1]}")
							dropdown_open = False
							resolution_rects = []
							break
	clock.tick(config.CLOCK_RATE)
