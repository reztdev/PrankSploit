#!/usr/bin/python
# -*- coding: utf-8 -*-
import random, base64
class pycolor_style:
    def __init__(self):
        pass

    W = '\033[0m'
    R = '\033[1;31m'
    G = '\033[1;32m'
    Y = '\033[1;33m'
    B = '\033[1;34m'
    P = '\033[1;35m'
    C = '\033[1;36m'
    L = '\033[04m'

color = [
        pycolor_style.P, pycolor_style.B,
        pycolor_style.C, pycolor_style.G,
        pycolor_style.R, pycolor_style.W, 
        pycolor_style.Y
    ]
random_color = random.choice(color)

def banners():
    text = random_color + '''
    
  __________ _________      .__         .__  __   
  \______   /   ______/____ |  |   ____ |___/  |_ 
  |     ___\_____  \ \____ \|  |  /  _ \|  \   __\ 
  |    |   /        ||  |_> |  |_(  <_> |  ||  |  
  |____|  /_______  ||   __/|____/\____/|__||__|  
                 \/ |__|                         
''' + pycolor_style.W
    return text

def banner():
    banner = random_color + '''

   ██▓███   ██▀███   ▄▄▄       ███▄    █  ██ ▄█▀
   ▓██░  ██▒▓██ ▒ ██▒▒████▄     ██ ▀█   █  ██▄█▒
   ▓██░ ██▓▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▓███▄░
   ▒██▄█▓▒ ▒▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██ █▄
   ▒██▒ ░  ░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░▒██▒ █▄
   ▒▓▒░ ░  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒
   ░▒ ░       ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒ ▒░
   ░░         ░░   ░   ░   ▒      ░   ░ ░ ░ ░░ ░
             ░           ░  ░         ░ ░  ░''' + pycolor_style.W
    return banner

def banner_reztdev():
    banner = random_color + """
     ██▀███  ▓█████ ▒███████▒▄▄▄█████▓▓█████▄ ▓█████  ██▒   █▓
    ▓██ ▒ ██▒▓█   ▀ ▒ ▒ ▒ ▄▀░▓  ██▒ ▓▒▒██▀ ██▌▓█   ▀ ▓██░   █▒
    ▓██ ░▄█ ▒▒███   ░ ▒ ▄▀▒░ ▒ ▓██░ ▒░░██   █▌▒███    ▓██  █▒░
    ▒██▀▀█▄  ▒▓█  ▄   ▄▀▒   ░░ ▓██▓ ░ ░▓█▄   ▌▒▓█  ▄   ▒██ █░░
    ░██▓ ▒██▒░▒████▒▒███████▒  ▒██▒ ░ ░▒████▓ ░▒████▒   ▒▀█░
    ░ ▒▓ ░▒▓░░░ ▒░ ░░▒▒ ▓░▒░▒  ▒ ░░    ▒▒▓  ▒ ░░ ▒░ ░   ░ ▐░
      ░▒ ░ ▒░ ░ ░  ░░░▒ ▒ ░ ▒    ░     ░ ▒  ▒  ░ ░  ░   ░ ░░
      ░░   ░    ░   ░ ░ ░ ░ ░  ░       ░ ░  ░    ░        ░░
       ░        ░  ░  ░ ░                ░       ░  ░      ░
                    ░                  ░                  ░""" + pycolor_style.W
    return banner

def banner_bold():
  bn = random_color + """
   /$$$$$$$                        /$$     /$$$$$$$                      
  | $$__  $$                      | $$    | $$__  $$                     
  | $$  \ $$  /$$$$$$  /$$$$$$$$ /$$$$$$  | $$  \ $$  /$$$$$$  /$$    /$$
  | $$$$$$$/ /$$__  $$|____ /$$/|_  $$_/  | $$  | $$ /$$__  $$|  $$  /$$/
  | $$__  $$| $$$$$$$$   /$$$$/   | $$    | $$  | $$| $$$$$$$$ \  $$/$$/ 
  | $$  \ $$| $$_____/  /$$__/    | $$ /$$| $$  | $$| $$_____/  \  $$$/  
  | $$  | $$|  $$$$$$$ /$$$$$$$$  |  $$$$/| $$$$$$$/|  $$$$$$$   \  $/   
  |__/  |__/ \_______/|________/   \___/  |_______/  \_______/    \_/    
                                                                    """ + pycolor_style.W
  return bn

"""

 _______  _______  _______ _________ ______   _______          
(  ____ )(  ____ \/ ___   )\__   __/(  __  \ (  ____ \|\     /|
| (    )|| (    \/\/   )  |   ) (   | (  \  )| (    \/| )   ( |
| (____)|| (__        /   )   | |   | |   ) || (__    | |   | |
|     __)|  __)      /   /    | |   | |   | ||  __)   ( (   ) )
| (\ (   | (        /   /     | |   | |   ) || (       \ \_/ / 
| ) \ \__| (____/\ /   (_/\   | |   | (__/  )| (____/\  \   /  
|/   \__/(_______/(_______/   )_(   (______/ (_______/   \_/   
                                                               
"""

def banner_graf():
  b = """
    __________                 __ ________               
    \______   \ ____ _________/  |\______ \   _______  __
    |       _// __ .\\___   /\   __\    |  \_/ __ \  \/ /
    |    |   \  ___/ /    /  |  | |    `   \  ___/\   / 
    |____|_  /\___  >_____ \ |__|/_______  /\___  >\_/  
            \/     \/      \/             \/     \/      
"""
  return b

def banner_italic():
  word = random_color + """
                              __              __      _ __ 
      ____  _________ _____  / /___________  / /___  (_) /_
     / __ \/ ___/ __ `/ __ \/ //_/ ___/ __ \/ / __ \/ / __/
    / /_/ / /  / /_/ / / / / ,< (__  ) /_/ / / /_/ / / /_  
   / .___/_/   \__,_/_/ /_/_/|_/____/ .___/_/\____/_/\__/  
  /_/                              /_/                     
""" + pycolor_style.W
  return word


def banner_sploit():
  word = random_color + """
   ____  ____    ____  ____   __  _  _____ ____  _       ___  ____  ______ 
  |    \|    \  /    ||    \ |  |/ ]/ ___/|    \| |     /   \|    ||      |
  |  o  )  D  )|  o  ||  _  ||  ' /(   \_ |  o  ) |    |     ||  | |      |
  |   _/|    / |     ||  |  ||    \ \__  ||   _/| |___ |  O  ||  | |_|  |_|
  |  |  |    \ |  _  ||  |  ||     \/  \ ||  |  |     ||     ||  |   |  |  
  |  |  |  .  \|  |  ||  |  ||  .  |\    ||  |  |     ||     ||  |   |  |  
  |__|  |__|\_||__|__||__|__||__|\_| \___||__|  |_____| \___/|____|  |__|""" + pycolor_style.W
  return word

def word_banner():
  text_word = """
  +-==[ {rd}PrankSploit Framework Portable{rd1} (2.1.0)
  +-==[ Development: ReztDev, LocaLhost, AduDu, LazySec
  +-==[ {cy}{ln}{link}{ln1}{cy1}
  +-==[ Copyright (c) ReztDev, etc. All rights reserved.
""".format(
    link=base64.b64encode("https://github.com/ReztDev/PrankSploit2"),
    rd=pycolor_style.R, rd1=pycolor_style.W,
    cy=pycolor_style.C, cy1=pycolor_style.W,
    ln=pycolor_style.L, ln1=pycolor_style.W,
  )
  return text_word