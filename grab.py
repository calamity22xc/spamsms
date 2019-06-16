#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by DECOMPILE•MARSHAL
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;32m
   _  _     \033[1;36mSPAM SMS (GRAB) UNLIMITED\033[1;32m
 _| || |_   \033[1;31mAuthor : 22XC•C4L4MITY\033[1;32m
|_  ..  _|  \033[1;31mTEAM : 22XploiterCrew\033[1;32m
|_      _|  \033[1;31mPESAN : JANGAN RECODE YA SU\033[1;32m
  |_||_| 
""")
	no = input("\033[1;37m[?] NOMOR (Pakai 62 Cok) =>\033[1;36m ")
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
