import zipfile as zp
import os
import time
tst = 0
def ext(zipname , password):
    try:
        z = zp.ZipFile(zipname , 'r')
        ps = password.encode()
        z.extractall(pwd=ps)
        z.close
        print('[+] password is ==>> ' + password)
        global tst
        tst+=1
    except:
        pass
        

def mainF(zname , passname):
    while True:
        try:
            zp.ZipFile(zname)
        except:
            print('unknown file')
            time.sleep(3)
            break
        zfile = zname
        passfile = open(passname)
        c = 0
        for line in passfile.readlines():
            password = line.split()
            password=password[0]
            c+=1
            print('try : '+str(c)+'| pass in use : '+ password[0])
            btr = ext(zfile , password)
            global tst
            if tst == 1:
                print('}=== Password Cracked ==={')
                input('for back to menu click enter >> ')
                tst = 0
                break


            
    
        


def banner():
    os.system('cls')
    print('''
     _____                _             
    /  __ \              | |            
 ___| /  \/_ __ __ _  ___| | _____ _ __ 
|_  / |   | '__/ _` |/ __| |/ / _ \ '__|
 / /| \__/\ | | (_| | (__|   <  __/ |   
/___|\____/_|  \__,_|\___|_|\_\___|_|   
                                        
========================================                                 
-------------- Welcome -----------------
----------------------------------------

    [1] >> START CRACKER
    [2] >> Developer

=========================================

    ''')
def banner2():
    os.system('cls')
    print(''' 

     _____                _             
    /  __ \              | |            
 ___| /  \/_ __ __ _  ___| | _____ _ __ 
|_  / |   | '__/ _` |/ __| |/ / _ \ '__|
 / /| \__/\ | | (_| | (__|   <  __/ |   
/___|\____/_|  \__,_|\___|_|\_\___|_|  

=========================================
                                        
                                    
    
    [1] >> Start default
    [2] >> Strat custom
    
    
    ''')

def dev():
    os.system('cls')
    print(''' 
     _____                _             
    /  __ \              | |            
 ___| /  \/_ __ __ _  ___| | _____ _ __ 
|_  / |   | '__/ _` |/ __| |/ / _ \ '__|
 / /| \__/\ | | (_| | (__|   <  __/ |   
/___|\____/_|  \__,_|\___|_|\_\___|_|   
                                        
                                    

    name = Alimoini     insta = Alimoio0

    press Enter to back >> ''')

def main():
    while True:
        try:
            banner()
            sel = int(input('>>>   '))
            if sel == 1:
                banner2()
                cus = int(input(' >> '))
                while True:
                    try:
                        if cus == 1:
                            print('Enter file name or address')
                            zname = input('>> ')
                            mainF(zname , 'passfile.txt')
                            break
                        if cus == 2:
                            zname6 = input('Enter zipfile name >> ')
                            pass6 = input("Enter your passfile name >> ")
                            mainF(zname6 , pass6)
                            break
                        else:
                            print('Enter correct number </> ')
                            time.sleep(3)
                            break
                    except:
                        pass
            if sel == 2:
                dev()
                input()
        except:
            print(' Error !!! </>  try again ')
            time.sleep(3)
main()





