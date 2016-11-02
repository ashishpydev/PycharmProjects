from datetime import datetime
import requests


class InstaBot:
	url = 'https://www.instagram.com/'
	url_login = 'https://www.instagram.com/accounts/login/ajax/'
	
	def __init__(self, login="i_cynefin", password="speedo", tag_list=['nature', 'wild', 'bird']):
		self.tag_list = tag_list
		
		# get the session
		self.s = requests.Session()
		
		# convert login to lower
		self.user_login = login.lower()
		self.user_password = password
		self.login()
		
	def login(self):
		log_string = 'Trying to login as %s...\n' % (self.user_login)
		print(log_string)
		self.login_post = {'username': self.user_login, 'password': self.user_password}
		r = self.s.get(self.url)
		self.s.headers.update({'Connection': 'keep-alive',
								 'Host': 'www.instagram.com',
								 'Referer': 'https://www.instagram.com/'})
		self.s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
		login = self.s.post(self.url_login, data=self.login_post)
		self.s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
		if login.status_code == 200:
			r = self.s.get(self.url)
			finder = r.text.find(self.user_login)
			if finder != -1:
				self.login_status = True
				log_string = '%s login success!' % (self.user_login)
				print(log_string)
			else:
				self.login_status = False
				print('Login error! Check your login data!')
		else:
			print('Login error! Connection error!')

insta = InstaBot()
