import os
import platform
'''

'''
OS = platform.system()
if OS == 'Linux':
    print("t es pas sur widows")
elif OS == 'Windows':
    print("tu es sur widows")
    launche=True
    while launche:
        choix=input("que veux tu ouvrir : 1- github 2-vscode")
        if choix == "1":
            os.system("git.bat")
        elif choix =="2":
            os.system("vs.bat")