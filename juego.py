import pygame, sys

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

class hammer:
    texture = pygame.image.load("hammer.png")
    pos_x: int
    pos_y: int
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

class amongu:
    texture = pygame.image.load("amongu.png")
    pos_x: int
    pos_y: int 
    visible = bool
    time = 1000
    def __init__(self, x, y, vis):
        self.pos_x = x
        self.pos_y = y
        self.visible = vis
    def count(self, speed):
        self.time -= speed
        if self.time <= 0:
            self.visible = not self.visible
            self.time = 1000

cursor = hammer(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

am_1 = amongu(32, 32, False)
am_2 = amongu(260, 32, True)
am_3 = amongu(512, 32, False)
am_4 = amongu(32, 256, False)
am_5 = amongu(260, 256, False)
am_6 = amongu(512, 256, True)

while True:
    am_1.count(1)
    am_2.count(1)
    am_3.count(1)
    am_4.count(1)
    am_5.count(1)
    am_6.count(1)
    cursor.pos_x = pygame.mouse.get_pos()[0]
    cursor.pos_y = pygame.mouse.get_pos()[1]
    screen.fill(black)
    if am_1.visible: screen.blit(am_1.texture, [am_1.pos_x, am_1.pos_y])
    if am_2.visible: screen.blit(am_2.texture, [am_2.pos_x, am_2.pos_y])
    if am_3.visible: screen.blit(am_3.texture, [am_3.pos_x, am_3.pos_y])
    if am_4.visible: screen.blit(am_4.texture, [am_4.pos_x, am_4.pos_y])
    if am_5.visible: screen.blit(am_5.texture, [am_5.pos_x, am_5.pos_y])
    if am_6.visible: screen.blit(am_6.texture, [am_6.pos_x, am_6.pos_y])
    screen.blit(cursor.texture, [cursor.pos_x - 55, cursor.pos_y - 40])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor.pos_x >= 32 and cursor.pos_x <= 160 and cursor.pos_y >= 32 and cursor.pos_y <= 160 and am_1.visible:
                am_1.visible = False
                am_1.time = 1000
            if cursor.pos_x >= 260 and cursor.pos_x <= 388 and cursor.pos_y >= 32 and cursor.pos_y <= 160 and am_2.visible:
                am_2.visible = False
                am_2.time = 1000
            if cursor.pos_x >= 512 and cursor.pos_x <= 640 and cursor.pos_y >= 32 and cursor.pos_y <= 160 and am_3.visible:
                am_3.visible = False
                am_3.time = 1000
            if cursor.pos_x >= 32 and cursor.pos_x <= 160 and cursor.pos_y >= 256 and cursor.pos_y <= 384 and am_4.visible:
                am_4.visible = False
                am_4.time = 1000
            if cursor.pos_x >= 260 and cursor.pos_x <= 388 and cursor.pos_y >= 256 and cursor.pos_y <= 384 and am_5.visible:
                am_5.visible = False
                am_5.time = 1000
            if cursor.pos_x >= 512 and cursor.pos_x <= 640 and cursor.pos_y >= 256 and cursor.pos_y <= 384 and am_6.visible:
                am_6.visible = False
                am_6.time = 1000