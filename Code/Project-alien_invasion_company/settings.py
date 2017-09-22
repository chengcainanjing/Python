#coding=utf-8
 
#====================
#File: settings.py
#Author: Cheng Cai
#Date: 2017-09-20
#====================

class Settings():
	#�洢�����������֡����������õ���

	def __init__(self):
		#��ʼ����Ϸ������
		#��Ļ����
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		#�ɴ�������
		self.ship_speed_factor = 25
		self.ship_limit = 3
		#�ӵ�����
		self.bullet_speed_factor = 20
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		#����������
		self.alien_speed_factor = 6
		self.fleet_drop_speed = 30
		#fleet_directionΪ1��ʾ�����ƣ�Ϊ-1��ʾ������
		self.fleet_direction = 1
