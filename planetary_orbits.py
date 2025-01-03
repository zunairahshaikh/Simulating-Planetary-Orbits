import pygame
import math

#initialize pygame
pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Planets go wee")

class Planet:
	AU = 149.6e6 * 1000 # in metres
	G = 6.67428e-11
	scale = 250 / AU  # 1AU = 100 pixels
	timeStep = 3600*24 # 1 day

	def __init__(self, x, y, radius, color, mass):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.mass = mass

		self.orbit = []
		self.sun = False
		self.distance_to_sun = 0

		self.x_vel = 0
		self.y_vel = 0

	def draw(self, win):
		x = self.x * self.SCALE + WIDTH / 2    # this formula is to ensure simulation appears in the middle of the screen
		y = self.y * self.SCALE + HEIGHT / 2

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2
				y = y * self.SCALE + HEIGHT / 2
				updated_points.append((x, y))

			pygame.draw.lines(win, self.color, False, updated_points, 2)

		pygame.draw.circle(win, self.color, (x, y), self.radius)
		
		if not self.sun:
			distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
			win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

def main():
    clock = pygame.time.Clock()        
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()
