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

turtles = []
last_spawn_time = time.time()

for i in range(50) :
    turtles.append(Turtle())

while True:
    clock.tick(30)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if time.time() - last_spawn_time > user_def.NEXT_GENE_TIME:
        turtles = []
        for i in range(10) :
            turtles.append(Turtle())
        last_spawn_time = time.time()

    for turtle in turtles:
        turtle.rotate()
        turtle.forword()
        turtle.draw(screen)

    pygame.display.update()