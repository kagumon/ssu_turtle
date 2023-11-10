import numpy as np
import random   # 랜덤 백터를 사용하기 위함
import pygame   # python game 패키지 사용
import math     # 삼각함수를 사용하기 위함
import user_def # 사용자 정의 헤더

class Turtle(object):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("./t.png"), (15, 17)).convert_alpha()
        self.x = user_def.WIDTH / 2 - self.image.get_width() / 2
        self.y = 300
        self.head = random.randint(0, 361)
        self.rotated_image = pygame.transform.rotate(self.image, self.head)
        self.rotate_speed = random.randint(1, 3)
        print("%f %f %f" % (self.head, math.cos(math.pi*(self.head / 180)), math.sin(math.pi*(self.head / 180))))

    def rotate(self):
        self.head += random.randint(-30, 30)
        self.rotated_image = pygame.transform.rotate(self.image, self.head)

    def forword(self):
        self.x -= math.sin(math.pi*(self.head / 180)) * 1.5
        self.y -= math.cos(math.pi*(self.head / 180)) * 1.5

    def draw(self, screen):
        screen.blit(self.rotated_image, (self.x + self.image.get_width() / 2 - self.rotated_image.get_width() / 2,
                                         self.y + self.image.get_height() / 2 - self.rotated_image.get_height() / 2))