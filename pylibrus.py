#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize
import getpass
import argparse
import re
import datetime
import time
waitinga = 5

def czekanko(waiting):
	#dotlumaczenia
	#print "Waiting %5d s for the website (if something will crash soon, the chosen waiting time may be too short)..." % waiting
	print "Czekanie %5d s na załadowanie strony (jeżeli coś się zcrashuje, oznacza to że wybrany czas czekanie może być za krótki)..." % waiting
	for waitinglive in range(0,waiting):
		time.wait(1)
		print "       %5d..." % waitinglive


class corobienie:
	def __init__(self,br,polecenia):
			self.polecenia = polecenia
			corobic = self.zdobadzpolecenie()
			if corobic == 'plan':
				self.plan(br, "n")
			elif corobic == 'costam':
				self.costam(br)
			else:
				print u'Błąd w kwestii informacji co robić'
				quit()
	def zdobadzpolecenie(self):
		
	def plan(self,br,dajreada):
		
	def costam(self,br):
		
polecenia = ('plan', 'costam')
br = mechanize.Browser()
br.open('https://dziennik.librus.pl/uczen_index')
br.select_form(name='logowanie')
uzyszk = raw_input('Wpisz nazwę użytkownika:  ')
br['login'] = uzyszk
haselo = getpass.getpass('Wpisz hasło (zabezp. przed pokazaniem na ekr. znaków hasła: JEST):  ')
br['passwd'] = haselo
odpoa = br.submit()

assert br.viewing_html()
print br.title()
print odpoa.geturl()
print odpoa.info() #d
print odpoa.read() #d
while True:
	corobienie(br,polecenia)
