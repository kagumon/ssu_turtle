import pygame     # python game 패키지 사용
import sys        # 시스템 함수를 사용하기 위함
import time       # sleep 등 시간 함수 사용을 위함
import random     # 랜덤 백터를 사용하기 위함
import math       # 삼각함수를 사용하기 위함
import user_def   # 사용자 정의 헤더
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
for i in range(50) :
    new_turtles.append(Turtle(True, []))

def next_gene_combine() : 
    global new_turtles
    global old_turtles
    old_turtles = new_turtles
    new_turtles = []
    for i in range(50) :
        new_turtles.append(Turtle(True, []))
        

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