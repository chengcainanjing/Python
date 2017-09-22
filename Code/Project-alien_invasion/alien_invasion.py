#coding=utf-8

#====================
#File: alien_invasion.py
#Author: Cheng Cai
#Date: 2017-09-20
#====================

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions  as gf


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,\
			ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船、一个用于存储子弹的编组和一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	#创建一群外星人
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#开始游戏的主循环
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()

		
