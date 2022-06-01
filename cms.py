#!usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
import os
import sys
from colorama import Fore
from multiprocessing.pool import ThreadPool
reload(sys)

banner = """
		 ______ _  ___   ___ _______ ____  ___  ___ ____
		/ __/  ' \(_-<  (_-</ __/ _ `/ _ \/ _ \/ -_) __/
		\__/_/_/_/___/ /___/\__/\_,_/_//_/_//_/\__/_/   (Priv8 Tools)

 		[+] Author : Cyber Ghost Malaya
 		[+] Github : https://github.com/CyberGhostMalaya
 		[+] Command : python2 cms.py list.txt 
 		[~] Quote  : It is better to be hated for what you are than to be loved for what you are not.
"""

os.system('cls' if os.name == 'nt' else 'clear')

if os.path.isdir("result")==False:os.system("mkdir result")
def scan(site):
	try:
	 if "http" in site:
	 	url = site
	 else:
	 	url = "http://" + site
	 r = requests.get(url,timeout=10)
	 #Wordpress
	 if "/wp-content/" in r.text or"/wp-login.php" in r.text or "/wp-admin/" in r.text:
		 print("[~] Wordpress")
	 	 open("result/wordpress.txt","a+").write(url +"\n")
	 #Joomla
	 elif "/Joomla!" in r.text or "/index.php?option=com_" in r.text or "/administrator/index.php" in r.text or "/administrator/" in r.text or "/administrator/manifests/files/joomla.xml" in r.text or "/<version>(.*?)<\/version>" in r.text or "/language/en-GB/en-GB.xml" in r.text or "<version>(.*?)<\/version>" in r.text:
		print("[~] Joomla")
		open("result/joomla.txt","a+").write(url +"\n")
	#Drupal
	 elif "/sites/default" in r.text:
		print("[~] Drupal ")
		open("result/drupal.txt","a+").write(url + "\n")
		#Opencart
	 elif "/index.php?route=common/home" in r.text:
		print("[~] Opencart")
		open("result/opencart.txt","a+").write(url + "\n")
	#Laravel PHPUnit
	 elif "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php" in r.text:
		print("[~] Laravel PHPUNIT")
		open("result/laravel_phpunit.txt","a+").write(url + "\n")
	#Jquery File Upload
	 elif "/assets/global/plugins/jquery-file-upload/server/php/" in r.text or "/jQuery/server/php" in r.text:
		print("[~] Jqueury file upload")
		open("result/jquery_file_upload.txt","a+").write(url + "\n")
	# 00. CMS NOT FOUND / NOT WORKING
	 else:
		 print("[!] Unknwown")
		 open("result/unknown.txt","a+").write(url + "\n")
	except:
		 print("[+] Bruhh Not Working")
		 pass
try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
		 ______ _  ___   ___ _______ ____  ___  ___ ____
		/ __/  ' \(_-<  (_-</ __/ _ `/ _ \/ _ \/ -_) __/
		\__/_/_/_/___/ /___/\__/\_,_/_//_/_//_/\__/_/   (Priv8 Tools)

 		[+] Author : Cyber Ghost Malaya
 		[+] Github : https://github.com/CyberGhostMalaya
 		[~] Quote  : It is better to be hated for what you are than to be loved for what you are not.
		""")
	ThreadPool(20).map(scan,open(sys.argv[1]).read().splitlines())
	print ("\n")
	print(Fore.RED("[\/] Result Saved In /result"))
except IndexError:exit("[!] Use: python2 cms.py list.txt \n Example: https://target.com/")
except requests.exceptions.ConnectionError:exit("[!] Check Connection")
except KeyboardInterrupt:exit("[!] Ctrl + C Detected [ Exiting... ]")
except IOError:exit("[!] File Does Not Exit")

sys.exit()
