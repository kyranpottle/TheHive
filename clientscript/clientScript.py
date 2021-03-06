#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:15:45 2018

TheHive Client Host Script
  ________         __  ___          
 /_  __/ /_  ___  / / / (_)   _____ 
  / / / __ \/ _ \/ /_/ / / | / / _ \ 
 / / / / / /  __/ __  / /| |/ /  __/
/_/ /_/ /_/\___/_/ /_/_/ |___/\___/ 
             monetize your PC 

@author: Kyran Pottle
"""


import urllib.request
#import socket
#import os
import sys
import time
import subprocess


logo = "  ________         __  ___          \n /_  __/ /_  ___  / / / (_)   _____ \n  / / / __ \/ _ \/ /_/ / / | / / _ \ \n / / / / / /  __/ __  / /| |/ /  __/\n/_/ /_/ /_/\___/_/ /_/_/ |___/\___/ \n             monetize your PC       \n" #you what? XD
print(logo)
time.sleep(0.5)


'''-------------------------
    INSTALL/UPDATE PACKAGES
   -------------------------'''

print("[PIP INSTALL FLASK]")
subprocess.call(["pip", "install", "flask"])
print("[PIP INSTALL SOCKETIO]")
subprocess.call(["pip", "install", "socketio"])
print("[PIP INSTALL PYMONGO]")
subprocess.call(["pip", "install", "pymongo"])
print("[PIP INSTALL EVENTLET]")
subprocess.call(["pip", "install", "eventlet"])



'''-----------
    BENCHMARK
   -----------'''
   
tier = 0
pi = 3.141592

start = time.time() / 60 #divide by 60 because there's 60 seconds in a minute
print("\n[BENCHMARKING]")



'''
The benchmarking here works by timing how long the CPU takes to complete a large amount of mathematically complex tasks
'''

for i in range(1,1000):
    if i % 13 == 0:
        print("#", end = "", flush = True)
              
    for x in range(1,1000):
        pi * 2**x

    for x in range(1,1000):
        float(x) / pi
            
        for x in range(1,1000):
            float(pi) / x
            
            
                
end = time.time() / 60

duration = end - start

time.sleep(0.5)



'''-------------
    ASSIGN TIER
   -------------'''

if duration <= 1.5:
    tier = 1 #£0.05/m
elif duration <= 2:
    tier = 2 #£0.025/m
elif duration <= 2.5:
    tier = 3 #£0.005/m
else:
    tier = 4 #£0.0005/m


subprocess.call(["clear"])
print(logo)



'''-------
    STATS
   -------'''

print("[Tier " + str(tier) + "]") #what tier plan the machine is on

#get ip in JSON
ip = ""
src = urllib.request.urlopen("https://api.ipify.org/?format=json")
json = src.read().decode()

#extract ip
for letter in json:
    if letter.isdigit() or letter == ".":
        ip += str(letter)

print("IP: " + ip +"\n")
print("Awaiting Connection...")

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

loop = True
count = 0

while loop:
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
    count =+ 1
    if count == 3750:
        loop = False
    ### TODO: Set loop to False when connection detected ###



#############################
### TODO: SECURITY ISSUES ###
#############################

# Possible stack overflow / divide by zero exploit if the user changes the system time

# Changing system time during benchmarking could result in a higher tier being achieved

