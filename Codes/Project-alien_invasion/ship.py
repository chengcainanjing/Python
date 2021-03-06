#coding=utf-8

#====================
#File: ship.py
#Author: Cheng Cai
#Date: 2017-09-20
#====================

import pygame

#import os

class Ship():
	def __init__(self, ai_settings, screen):		#第二个参数是指定要将飞船绘制在什么地方
		#初始化飞船并设置其初始化位置
		self.screen =screen
		self.ai_settings = ai_settings
		
		#加载飞船图像并获得其外接矩形
		#path = os.path.dirname(__file__)
		#print path
		#print os.getcwd()
		#self.image = pygame.image.load(os.path.join(path, 'ship.bmp')) 
		#self.image = pygame.image.load((path + '\images\ship.bmp')) 
		self.image = pygame.image.load('images/ship.bmp') 
		#调用pygame.image.load()
		#这个函数返回一个表示飞船的surface，
		#将这个surface存储到self.image中		
		self.rect = self.image.get_rect()
		#get_rect()获取相应的surface属性rect
		self.screen_rect = screen.get_rect()
		#将屏幕的矩形存储在self.screen_rect中
		
		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		#self.rect.centerx(飞船中心的x坐标)设置为屏幕的矩形属性centerx
		self.rect.bottom = self.screen_rect.bottom
		#self.rect.bottom（飞船下边缘的y坐标）设置为表示屏幕的矩形的属性bottom
		
		#在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		#根据移动标志调整飞船的位置
		#更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		#根据self.center更新rect对象
		self.rect.centerx = self.center
		
	def blitme(self):
		#在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)
		
