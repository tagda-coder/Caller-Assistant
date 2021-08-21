#!/usr/bin/env python 

"""
 Hello Guys This is Your Caller Assistant From this Script You will be Able to Make call in termux ..

 This Tool is Created by Mandeep 
 Malakar
      Use This Tool But Give Credits 

"""
# Requirements For this Tool 
'''
1.Python Programming
2.Termux
3.Termux-Api Apps and Packages 
        Installed 
4.Your Efforts

'''

# Import Module Called Os 

import os
os.system("clear")
print(" \033[1mWait Starting....!")
os.system("pkg install termux-api -y >/dev/null 2>&1")
os.system("clear") # Clear The Screen 
print("\033[1m\033[33m]\033[32m─────────────────────────────────────\033[33m[")
print("\033[33m\033[1m       Dear Users You Can Use \n\033[32m         This Tool for Calling. 📞 ")
print()
print("\033[1m\033[33m]\033[32m─────────────────────────────────────\033[33m[")
print("       \033[31m\033[42m\033[1m }-Coded By \033[36m\033[41mMandeep--{\033[0m")
print("]─────────────────────────────────────[")
print()
print()
code = int(input("\033[1m\033[35m[+] \033[33mEnter Your \033[37mCountry Code\033[32m[Ex-(+91) : \033[37m"))

print()
os.system("bash call.sh")





