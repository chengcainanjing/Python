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
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,\
			ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#����һ�ҷɴ���һ�����ڴ洢�ӵ��ı����һ�������˱���
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	#����һȺ������
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#��ʼ��Ϸ����ѭ��
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()

		
