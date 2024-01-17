import pygame as pg
from math import *
import random


class obx:
    def __init__(self, pic, x, y, x_r, y_r):
        self.pic = pg.image.load(pic)
        self.pic = pg.transform.scale(self.pic, (x_r, y_r))
        self.rec = pg.Rect(x, y, x_r, y_r)
        self.x = x
        self.y = y


pg.init()

window_width = 1920
window_height = 1080

window = pg.display.set_mode((window_width, window_height))
run = True

# 1 МЕЛЬНИЦА
house = obx('assets\МельницаДом.png', 100, 350, 500, 500)
wood = obx('assets\wood.png', 360, 500, 75, 75)
knife = obx('assets\МельницаЛопости.png', 360, 500, 200, 100)
knife2 = obx('assets\МельницаЛопости.png', 360, 500, 200, 100)
knife3 = obx('assets\МельницаЛопости.png', 360, 500, 200, 100)
knife4 = obx('assets\МельницаЛопости.png', 360, 500, 200, 100)
vectorLen = 0.5

al = 0
al2 = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    al+=.1
    knife.rec.x = knife.x + 3 + 100 * cos(-al / 57)
    knife.rec.y = knife.y + 100 * sin(-al / 57)

    knife2.rec.x = knife2.x + 3 + 100 * cos(-al / 57 + pi)
    knife2.rec.y = knife2.y + 100 * sin(-al / 57 + pi)

    knife3.rec.x = knife3.x + 3 + 100 * cos(-al / 57 + pi / 2)
    knife3.rec.y = knife3.y + 100 * sin(-al / 57 + pi / 2)

    knife4.rec.x = knife4.x + 3 + 100 * cos(-al / 57 + pi * 3 / 2)
    knife4.rec.y = knife4.y + 100 * sin(-al / 57 + pi * 3 / 2)

    #knife5.rec.x = knife4.x + 3 + 100 * cos(-al / 57 + pi / 4 * 3)
    #knife5.rec.y = knife4.y + 100 * sin(-al / 57 + pi / 4 * 3)

    mouseX = wood.x + 0.1 * cos(-al / 57)
    mouseY = wood.y + 0.1 * sin(-al / 57)
    vX = mouseX - wood.x
    vY = mouseY - wood.y

    angle = atan2(vY, vX);
    # vX, vY =  cos(angle) * vectorLen, sin(angle) * vectorLen
    wood_rotate = pg.transform.rotate(wood.pic, -angle * 57)
    knife_rotate = pg.transform.rotate(knife.pic, -angle * 57 + 180)
    knife2_rotate = pg.transform.rotate(knife2.pic, -angle * 57 + 0)
    knife3_rotate = pg.transform.rotate(knife3.pic, -angle * 57 + 90)
    knife4_rotate = pg.transform.rotate(knife4.pic, -angle * 57 + 270)
    #knife5_rotate = pg.transform.rotate(knife5.pic, -angle * 57 + 45)

    window.fill(0)
    window.blit(house.pic, [house.x, house.y])
    # window.blit(ball.pic,ball.rec)
    window.blit(knife_rotate, knife_rotate.get_rect(center=(knife.rec.x, knife.rec.y)))
    window.blit(knife2_rotate, knife2_rotate.get_rect(center=(knife2.rec.x, knife2.rec.y)))
    window.blit(knife3_rotate, knife3_rotate.get_rect(center=(knife3.rec.x, knife3.rec.y)))
    window.blit(knife4_rotate, knife4_rotate.get_rect(center=(knife4.rec.x, knife4.rec.y)))

    window.blit(wood_rotate, wood_rotate.get_rect(center=(wood.rec.x, wood.rec.y)))
    #window.blit(knife5_rotate, knife5_rotate.get_rect(center=(knife5.rec.x, knife5.rec.y)))

    pg.display.flip()

pg.quit()