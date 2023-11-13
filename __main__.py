import pygame     # python game 패키지 사용
import sys        # 시스템 함수를 사용하기 위함
import time       # sleep 등 시간 함수 사용을 위함
import random     # 랜덤 백터를 사용하기 위함
import math       # 삼각함수를 사용하기 위함
import numpy as np

#화면 사이즈
WIDTH = 300
HEIGHT = 500

#초당 이동 횟수
CLOCK_TICK = 30

#세대 체인지 시간
NEXT_GENE_TIME = 7

#세대 체인지 시간
TURTLE_STEP_SIZE = 2

#거북이 개체 수
TURTLE_COUNT = 100
MUTATION_COUNT = 30

#거북이 사이즈 및 정보
TURTLE_WIDTH  = 15
TURTLE_HEIGHT = 17
TURTLE_X      = WIDTH  / 2 - TURTLE_WIDTH  / 2
TURTLE_Y      = HEIGHT - 100 - TURTLE_HEIGHT / 2

#장애물 사이즈 및 정보
JANG_WIDTH  = 150
JANG_HEIGHT = 10
JANG_X      = WIDTH  / 2 - JANG_WIDTH  / 2
JANG_Y      = HEIGHT / 2 - JANG_HEIGHT / 2

#목표물 사이즈 및 정보
TARGET_WIDTH  = 20
TARGET_HEIGHT = 20
TARGET_X      = WIDTH  / 2 - TARGET_WIDTH  / 2
TARGET_Y      = 100 - TARGET_HEIGHT / 2

class Turtle(object):
    def __init__(self, randyn, gene):
        self.image         = pygame.transform.scale(pygame.image.load("./turtle.png"), (TURTLE_WIDTH, TURTLE_HEIGHT)).convert_alpha()
        self.x             = TURTLE_X
        self.y             = TURTLE_Y
        self.head          = 0
        self.rotated_image = pygame.transform.rotate(self.image, self.head)
        self.rotate_speed  = random.randint(1, 3)
        self.gene          = np.random.randint(-30, 30, size=CLOCK_TICK * NEXT_GENE_TIME) if randyn else gene

    def rotate(self, idx):
        if(idx < CLOCK_TICK * NEXT_GENE_TIME) : 
            self.head += self.gene[idx]
        self.rotated_image = pygame.transform.rotate(self.image, self.head)

    def forword(self):
        self.x -= math.sin(math.pi*(self.head / 180)) * TURTLE_STEP_SIZE
        self.y -= math.cos(math.pi*(self.head / 180)) * TURTLE_STEP_SIZE

    def draw(self, screen):
        screen.blit(self.rotated_image, (self.x + self.image.get_width() / 2 - self.rotated_image.get_width() / 2,
                                         self.y + self.image.get_height() / 2 - self.rotated_image.get_height() / 2))
    
    def crush(self, jang) :
        turtle        = self.image.get_rect()
        turtle.left   = self.x
        turtle.top    = self.y
        jangamul      = jang.get_rect()
        jangamul.left = JANG_X
        jangamul.top  = JANG_Y
        if(turtle.colliderect(jangamul)) :
            return True
        else :
            return False
    
    def distance(self) :
        x1 = self.x
        x2 = TARGET_X
        
        y1 = self.y
        y2 = TARGET_Y
 
        a = int(self.x - TARGET_X)
        b = int(self.y - TARGET_Y)
 
        return math.sqrt((a * a) + (b * b))

pygame.init()
pygame.display.set_caption("숭실 거북이 만들기")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

jangamul = pygame.transform.scale(pygame.image.load("./blackreact.png"), (JANG_WIDTH, JANG_HEIGHT)).convert_alpha()
target   = pygame.transform.scale(pygame.image.load("./blackreact.png"), (TARGET_WIDTH, TARGET_HEIGHT)).convert_alpha()
new_turtles = []
old_turtles = []
last_spawn_time = time.time()

# 1세대 거북이 생성
for i in range(TURTLE_COUNT) :
    new_turtles.append(Turtle(True, []))

def next_gene_combine() : 
    global new_turtles
    global old_turtles
    old_turtles = new_turtles
    new_turtles = []
    
    gene = []
    percent = []

    for idx in range(TURTLE_COUNT) :
        if(old_turtles[idx].crush(jangamul)) : continue
        gene.append(idx)
        p = 200 - old_turtles[idx].distance()
        if(p < 20) : percent.append(20)
        else : percent.append(p)
        

    for idx in range(TURTLE_COUNT) :
        gene1 = old_turtles[random.choices(gene, percent)[0]].gene
        gene2 = old_turtles[random.choices(gene, percent)[0]].gene

        new_gene = []
        
        random_point = random.randint(1, CLOCK_TICK * NEXT_GENE_TIME - 1)

        new_gene = np.append(gene1[:random_point], gene2[random_point:])
        new_turtles.append(Turtle(False, new_gene))
    
    for idx in range(MUTATION_COUNT) :
        new_turtles[idx].gene[random.randint(0, CLOCK_TICK * NEXT_GENE_TIME)] = random.randint(-30, 30)
        

step_idx = 0
while True:
    clock.tick(CLOCK_TICK)
    screen.fill((255, 255, 255))
    screen.blit(jangamul, (JANG_X  , JANG_Y  ))
    screen.blit(target  , (TARGET_X, TARGET_Y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if time.time() - last_spawn_time > NEXT_GENE_TIME:
        step_idx = 0
        next_gene_combine()
        last_spawn_time = time.time()

    for turtle in new_turtles:
        if(turtle.crush(jangamul)) :
            continue
        turtle.rotate(step_idx)
        turtle.forword()
        turtle.draw(screen)

    step_idx+=1
    pygame.display.update()