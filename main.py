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

bg = obx('assets/bg.jpg', 0, 0, 1920, 1080)
sun = obx('assets/sun.png', 1275, 300, 300, 300)
# 1 МЕЛЬНИЦА
house = obx('assets\МельницаДом.png', 100, 590, 500, 500)
wood = obx('assets\wood.png', 360, 740, 75, 75)
knife1 = obx('assets\МельницаЛопости.png', 360, 740, 200, 100)
knife2 = obx('assets\МельницаЛопости.png', 360, 740, 200, 100)
knife3 = obx('assets\МельницаЛопости.png', 360, 740, 200, 100)
knife4 = obx('assets\МельницаЛопости.png', 360, 740, 200, 100)
vectorLen = 0.5

#2 МЕЛЬНИЦА
house2 = obx('assets\МельницаДом.png', 500, 590, 500, 500)
wood2 = obx('assets\wood.png', 760, 740, 75, 75)
knife5 = obx('assets\МельницаЛопости2.png', 760, 740, 200, 100)
knife6 = obx('assets\МельницаЛопости2.png', 760, 740, 200, 100)
knife7 = obx('assets\МельницаЛопости2.png', 760, 740, 200, 100)
knife8 = obx('assets\МельницаЛопости2.png', 760, 740, 200, 100)

#3 МЕЛЬНИЦА
house3 = obx('assets\МельницаДом.png', 900, 590, 500, 500)
wood3 = obx('assets\wood.png', 1160, 740, 75, 75)
knife9 = obx('assets\МельницаЛопости.png', 1160, 740, 200, 100)
knife10 = obx('assets\МельницаЛопости.png', 1160, 740, 200, 100)
knife11 = obx('assets\МельницаЛопости.png', 1160, 740, 200, 100)
knife12 = obx('assets\МельницаЛопости.png', 1160, 740, 200, 100)

#3 МЕЛЬНИЦА
house4 = obx('assets\МельницаДом.png', 1300, 590, 500, 500)
wood4 = obx('assets\wood.png', 1560, 740, 75, 75)
knife13 = obx('assets\МельницаЛопости2.png', 1560, 740, 200, 100)
knife14 = obx('assets\МельницаЛопости2.png', 1560, 740, 200, 100)
knife15 = obx('assets\МельницаЛопости2.png', 1560, 740, 200, 100)
knife16 = obx('assets\МельницаЛопости2.png', 1560, 740, 200, 100)
al = 0
al2 = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    al+=.1
    al2 -= .1
    knife1.rec.x = knife1.x + 3 + 100 * cos(-al / 57)
    knife1.rec.y = knife1.y + 100 * sin(-al / 57)

    knife2.rec.x = knife2.x + 3 + 100 * cos(-al / 57 + pi)
    knife2.rec.y = knife2.y + 100 * sin(-al / 57 + pi)

    knife3.rec.x = knife3.x + 3 + 100 * cos(-al / 57 + pi / 2)
    knife3.rec.y = knife3.y + 100 * sin(-al / 57 + pi / 2)

    knife4.rec.x = knife4.x + 3 + 100 * cos(-al / 57 + pi * 3 / 2)
    knife4.rec.y = knife4.y + 100 * sin(-al / 57 + pi * 3 / 2)

    # 2 МЕЛЬНИЦА
    knife5.rec.x = knife5.x + 3 + 100 * cos(-al2 / 57)
    knife5.rec.y = knife5.y + 100 * sin(-al2 / 57)

    knife6.rec.x = knife6.x + 3 + 100 * cos(-al2 / 57 + pi)
    knife6.rec.y = knife6.y + 100 * sin(-al2 / 57 + pi)

    knife7.rec.x = knife7.x + 3 + 100 * cos(-al2 / 57 + pi / 2)
    knife7.rec.y = knife7.y + 100 * sin(-al2 / 57 + pi / 2)

    knife8.rec.x = knife8.x + 3 + 100 * cos(-al2 / 57 + pi * 3 / 2)
    knife8.rec.y = knife8.y + 100 * sin(-al2 / 57 + pi * 3 / 2)

    # 3 МЕЛЬНИЦА
    knife9.rec.x = knife9.x + 3 + 100 * cos(-al / 57)
    knife9.rec.y = knife9.y + 100 * sin(-al / 57)

    knife10.rec.x = knife9.x + 3 + 100 * cos(-al / 57 + pi)
    knife10.rec.y = knife10.y + 100 * sin(-al / 57 + pi)

    knife11.rec.x = knife11.x + 3 + 100 * cos(-al / 57 + pi / 2)
    knife11.rec.y = knife11.y + 100 * sin(-al / 57 + pi / 2)

    knife12.rec.x = knife12.x + 3 + 100 * cos(-al / 57 + pi * 3 / 2)
    knife12.rec.y = knife12.y + 100 * sin(-al / 57 + pi * 3 / 2)

    # 4 МЕЛЬНИЦА
    knife13.rec.x = knife13.x + 3 + 100 * cos(-al2 / 57)
    knife13.rec.y = knife13.y + 100 * sin(-al2 / 57)

    knife14.rec.x = knife14.x + 3 + 100 * cos(-al2 / 57 + pi)
    knife14.rec.y = knife14.y + 100 * sin(-al2 / 57 + pi)

    knife15.rec.x = knife15.x + 3 + 100 * cos(-al2 / 57 + pi / 2)
    knife15.rec.y = knife15.y + 100 * sin(-al2 / 57 + pi / 2)

    knife16.rec.x = knife16.x + 3 + 100 * cos(-al2 / 57 + pi * 3 / 2)
    knife16.rec.y = knife16.y + 100 * sin(-al2 / 57 + pi * 3 / 2)

    #knife5.rec.x = knife4.x + 3 + 100 * cos(-al / 57 + pi / 4 * 3)
    #knife5.rec.y = knife4.y + 100 * sin(-al / 57 + pi / 4 * 3)

    mouseX = wood.x + 0.1 * cos(-al / 57)
    mouseY = wood.y + 0.1 * sin(-al / 57)
    vX = mouseX - wood.x
    vY = mouseY - wood.y

    angle = atan2(vY, vX)
    # vX, vY =  cos(angle) * vectorLen, sin(angle) * vectorLen
    wood_rotate = pg.transform.rotate(wood.pic, -angle * 57)
    knife1_rotate = pg.transform.rotate(knife1.pic, -angle * 57 + 180)
    knife2_rotate = pg.transform.rotate(knife2.pic, -angle * 57 + 0)
    knife3_rotate = pg.transform.rotate(knife3.pic, -angle * 57 + 90)
    knife4_rotate = pg.transform.rotate(knife4.pic, -angle * 57 + 270)
    
    wood2_rotate = pg.transform.rotate(wood.pic, angle * 57)
    knife5_rotate = pg.transform.rotate(knife1.pic, angle * 57 + 180)
    knife6_rotate = pg.transform.rotate(knife2.pic, angle * 57 + 0)
    knife7_rotate = pg.transform.rotate(knife3.pic, angle * 57 + 90)
    knife8_rotate = pg.transform.rotate(knife4.pic, angle * 57 + 270)

    wood3_rotate = pg.transform.rotate(wood.pic, -angle * 57)
    knife9_rotate = pg.transform.rotate(knife1.pic, -angle * 57 + 180)
    knife10_rotate = pg.transform.rotate(knife2.pic, -angle * 57 + 0)
    knife11_rotate = pg.transform.rotate(knife3.pic, -angle * 57 + 90)
    knife12_rotate = pg.transform.rotate(knife4.pic, -angle * 57 + 270)

    wood4_rotate = pg.transform.rotate(wood.pic, angle * 57)
    knife13_rotate = pg.transform.rotate(knife1.pic, angle * 57 + 180)
    knife14_rotate = pg.transform.rotate(knife2.pic, angle * 57 + 0)
    knife15_rotate = pg.transform.rotate(knife3.pic, angle * 57 + 90)
    knife16_rotate = pg.transform.rotate(knife4.pic, angle * 57 + 270)
    #knife5_rotate = pg.transform.rotate(knife5.pic, -angle * 57 + 45)

    sun_rotate = pg.transform.rotate(sun.pic, angle * 57)

    window.blit(bg.pic, [bg.x, bg.y])
    window.blit(house.pic, [house.x, house.y])
    window.blit(house2.pic, [house2.x, house2.y])
    window.blit(house3.pic, [house3.x, house3.y])
    window.blit(house4.pic, [house4.x, house4.y])
    # window.blit(ball.pic,ball.rec)
    window.blit(knife1_rotate, knife1_rotate.get_rect(center=(knife1.rec.x, knife1.rec.y)))
    window.blit(knife2_rotate, knife2_rotate.get_rect(center=(knife2.rec.x, knife2.rec.y)))
    window.blit(knife3_rotate, knife3_rotate.get_rect(center=(knife3.rec.x, knife3.rec.y)))
    window.blit(knife4_rotate, knife4_rotate.get_rect(center=(knife4.rec.x, knife4.rec.y)))

    window.blit(knife5_rotate, knife5_rotate.get_rect(center=(knife5.rec.x, knife5.rec.y)))
    window.blit(knife6_rotate, knife6_rotate.get_rect(center=(knife6.rec.x, knife6.rec.y)))
    window.blit(knife7_rotate, knife7_rotate.get_rect(center=(knife7.rec.x, knife7.rec.y)))
    window.blit(knife8_rotate, knife8_rotate.get_rect(center=(knife8.rec.x, knife8.rec.y)))

    window.blit(knife9_rotate, knife9_rotate.get_rect(center=(knife9.rec.x, knife9.rec.y)))
    window.blit(knife10_rotate, knife10_rotate.get_rect(center=(knife10.rec.x, knife10.rec.y)))
    window.blit(knife11_rotate, knife11_rotate.get_rect(center=(knife11.rec.x, knife11.rec.y)))
    window.blit(knife12_rotate, knife12_rotate.get_rect(center=(knife12.rec.x, knife12.rec.y)))

    window.blit(knife13_rotate, knife13_rotate.get_rect(center=(knife13.rec.x, knife13.rec.y)))
    window.blit(knife14_rotate, knife14_rotate.get_rect(center=(knife14.rec.x, knife14.rec.y)))
    window.blit(knife15_rotate, knife15_rotate.get_rect(center=(knife15.rec.x, knife15.rec.y)))
    window.blit(knife16_rotate, knife16_rotate.get_rect(center=(knife16.rec.x, knife16.rec.y)))

    window.blit(wood_rotate, wood_rotate.get_rect(center=(wood.rec.x, wood.rec.y)))
    window.blit(wood2_rotate, wood2_rotate.get_rect(center=(wood2.rec.x, wood2.rec.y)))
    window.blit(wood3_rotate, wood3_rotate.get_rect(center=(wood3.rec.x, wood3.rec.y)))
    window.blit(wood4_rotate, wood4_rotate.get_rect(center=(wood4.rec.x, wood4.rec.y)))

    window.blit(sun_rotate, sun_rotate.get_rect(center=(sun.rec.x, sun.rec.y)))
    #window.blit(knife5_rotate, knife5_rotate.get_rect(center=(knife5.rec.x, knife5.rec.y)))

    pg.display.flip()

pg.quit()