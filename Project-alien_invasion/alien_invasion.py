#coding=utf-8

import pygame

from settings import Settings
from ship import Ship
import game_functions  as gf

def run_game():
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#���ñ���ɫ
	#bg_color = (230, 230, 230)
	
	#����һ�ҷɴ�
	ship = Ship(ai_settings,screen)
	
	#��ʼ��Ϸ����ѭ��
	while True:
		
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		#����һ�δ�����ģ��game_functions��
		##import sys
		##���Ӽ��̺�����¼�
		# for event in pygame.event.get():
			# if event.type == pygame.QUIT:
				# sys.exit()
		
		#����һ�δ�����ģ��game_functions��
		##ÿ��ѭ��ʱ���ػ���Ļ
		#screen.fill(ai_settings.bg_color)
		#ship.blitme()
		
		#����һ�δ�����ģ��game_functions��
		##��������Ƶ���Ļ�ɼ�
		#pygame.display.flip()

run_game()

		