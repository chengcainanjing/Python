#coding=utf-8

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions  as gf


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
	
    #设置背景色
    #bg_color = (230, 230, 230)
	
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()




    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
	#下面一段代码在模块game_functions中
	##import sys
	##监视键盘和鼠标事件
	# for event in pygame.event.get():
		# if event.type == pygame.QUIT:
			# sys.exit()
	
	#下面一段代码在模块game_functions中
	##每次循环时都重绘屏幕
	#screen.fill(ai_settings.bg_color)
	#ship.blitme()
	
	#下面一段代码在模块game_functions中
	##让最近绘制的屏幕可见
	#pygame.display.flip()

run_game()

		
