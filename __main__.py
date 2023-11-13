import pygame     # python game 패키지 사용
import sys        # 시스템 함수를 사용하기 위함
import time       # sleep 등 시간 함수 사용을 위함
import random     # 랜덤 백터를 사용하기 위함
import math       # 삼각함수를 사용하기 위함
import user_def   # 사용자 정의 헤더
import numpy as np
from ssu_turtle import Turtle # 거북이 클래스

pygame.init()
pygame.display.set_caption("숭실 거북이 만들기")
screen = pygame.display.set_mode((user_def.WIDTH, user_def.HEIGHT))
clock = pygame.time.Clock()

jangamul = pygame.transform.scale(pygame.image.load("./blackreact.png"), (user_def.JANG_WIDTH, user_def.JANG_HEIGHT)).convert_alpha()
target   = pygame.transform.scale(pygame.image.load("./blackreact.png"), (user_def.TARGET_WIDTH, user_def.TARGET_HEIGHT)).convert_alpha()
new_turtles = []
old_turtles = []
last_spawn_time = time.time()

# 1세대 거북이 생성
for i in range(user_def.TURTLE_COUNT) :
    new_turtles.append(Turtle(True, []))

def next_gene_combine() : 
    global new_turtles
    global old_turtles
    old_turtles = new_turtles
    new_turtles = []
    
    gene = []
    percent = []

    for idx in range(user_def.TURTLE_COUNT) :
        if(old_turtles[idx].crush(jangamul)) : continue
        gene.append(idx)
        p = 200 - old_turtles[idx].distance()
        if(p < 20) : percent.append(20)
        else : percent.append(p)
        

    for idx in range(user_def.TURTLE_COUNT) :
        gene1 = old_turtles[random.choices(gene, percent)[0]].gene
        gene2 = old_turtles[random.choices(gene, percent)[0]].gene

        new_gene = []
        
        random_point = random.randint(1, user_def.CLOCK_TICK * user_def.NEXT_GENE_TIME - 1)

        new_gene = np.append(gene1[:random_point], gene2[random_point:])
        new_turtles.append(Turtle(False, new_gene))
    
    for idx in range(user_def.MUTATION_COUNT) :
        new_turtles[idx].gene[random.randint(0, user_def.CLOCK_TICK * user_def.NEXT_GENE_TIME)] = random.randint(-30, 30)
        

step_idx = 0
while True:
    clock.tick(user_def.CLOCK_TICK)
    screen.fill((255, 255, 255))
    screen.blit(jangamul, (user_def.JANG_X  , user_def.JANG_Y  ))
    screen.blit(target  , (user_def.TARGET_X, user_def.TARGET_Y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if time.time() - last_spawn_time > user_def.NEXT_GENE_TIME:
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