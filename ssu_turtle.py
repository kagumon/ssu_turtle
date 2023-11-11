import numpy as np
import random   # 랜덤 백터를 사용하기 위함
import pygame   # python game 패키지 사용
import math     # 삼각함수를 사용하기 위함
import user_def # 사용자 정의 헤더

class Turtle(object):
    def __init__(self, randyn, gene):
        self.image         = pygame.transform.scale(pygame.image.load("./turtle.png"), (user_def.TURTLE_WIDTH, user_def.TURTLE_HEIGHT)).convert_alpha()
        self.x             = user_def.TURTLE_X
        self.y             = user_def.TURTLE_Y
        self.head          = random.randint(0, 361)
        self.rotated_image = pygame.transform.rotate(self.image, self.head)
        self.rotate_speed  = random.randint(1, 3)
        self.gene          = np.random.randint(-30, 30, size=user_def.CLOCK_TICK * user_def.NEXT_GENE_TIME)

    def rotate(self, idx):
        self.head += self.gene[idx]
        self.rotated_image = pygame.transform.rotate(self.image, self.head)

    def forword(self):
        self.x -= math.sin(math.pi*(self.head / 180)) * user_def.TURTLE_STEP_SIZE
        self.y -= math.cos(math.pi*(self.head / 180)) * user_def.TURTLE_STEP_SIZE

    def draw(self, screen):
        screen.blit(self.rotated_image, (self.x + self.image.get_width() / 2 - self.rotated_image.get_width() / 2,
                                         self.y + self.image.get_height() / 2 - self.rotated_image.get_height() / 2))
    
    def crush(self, jang) :
        turtle        = self.image.get_rect()
        turtle.left   = self.x
        turtle.top    = self.y
        jangamul      = jang.get_rect()
        jangamul.left = user_def.JANG_X
        jangamul.top  = user_def.JANG_Y
        if(turtle.colliderect(jangamul)) :
            return True
        else :
            return False