# -*- coding: utf-8 -*-
# Author: @Dyl4n1993
# Crew: Cursed Eyes Crew

from datetime import datetime
import requests
import os
import time

os.system("clear||cls")
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
d = raw_input("Deseja salvar os subdominios em um arquivo? S/n ~> ")
os.system("clear||cls")
print """
[!] 𝖙𝖔𝖔𝖑 𝖋𝖊𝖎𝖙𝖆 𝖕𝖔𝖗 @Dyl4n1993 [!]
[!] 𝕱𝖗𝖔𝖒: Cursed Eyes Crew [!]
"""
time.sleep(1.0)
os.system("clear||cls")
print """
╔═╗┬ ┬┌┐ ╔═╗┬┌┐┌┌┬┐┌─┐┬─┐
╚═╗│ │├┴┐╠╣ ││││ ││├┤ ├┬┘
╚═╝└─┘└─┘╚  ┴┘└┘─┴┘└─┘┴└─

[!] {} [!]
""".format(date)
t = raw_input("ᴛᴀʀɢᴇᴛ:~> ")
r = requests.get("http://{}/".format(t))
print "sᴛᴀᴛᴜs ᴄᴏᴅᴇ:"
print r.status_code
print ""
if d == "n":
	os.system("curl https://api.hackertarget.com/hostsearch/?q={}".format(t))
	print ""
	print ""
	print "*** 𝙴𝚗𝚍 ***\n\r"
if d == "s":
        os.system("curl https://api.hackertarget.com/hostsearch/?q={} -o subdominios.txt 2>/dev/null".format(t))
	print ""
	print "[+] dominios salvos em ~> subdominios.txt [+]"
	print ""
	os.system("cat subdominios.txt")
        print ""
        print ""
        print "*** 𝙴𝚗𝚍 ***\n\r"

if d == "N":
        os.system("curl https://api.hackertarget.com/hostsearch/?q={}".format(t))
        print ""
        print ""
        print "*** 𝙴𝚗𝚍 ***\n\r"
if d == "S":
        os.system("curl https://api.hackertarget.com/hostsearch/?q={} -o subdominios.txt 2>/dev/null")
        print ""
        print "[+] dominios salvos em ~> subdominios.txt [+]"
	print ""
        os.system("cat subdominios.txt")
        print ""
        print ""
        print "*** 𝙴𝚗𝚍 ***\n\r"

