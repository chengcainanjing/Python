#coding=utf-8

import pygame
from pygame.sprite import Group

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
    #����һ�����ڴ洢�ӵ��ı���
    bullets = Group()




    #��ʼ��Ϸ����ѭ��
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
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

		
