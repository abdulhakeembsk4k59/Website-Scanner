#!/user/python2

import os
import sys

#This tool is coded in python by Abdul hakeem Shaik

print("\033[93m ")
os.system("figlet Abdul Hakeem Shaik")
url = raw_input("[+] Enter Website : ")
os.system("whois %s " % (url))

