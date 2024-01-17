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
        self.rect = pg.Rect(x, y, x_r, y_r)

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

ball1 = obx('ball.png', 1240, 280, 50, 50)
ball2 = obx('ball.png', 1240, 280, 50, 50)
ball3 = obx('ball.png', 1240, 280, 50, 50)
ball4 = obx('ball.png', 1240, 280, 50, 50)
ball5 = obx('ball.png', 1240, 280, 50, 50)
ball6 = obx('ball.png', 1240, 280, 50, 50)
ball7 = obx('ball.png', 1240, 280, 50, 50)
ball8 = obx('ball.png', 1240, 280, 50, 50)

pg.mixer.music.load("assets/music.mp3")
pg.mixer.music.play(-1)
al = 0
al2 = 0
step = 50
ballall = []
cnt = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # elif event.type == pg.MOUSEBUTTONDOWN:
        #     ballall.append(obx('assets/ball.png',0,0,50,50))
        #     ballall[-1].rect.x = sun.x + vX * step
        #     ballall[-1].rect.y = sun.y + vY * step
        #     if ballall[-1].y < 200:
        #         ballall[-1].x=sun.x+vX * step
        #         ballall[-1].y=sun.y+vY * step
        #     ballall[-1].vX=vX
        #     ballall[-1].vY=vY
        #     ballall[-1].rotate = pg.transform.rotate(ballall[-1].pic, -angle2 * 57)
    al+=.1
    al2 -= .1
    al3 = 1
    cnt += 1
    # for i in range(len(ballall)):
    #     ballall[i].y += 50
    #     al3+=1
    #     ballall[i].rec.x = ballall[i].x + 25 + 100*cos(-al3/57)
    #     ballall[i].rec.y = ballall[i].y + 25 + 100*sin(-al3/57)
    #     vY = 0.1*sin(-al/57)
    #     angle2 = atan2(vY2,vX2)
    #     gun2_rotate = pg.transform.rotate(ballall[i].pic,-angle2 * 57)
    if cnt % 100 == 0:
        ball1.x = 1240
        ball1.y = 280

        ball2.x = 1240
        ball2.y = 280

        ball3.x = 1240
        ball3.y = 280

        ball4.x = 1240
        ball4.y = 280

        ball5.x = 1240
        ball5.y = 280

        ball6.x = 1240
        ball6.y = 280

        ball7.x = 1240
        ball7.y = 280

        ball8.x = 1240
        ball8.y = 280

    ball1.x += 20
    ball2.y += 20
    ball3.x -= 20
    ball4.y -= 20
    ball5.x += 20
    ball5.y += 20
    ball6.x -= 20
    ball6.y -= 20
    ball7.x -= 20
    ball7.y += 20
    ball8.x += 20
    ball8.y -= 20


    vX2 = 240 - sun.x
    vY2 = 50 - sun.y
    angle2 = atan2(vY2, vX2)

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
    window.blit(ball1.pic, [ball1.x, ball1.y])
    window.blit(ball2.pic, [ball2.x, ball2.y])
    window.blit(ball3.pic, [ball3.x, ball3.y])
    window.blit(ball4.pic, [ball4.x, ball4.y])
    window.blit(ball5.pic, [ball5.x, ball5.y])
    window.blit(ball6.pic, [ball6.x, ball6.y])
    window.blit(ball7.pic, [ball7.x, ball7.y])
    window.blit(ball8.pic, [ball8.x, ball8.y])

    pg.display.flip()

pg.quit()