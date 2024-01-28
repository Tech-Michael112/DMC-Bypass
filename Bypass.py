import os, sys,time
os.system('clear')
print(""" 
██████  ██    ██ ██████   █████  ███████ ███████     
██   ██  ██  ██  ██   ██ ██   ██ ██      ██          
██████    ████   ██████  ███████ ███████ ███████     
██   ██    ██    ██      ██   ██      ██      ██     
██████     ██    ██      ██   ██ ███████ ███████     
[~] Bypassed By Michael
[~] Run this tool to continue
[~] Send key to Mr-Michael 
[~] Bypass version - [1.0]

""") 
time.sleep(3)
#os.system('xdg-open https://chat.whatsapp.com/GO3uvcJyyDpCQFHL48vlF3')
try:
    __import__("HAX").menu()
except Exception as e:
    exit(str(e))
