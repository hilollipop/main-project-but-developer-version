#version 0.0.1
import os
x = True
def little():
    print(""" sign in
 developer sing in
 login
 exit
    """)



def little_list():
    print(""" new account
 account
 account look
 account rm
 kimlik rm
    """)

def U():
    x = True
    while x == True:
        print("error >>>>>>>>> code: unknown error <type the error to send a report.> ")
        input(':')
        print('UwU thanks')
        x = False
    if x == False:
        while x == False:
            print('''            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
            errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror
''')
            print('UwU LOL. <hahhahahahahhahahahaha yuubii !!!>')

def UwU():
    print("error >>>>>>>>> code: unknown error <type the error to send a report.> ")
    input(':')
    print('UwU thanks')

def UUwU():
    print("<type the error to send a report.> <!!!!>")
    input(':')
    print('UwU thanks')
    e()

def login():
    print("hello")
    e()




def no_hello():
    e()



def sign_in():
    dosya = open("yo.u.UwU", "a")
    n = input("enter name : ")
    p = input("enter passwork:")
    dosya.write(n)
    dosya.write(p)
    dosya.close()
    no_hello()

def d():
    dosya = open("yo.w.UwU", "a")
    d = input("1. kimlik girin:")
    dd = input("2. kiklik bilmemsi sayı lütfen:")
    ddd = input("2. kiklik bilmemsi sayı lütfen:")
    k = print(dd + ddd)
    dosya.write(d)
    dosya.write(dd + ddd)
    dosya.close()
    sign_in()






def l():
    os.remove("yo.u.UwU")



def k():
    os.remove("yo.w.UwU")




def t():
    dosya = open("yo.u.UwU","r")
    print(dosya.read())



def e(c = True):
    nt = input ("enter alias:")
    if nt == "little butterfly":
        UwU()
        print('sorry please type another bi alias')
        nt = input ("enter alias:")
    elif nt == "snowie":
        UwU()
        print('sorry please type another bi alias')
        nt = input ("enter alias:")
    elif nt == "killing butterflies":
        UwU()
        print('sorry please type another bi alias')
        nt = input ("enter alias:")
    elif nt == "dead butterflies":
        UwU()
        print('sorry please type another bi alias')
        nt = input ("enter alias:")
        
    if nt == "little":
        print('lb:<little butterfly> , kb <killing butterflies> , db <dead butterflies> .')
        n = input()
        if n == "lb":
            nt = "little butterfly"
        elif n == "kb":
            nt = "killing butterflies"
        elif n == "db":
            nt = "dead butterflies"
        elif n == "db":
            nt = "snowie"
    while c == True:
        m = input("message enter:")
        if m == 'commands':
            print('alias edit, exit, back.')
        if m == 'error':
            U()
        if m == "report":
            UUwU()
        if m == 'alias edit':
            nt = input("enter alias:")
            if nt == "little butterfly":
                UwU()
                print('sorry please type another bi alias')
                nt = input ("enter alias:")
            elif nt == "killing butterflies":
                UwU()
                print('sorry please type another bi alias')
                nt = input ("enter alias:")
            elif nt == "dead butterflies":
                UwU()
                print('sorry please type another bi alias')
                nt = input ("enter alias:")
            elif nt == "lb":
                nt = "little butterfly"
            elif nt == "kb":
                nt = "killing butterflies"
            elif nt == "db":
                nt = "dead butterflies"
        f = ("{}: {}".format(nt,m))
        print(f)
        if m == "exit":
            print("goodbye")
            exit(little)
        if  m == "back":
            c = False



while x == True:
    little()
    p = (input("please choose what to do:"))
    if p == "sing in":
        sign_in()
    elif p == "login":
        login()
    elif p == "account look":
        t()
    elif p == "account rm":
        l()
    elif p == "kimlik rm":
        k()
    elif p == "developer sing in":
        d()
    elif p == "little e":
        e()
    elif p == "list":
        little_list()
    elif p ==  "exit" :
        print("goodbye")
        exit(little)
        