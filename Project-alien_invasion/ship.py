#coding=utf-8

import pygame

#import os

class Ship():
	def __init__(self, ai_settings, screen):		#�ڶ���������ָ��Ҫ���ɴ�������ʲô�ط�
		#��ʼ���ɴ����������ʼ��λ��
		self.screen =screen
		self.ai_settings = ai_settings
		
		#���طɴ�ͼ�񲢻������Ӿ���
		#path = os.path.dirname(__file__)
		#print path
		#print os.getcwd()
		#self.image = pygame.image.load(os.path.join(path, 'ship.bmp')) 
		#self.image = pygame.image.load((path + '\images\ship.bmp')) 
		self.image = pygame.image.load('images/ship.bmp') 
		#����pygame.image.load()
		#�����������һ����ʾ�ɴ���surface��
		#�����surface�洢��self.image��		
		self.rect = self.image.get_rect()
		#get_rect()��ȡ��Ӧ��surface����rect
		self.screen_rect = screen.get_rect()
		#����Ļ�ľ��δ洢��self.screen_rect��
		
		#��ÿ���·ɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx
		#self.rect.centerx(�ɴ����ĵ�x����)����Ϊ��Ļ�ľ�������centerx
		self.rect.bottom = self.screen_rect.bottom
		#self.rect.bottom���ɴ��±�Ե��y���꣩����Ϊ��ʾ��Ļ�ľ��ε�����bottom
		
		#�ڷɴ�������center�д洢С��ֵ
		self.center = float(self.rect.centerx)
		
		#�ƶ���־
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		#�����ƶ���־�����ɴ���λ��
		#���·ɴ���centerֵ��������rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		#����self.center����rect����
		self.rect.centerx = self.center
		
	def blitme(self):
		#��ָ��λ�û��Ʒɴ�
		self.screen.blit(self.image, self.rect)
		
