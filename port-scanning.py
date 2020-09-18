import os

os.system("clear")

banner="""
ooooooooo.     .oooooo.   ooooooooo.   ooooooooooooo 
`888   `Y88.  d8P'  `Y8b  `888   `Y88. 8'   888   `8 
 888   .d88' 888      888  888   .d88'      888      
 888ooo88P'  888      888  888ooo88P'       888      
 888         888      888  888`88b.         888      
 888         `88b    d88'  888  `88b.       888      
o888o         `Y8bood8P'  o888o  o888o     o888o     

Port Tarama Aracı                    @ByHypertext
"""
print(banner)
hedef_ip=input("hedef-ip-adresi----->")
os.system("clear && nmap -sV "+hedef_ip)
input("")
