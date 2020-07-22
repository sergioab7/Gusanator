#!/usr/bin/python3
#coding: utf-8

#Autor: xaxxjs


from colorama import Fore, Back, Style
import sys
import os
import shutil
import signal
import time
from subprocess import call

if(os.getuid() != 0):
    print(Fore.RED + "[!] Debes tener privilegios root para este script!"+Fore.RESET)
    sys.exit(1)


os.system("clear")

print(Style.BRIGHT)
def signal_handler(key,frame):
    print(Fore.YELLOW + "\n\n\t[*]" + Fore.RESET + "Exiting...\n")
    print(Style.RESET_ALL)
    sys.exit(1)

signal=signal.signal(signal.SIGINT,signal_handler)

def help():
        print(""" 

        ----------------      ---------------------------
       |    COMMAND     |    |         DESCRIPTION       |
        ----------------      ---------------------------
        
        CREATE                New worm


        VERSION               Last version
        ABOUT                 Information about program
        HELP                  List of commands

        CLEAR                 Clear the screen
        EXIT                  Exit

        """)

def about():
    print("""
    
        -----------------------------
       |            ABOUT            |
        -----------------------------

        ¡Use it in controlled environments, it can cause a lot of damage to your computer!
        I am not responsible for the use that you can give it.


        It is a very simple program capable of creating worms and spreading through your folders all over your computer.

    """)

def simple_worm():

    eleccion_archivos=int(input(Fore.YELLOW + "\n[+] Select: \n\t[1] Files\n\t[2] Folder\n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm)>" +Fore.RESET))
    while(eleccion_archivos is not None):
        if(eleccion_archivos==1):
            while True:
                name=input(Fore.GREEN + "\n\t[+] Worm filename>> \n"+ Fore.RESET + Fore.BLUE + "[00] back \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                if(name=="00"):
                    break
                extension=input(Fore.GREEN + "\n\t[+] Worm filename extension(php,txt,jpg...)>> \n"+ Fore.RESET + Fore.BLUE + "[00] back \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                if(extension=="00"):
                    break
                existe_name=name+str(1)+'.'+extension
                while(os.path.exists(existe_name)):
                    print("\n[!] El archivo ya existe, elija otro.")
                    name=input(Fore.GREEN + "\n\t[+] Worm filename>> \n"+ Fore.RESET + Fore.BLUE + "[00] back \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                    existe_name=name+str(1)+'.'+extension

                veces=int(input(Fore.GREEN + "\n\t[+] Number of times to repeat>> \n"+Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET))
                

                contenido=input(Fore.YELLOW + "\n\t[+] Add content to files(y/n) >> \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                contenido = contenido.lower()

                while contenido is not None:
                    if(contenido=='y'):
                        add_content=input(Fore.GREEN + "\n\t[+] Content >> \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                        break
                    elif(contenido=='n'):
                        add_content=""
                        break 
                    else:
                        print("[-]Command not found")
                        contenido=input(Fore.YELLOW + "\n\t[+] Add content to files(y/n) >> \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                        contenido = contenido.lower()


                if(len(add_content)>0):
                    print(Fore.YELLOW + "\n\t[!] Save: %s.%s x %s, with content."%(name,extension,veces) + Fore.RESET)
                else:
                    print(Fore.YELLOW + "\n\t[!] Save: %s.%s x %s, without content."%(name,extension,veces) + Fore.RESET)

                correct=input(Fore.BLUE + "\n\t[*] Continue? >>(y/n)\n"+Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)
                correct=correct.lower()
                while correct is not None:
                    if(correct=='y'):
                        for n in range(0,int(veces)):
                            if(len(add_content)>0):
                                call(['touch', name+str(n+1)+'.'+extension])
                                archivo=open(name+str(n+1)+'.'+extension, "w")
                                archivo.write(add_content)
                                archivo.close()
                            else:
                                call(['touch', name+str(n+1)+'.'+extension])
                        directorio=os.getcwd()
                        time.sleep(1.5)
                        print(Fore.YELLOW + "\n\t[SUCCESS] Worm '%s.%s' created with '%s' files in %s. \n\n"%(name,extension,veces,directorio) + Fore.RESET)
                        print(Fore.YELLOW+"\t Exit...\n"+Fore.RESET)
                        sys.exit(1)
                    elif(correct=='n'):
                        break
                    else:
                        print("[-]Command not found")
                        correct=input("[*] Continue>>(y/n)\n"+ Fore.RED+ "(gusanator/create/simple_worm/files)>" +Fore.RESET)

        elif(eleccion_archivos==2):
            while True:
                try:
                    name=input(Fore.GREEN + "\n\t[+] Worm folder>> \n"+ Fore.RESET + Fore.BLUE + "[00] back \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/folder)>" +Fore.RESET)
                    while(os.path.isdir(name)):
                        print("[-] Folder exists, change name.")
                        name=input(Fore.GREEN + "\n\t[+] Worm folder>> \n"+ Fore.RESET + Fore.BLUE + "[00] back \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/folder)>" +Fore.RESET)
                    if(name==00):
                        break
                    veces=int(input(Fore.GREEN + "\n\t[+] Number of times to repeat>> \n"+Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm/folder)>" +Fore.RESET))


                    for n in range(0,veces):
                        call(['mkdir', name+str(n+1)])
                    print("\n[+]Creating....")
                    time.sleep(1.5)
                    
                    directorio=os.getcwd()
                    print(Fore.YELLOW + "\n\t[SUCCESS] Folder created in: %s.\n\n"%(directorio) + Fore.RESET)
                    time.sleep(1.5)
                    sys.exit(1)
                except Exception as e:
                    print("Error: %s"%(e))
                    


        else:
            print("[-] Command not found")
            eleccion_archivos=int(input(Fore.YELLOW + "\n[+] Select: \n\t[1] Files\n\t[2] Folder\n"+ Fore.RESET + Fore.RED+ "(gusanator/create/simple_worm)>" +Fore.RESET))


def advanced_worm():
    print(Fore.YELLOW + "\n\t[WARNING]" + Fore.RESET + " ¡Be careful with the use of the program! \n")
    print(Fore.BLUE + "\t[INFO] You must start the script in the directory you want it to run" + Fore.RESET)
    while True:
        name=input(Fore.GREEN + "\n\t[+] Worm filename>> \n"+ Fore.RESET + Fore.BLUE + "[00] back \n"+ Fore.RESET + Fore.RED+ "(gusanator/create/advanced_worm)>" +Fore.RESET)
        if(name=="00"):
            break
        veces=int(input(Fore.GREEN + "\n\t[+] Number of times to repeat>> \n"+Fore.RESET + Fore.RED+ "(gusanator/create/advanced_worm)>" +Fore.RESET))

        correct=input(Fore.BLUE + "\n\t[*] Do you want continue? >>(y/n)\n"+Fore.RESET + Fore.RED+ "(gusanator/create/advanced_worm)>" +Fore.RESET)
        while(correct is not None):
            if(correct=='y'):
                print("[+] Starting...")
                time.sleep(1.5)
                actual=os.getcwd()
                for root,dirs,files in os.walk(actual):
                    for i in range(0, veces):
                        call(['mkdir', root+'/'+name+str(i)])
            elif(correct=="n"):
                break
            else:
                print("[-]Command not found")
                correct=input("[*] Continue>>(y/n)\n"+ Fore.RED+ "(gusanator/create/advanced_worm)>" +Fore.RESET)

        print(Fore.YELLOW + "\n\t[SUCCESS] All created." + Fore.RESET)
        time.sleep(1.5)
        sys.exit(1)
        

        

def version():
    print("""
    
        -----------------------------
       |            VERSION          |
        -----------------------------

        It's currently version 0.1

    """)

def create():
    eleccion=(""" 
        
        --------          ----------------------
       | NUMBER |        |    DESCRIPTION      |
        --------          ----------------------

         [01]               Simple Worm (The same folder you're in)
         [02]               Advanced Worm (All your pc)

         [99]               Back to menu

    """)
    print(eleccion)
    while True:
        elegir=input(Fore.RED+'(gusanator/create)>'+Fore.RESET)
        if(elegir=="01"):
            simple_worm()
        elif(elegir=="02"):
            advanced_worm()
        elif(elegir=="help"):
            print(eleccion)
        elif(elegir=="99"):
            break
        else:
            print("[-]Command not found")
banner="""
                                -  /
                               (o)(o)
                              /      |
                             /       |
                            /   \  * |
              ________     /    /\__/
      _      /        \   /    /
     / \    /  ____    \_/    /
    //\ \  /  /    \         /
    V  \ \/  /      \       /       by:xaxxjs
        \___/        \_____/        v0.1

"""

print(banner)
print("\tWelcome to gusanator, write <help> to more info.\n\n")

while True:
    datos=input(Fore.RED+'(gusanator)>'+Fore.RESET)
    datos = datos.lower()
    try:
        if(datos=="help"):
            help()
        elif(datos=="about"):
            about()
        elif(datos=="version"):
            version()
        elif(datos=="create"):
            create()
        elif(datos=="clear"):
            os.system("clear")
            print(banner)
        elif(datos=="exit"):
            sys.exit(1)
        else:
            print(Fore.YELLOW+"[-]"+Fore.RESET+"Command not found.")
    except Exception as e:
        print("Error %s"%(e))
        