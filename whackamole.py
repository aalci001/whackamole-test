import pygame
import random
screen = pygame.display.set_mode((640, 512))
screen.fill("purple")
size = 32
BOARD_ROWS = 16
BOARD_COLS = 20
width = 640
height = 512
space = 0


mole_image = pygame.image.load("mole.png")
m_rect = mole_image.get_rect()

def mole():
    x = random.randint(0, width - BOARD_ROWS // size)
    y = random.randint(0, height - BOARD_COLS // size)
    m_rect.topleft = (x,y)

m_rect.x = random.randint(0, width -  BOARD_COLS // size)
m_rect.y = random.randint(0, height - BOARD_ROWS // size)
def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen,"dark blue",(0, i * size),(width, i * size))
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen,'dark blue',(i * size, 0),(i * size, height))
def main():
    try:
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if m_rect.collidepoint(event.pos):
                        mole()
            draw_grid()
            screen.blit(mole_image, m_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
